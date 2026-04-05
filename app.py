import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

from app_modules.user_inputs import collect_user_inputs
user_data = collect_user_inputs()

from app_modules.ai_generate import ai_prompt
prompt = ai_prompt(user_data)

# ===== 加载 API Key =====
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Resume Generator", layout="wide")
st.title("📄 AI Resume Generator")

# ===== 使用 GPT 生成 自我介绍 + 工作内容条目 =====
if st.button("✏️ Gnerate Resume"):
    with st.spinner("Generating resume content..."):
        summary_text = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt['summary_prompt']}],
            temperature=0.5
        ).choices[0].message.content.strip()

        work_result = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt['work_prompt']}],
            temperature=0.4
        ).choices[0].message.content.strip()

        project_result = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt['project_prompt']}],
            temperature=0.4
        ).choices[0].message.content.strip()

        skills = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt['skills_prompt']}],
            temperature=0.3
        ).choices[0].message.content

        academic_achievements = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt['edu_achievements_prompt']}],
            temperature=0.2
        ).choices[0].message.content

# ===== 拼接最终简历文本（结构化） =====
    resume = f"""
**{user_data['name']}**  
Mobile: {user_data['phone']}  
Email: {user_data['email']}  
{user_data['github']}

#### Self-introduction:  
{summary_text}

#### Education:  
**{user_data['school']}**  
{user_data['degree']} degree in {user_data['major']} | Graduation: {user_data['edu_end']}  
Relevant courses: {user_data['courses']}\n
Academic achievements: 
{academic_achievements}

#### Work Experience:  
**{user_data['job_title']}** | {user_data['job_company']} — {user_data['job_location']} | {user_data['job_time']}  
{work_result}

#### Project Experience:  
**{user_data['project_name']}** | {user_data['project_time']}  
Technologies: {user_data['project_tech']} | Role: {user_data['project_role']}  
{project_result}

#### Skills:  
{skills}
"""
    st.subheader("📄 Generate result preview")
    st.markdown(resume)


# python -m streamlit run app.py
