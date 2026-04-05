import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

from app_modules.user_inputs import collect_user_inputs
user_data = collect_user_inputs()

# ===== 加载 API Key =====
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Resume Generator", layout="wide")
st.title("📄 AI Resume Generator")


# ===== 点击按钮生成简历内容 =====
if st.button("✏️ Gnerate Resume"):
    with st.spinner("Generating resume content..."):

        # ===== 使用 GPT 生成 自我介绍 + 工作内容条目 =====
        summary_prompt = f"""
        Please write a resume summary paragraph (about 100 words).
        Based on the following self-introduction and career goal, 
        Introduction: {user_data['intro_brief']}
        Career Goal: {user_data['career_goal']}
        Highlight the applicant's strengths and competitiveness in the workplace.
        Don't fabricate informations!
        """

        edu_achievements_prompt = f"""
        Please write bullet points for resume about this role:
        Each bullet point correporate an eduction achievement: {user_data['edu_achievements']}
        Display succinctly and clearly
        Don't omit any achievement！
        Don't fabricate informations!
        """

        work_prompt = f"""
        Please write 3-5 bullet points for resume about this role:
        Job Title: {user_data['job_title']}
        Company: {user_data['job_company']}
        Location: {user_data['job_location']}
        Time: {user_data['job_time']}
        Responsibilities: {user_data['job_responsibilities']}
        Achievements: {user_data['job_achievements']}
        Use short, action-driven English. Start each line with a verb.
        Don't fabricate informations!
        """

        skills_prompt = f"""
        My skills include: {user_data['tech_skills']}, {user_data['long_skills']}, {user_data['soft_skills']}. 
        Please write a bullet-point style resume skills section.
        Don't fabricate informations!
        """

        summary_text = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": summary_prompt}],
            temperature=0.5
        ).choices[0].message.content.strip()

        work_result = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": work_prompt}],
            temperature=0.4
        ).choices[0].message.content.strip()

        skills = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": skills_prompt}],
            temperature=0.3
        ).choices[0].message.content

        academic_achievements = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": edu_achievements_prompt}],
            temperature=0.0
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
Relevant courses: {user_data['courses']}
Academic achievements: 
{academic_achievements}

#### Work Experience:  
**{user_data['job_title']}** | {user_data['job_company']} — {user_data['job_location']} | {user_data['job_time']}  
{work_result}

#### Skills:  
{skills}
"""
    st.subheader("📄 Generate result preview")
    st.markdown(resume)

# cd "C:\Users\sheng\.vscode\cli\Resume Generator\"
# python -m streamlit run app.py
