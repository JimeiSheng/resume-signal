import streamlit as st

def collect_user_inputs():
    # ===== 1. Fundamental Information =====
    st.header("🧑‍🎓 Personal information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
        phone = st.text_input("Phone number")
        email = st.text_input("Email")
    with col2:
        github = st.text_input("LinkedIn / GitHub (optional)")
        age = st.text_input("Age")
        gender = st.selectbox("Gender", ["", "Male", "Femal", "Others"])

    # ===== 2. Education Background =====
    st.header("🎓 Education Background")
    school = st.text_input("School")
    edu_start = st.text_input("Year of enrollment")
    edu_end = st.text_input("Graduation year/Expected graduation year")
    major = st.text_input("Major")
    degree = st.text_input("Degree (Bachelor's, Master's, Doctoral, etc.)")
    courses = st.text_area("Related courses (optional)")
    edu_achievements = st.text_area("Academic achievements (grades, awards, etc.)")

    # ===== 3. Work Experience =====
    st.header("💼 Work Experience")
    job_title = st.text_input("Job title")
    job_company = st.text_input("Company name")
    job_location = st.text_input("Job location")
    job_time = st.text_input("Work duration (e.g. June 2023 - present)")
    job_responsibilities = st.text_area("Work content (brief)")
    job_achievements = st.text_area("Work achievements (optional)")

    # ===== 4. Project Experience =====
    st.header("🚀 Project Experience")
    project_name = st.text_input("Project name")
    project_description = st.text_area("Project description")
    project_time = st.text_input("Project duration (e.g. June 2023 - present)")
    project_tech = st.text_input("Technologies used")
    project_role = st.text_input("Your role in the project")
    project_achievements = st.text_area("Project achievements (optional)")

    # ===== 5. Skills =====
    st.header("🧠 Skills")
    tech_skills = st.text_input("Technical skills")
    lang_skills = st.text_input("Language ability")
    soft_skills = st.text_input("Other skills")

    # ===== 6. Self Introduction & Career Goal =====
    st.header("🎯 Job Objective and Introduction")
    career_goal = st.text_input("Target position/industry")
    intro_brief = st.text_area("Self-introduction (2-4 sentences)")

    user_data = {
    "name": name,
    "age": age,
    "phone": phone,
    "email": email,
    "github": github,
    "gender": gender,

    "school": school,
    "edu_start": edu_start,
    "edu_end": edu_end,
    "major": major,
    "degree": degree,
    "courses": courses,
    "edu_achievements": edu_achievements,

    "job_title": job_title,
    "job_company": job_company,
    "job_location": job_location,
    "job_time": job_time,
    "job_responsibilities": job_responsibilities,
    "job_achievements": job_achievements,

    "project_name": project_name,
    "project_description": project_description,
    "project_time": project_time,
    "project_tech": project_tech,
    "project_role": project_role,
    "project_achievements": project_achievements,

    "tech_skills": tech_skills,
    "lang_skills": lang_skills,
    "soft_skills": soft_skills,

    "career_goal": career_goal,
    "intro_brief": intro_brief
    }

    return user_data