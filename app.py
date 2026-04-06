import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import re

from app_modules.user_inputs import collect_user_inputs
from app_modules.ai_generate import ai_prompt

# ===== 页面配置 =====
st.set_page_config(page_title="AI Resume Generator", layout="wide")
st.title("📄 AI Resume Generator")

# ===== 初始化状态 =====
if "resume" not in st.session_state:
    st.session_state.resume = ""

if "debug" not in st.session_state:
    st.session_state.debug = ""

# ===== API KEY =====
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY not found")
    st.stop()

client = OpenAI(api_key=api_key)

# ===== 用户输入 =====
user_data = collect_user_inputs()

# ===== 生成按钮 =====
if st.button("✏️ Generate Resume"):
    with st.spinner("Generating resume..."):
        try:
            prompt = ai_prompt(user_data)

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                response_format={"type": "json_object"}
            )

            raw_output = response.choices[0].message.content

            if not raw_output:
                st.error("❌ Model returned empty output")
                st.stop()

            st.session_state.debug = raw_output

            # ===== JSON解析函数 =====
            def extract_json(text):
                try:
                    return json.loads(text)
                except:
                    pass

                # 去掉 ```json ``` 包裹
                text = text.strip()
                if text.startswith("```"):
                    text = text.split("```")[1]

                try:
                    return json.loads(text)
                except:
                    pass

                start = text.find("{")
                end = text.rfind("}")
                if start != -1 and end != -1:
                    return json.loads(text[start:end+1])
                return None

            result = extract_json(raw_output)
            if not result:
                st.error("❌ Failed to parse JSON")
                st.write(raw_output)
                st.stop()

            # ===== 安全取值函数 =====
            def get_safe(value, default=""):
                if value is None:
                    return default
                return value

            # ===== 构建简历 =====
            resume = f"""
**{user_data.get('name') or 'Your Name'}**  
Mobile: {user_data.get('phone') or '-'}  
Email: {user_data.get('email') or '-'}  
{user_data.get('github') or ''}

---

### Summary
{get_safe(result.get('summary'), '-')}
"""
            # ===== Education =====
            # education uses user_data only
            school = user_data.get("school")
            degree = user_data.get("degree")
            major = user_data.get("major")
            year = user_data.get("edu_end")

            resume += "### Education\n"
            # First line
            if major:
                resume += f"{school} | {degree} in {major}  \n"
            else:
                resume += f"{school} | {degree}  \n"
            # Second line (you control the format, don't let AI mess it up)
            if year:
                resume += f"Expected Graduation {year}  \n"
            # Third line (just use user input, most reliable)
            courses = user_data.get("courses")
            if courses:
                resume += f"\nCourses: {courses}\n"

            # ==== Academic Achievements ====
            edu_ach = get_safe(result.get("education_achievements"), [])
            if edu_ach:
                resume += "\n**Academic Achievements:**\n"
                for b in edu_ach:
                    resume += f"- {b}\n"

            # ===== Work Experience =====
            work = get_safe(result.get("work_experience"), [])
            if work:
                resume += "\n### Work Experience\n"
                for job in work:
                    # support dict or string
                    if isinstance(job, dict):
                        title_line = job.get("position_company_location_time", "")
                        resume += f"**{title_line}**\n"
                        for detail in job.get("details", []):
                            # Mark empty details in red to prompt user to fill them in later
                            if not detail.strip():
                                resume += f"- <span style='color:red'>[Please fill]</span>\n"
                            else:
                                resume += f"- {detail}\n"
                    else:
                        resume += f"- {job}\n"

            # ===== Project Experience =====
            project = get_safe(result.get("project_experience"), [])
            if project:
                resume += "\n### Project Experience\n"
                for proj in project:
                    if isinstance(proj, dict):
                        title_line = proj.get("name_role_time", "")
                        resume += f"**{title_line}**\n"
                        for detail in proj.get("details", []):
                            if not detail.strip():
                                resume += f"- <span style='color:red'>[Please fill]</span>\n"
                            else:
                                resume += f"- {detail}\n"
                    else:
                        resume += f"- {proj}\n"

            # ===== Skills =====
            skills_raw = result.get("skills")

            resume += "\n### Skills\n"

            # Situation1: ideal case (dict)
            if isinstance(skills_raw, dict):
                technical = skills_raw.get("technical", "")
                languages = skills_raw.get("languages", "")
                other = skills_raw.get("other", "")

                if technical:
                    resume += f"Technical: {technical}  \n"
                if languages:
                    resume += f"Languages: {languages}  \n"
                if other:
                    resume += f"Other: {other}  \n"

            # Situation2: AI occasionally returns a string (fallback)
            elif isinstance(skills_raw, str):
                import re

                # Automatically split into multiple lines
                lines = re.split(r'(?=Technical:|Languages:|Other:)', skills_raw)

                for line in lines:
                    if line.strip():
                        resume += f"{line.strip()}  \n"

            # Situation3: Completely missing (防空)
            else:
                resume += "-\n"
            
            st.session_state.resume = resume

        except Exception as e:
            st.error(f"❌ Error: {e}")

# ===== Display Result =====
if st.session_state.resume:
    st.subheader("📄 Generated Resume")
    st.markdown(st.session_state.resume, unsafe_allow_html=True)

# ===== Debug =====
with st.expander("🔍 Debug (model raw output)"):
    st.code(st.session_state.debug)

#   python -m streamlit run app.py
