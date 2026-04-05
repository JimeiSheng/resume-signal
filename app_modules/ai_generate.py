def ai_prompt(user_data):

    summary_prompt = f"""
    Please write a resume summary paragraph (about 100 words).
    Based on the following self-introduction and career goal, 
    Introduction: {user_data['intro_brief']}
    Career Goal: {user_data['career_goal']}
    Job Achievements: {user_data['job_achievements']}
    Eduction achievement: {user_data['edu_achievements']}
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

    project_prompt = f"""
    Please write 3-5 bullet points for resume about this project:
    Project Name: {user_data['project_name']}
    Description: {user_data['project_description']}
    Time: {user_data['project_time']}
    Technologies: {user_data['project_tech']}
    Role: {user_data['project_role']}
    Achievements: {user_data['project_achievements']}
    Use short, action-driven English. Start each line with a verb.
    Don't fabricate informations!
    """

    skills_prompt = f"""
    My skills include: {user_data['tech_skills']}, {user_data['lang_skills']}, {user_data['soft_skills']}. 
    Please write a bullet-point style resume skills section.
    Don't fabricate informations!
    """

    result = {    
    "summary_prompt": summary_prompt,
    "edu_achievements_prompt": edu_achievements_prompt,
    "work_prompt": work_prompt,
    "project_prompt": project_prompt,
    "skills_prompt": skills_prompt
    }
    return result