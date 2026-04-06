def ai_prompt(user_data):

    def clean(data, key):
        value = data.get(key)
        return value.strip() if value and value.strip() else ""

    # ===== Clean User Data =====
    cleaned_data = {
        "name": clean(user_data, "name"),
        "phone": clean(user_data, "phone"),
        "email": clean(user_data, "email"),
        "github": clean(user_data, "github"),

        "school": clean(user_data, "school"),
        "degree": clean(user_data, "degree"),
        "major": clean(user_data, "major"),
        "edu_end": clean(user_data, "edu_end"),
        "courses": clean(user_data, "courses"),
        "edu_achievements": clean(user_data, "edu_achievements"),

        "job_title": clean(user_data, "job_title"),
        "job_company": clean(user_data, "job_company"),
        "job_location": clean(user_data, "job_location"),
        "job_time": clean(user_data, "job_time"),
        "job_responsibilities": clean(user_data, "job_responsibilities"),
        "job_achievements": clean(user_data, "job_achievements"),

        "project_name": clean(user_data, "project_name"),
        "project_time": clean(user_data, "project_time"),
        "project_description": clean(user_data, "project_description"),
        "project_tech": clean(user_data, "project_tech"),
        "project_role": clean(user_data, "project_role"),
        "project_achievements": clean(user_data, "project_achievements"),

        "tech_skills": clean(user_data, "tech_skills"),
        "lang_skills": clean(user_data, "lang_skills"),
        "soft_skills": clean(user_data, "soft_skills"),

        "career_goal": clean(user_data, "career_goal"),
        "intro_brief": clean(user_data, "intro_brief"),
    }

    prompt = f"""
You are an ATS resume generator.

STRICT RULES:
- Do NOT fabricate anything
- If data is missing → output empty string for that field
- No explanations, no templates, no "Certainly"
- Output MUST be valid JSON only
- Use concise resume language
- No buzzwords, no exaggeration

OUTPUT FORMAT (STRICT JSON):

{{
  "summary": "",
  "education": {{
      "school": "",
      "degree": "",
      "major": "",
      "year": ""
  }},
  "education_achievements": [],
  "work_experience": [],
  "project_experience": [],
  "skills": {{}}
}}

INPUT DATA:
{{
  "name": "{cleaned_data.get('name')}",
  "career_goal": "{cleaned_data.get('career_goal')}",
  "intro_brief": "{cleaned_data.get('intro_brief')}",

  "school": "{cleaned_data.get('school')}",
  "degree": "{cleaned_data.get('degree')}",
  "major": "{cleaned_data.get('major')}",
  "edu_end": "{cleaned_data.get('edu_end')}",
  "courses": "{cleaned_data.get('courses')}",
  "edu_achievements": "{cleaned_data.get('edu_achievements')}",

  "job_title": "{cleaned_data.get('job_title')}",
  "job_company": "{cleaned_data.get('job_company')}",
  "job_location": "{cleaned_data.get('job_location')}",
  "job_time": "{cleaned_data.get('job_time')}",
  "job_responsibilities": "{cleaned_data.get('job_responsibilities')}",
  "job_achievements": "{cleaned_data.get('job_achievements')}",

  "project_name": "{cleaned_data.get('project_name')}",
  "project_description": "{cleaned_data.get('project_description')}",
  "project_time": "{cleaned_data.get('project_time')}",
  "project_tech": "{cleaned_data.get('project_tech')}",
  "project_role": "{cleaned_data.get('project_role')}",
  "project_achievements": "{cleaned_data.get('project_achievements')}",

  "tech_skills": "{cleaned_data.get('tech_skills')}",
  "lang_skills": "{cleaned_data.get('lang_skills')}",
  "soft_skills": "{cleaned_data.get('soft_skills')}"
}}

INSTRUCTIONS:

1. SUMMARY
- Max 40 words
- Focus on skills + career direction

2. EDUCATION
- Return structured fields ONLY
- Do NOT combine into sentences
- Do NOT include words like "Expected Graduation"

3. EDUCATION ACHIEVEMENTS
- Only if provided, 0–3 bullets
- Otherwise empty list []

4. WORK EXPERIENCE
- Return as a list of objects
Format:
[
  {{
    "position_company_location_time": "",
    "details": []
  }}
]
- position_company_location_time:
  Combine Position | Company — Location | Time
- details:
  1–3 bullet points mentioning responsibilities and achievements

5. PROJECT EXPERIENCE
- Return as a list of objects
Format:
[
  {{
    "name_role_time": "",
    "details": []
  }}
]
- name_role_time:
  Combine Project Name | Role | Time
- details:
  1–3 bullet points mentioning tech and results

6. SKILLS
- Return as JSON object:
{{
  "technical": "",
  "languages": "",
  "other": ""
}}
- Only use provided data, do NOT fabricate

RETURN JSON ONLY.
"""
    return prompt