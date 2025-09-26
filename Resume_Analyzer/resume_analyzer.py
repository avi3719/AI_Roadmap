import re

# ✅ Define important keywords recruiters look for
important_keywords = [
    "Python", "SQL", "Machine Learning", "Data Analysis",
    "Communication", "Teamwork", "Problem Solving", "Java",
    "Artificial Intelligence", "Git", "Deep Learning"
]

def analyze_resume(resume_text):
    found = []
    missing = []
    
    for keyword in important_keywords:
        if re.search(rf"\b{keyword}\b", resume_text, re.IGNORECASE):
            found.append(keyword)
        else:
            missing.append(keyword)
    
    print("✅ Skills Found in Resume:", found)
    print("❌ Skills Missing from Resume:", missing)

# Example resume text (later we can read from PDF)
resume_text = """
I am Avishkar, a B.Sc. IT student. I know Python, SQL, and have done data analysis projects.
I also worked on Machine Learning and GitHub projects with my team.
"""

analyze_resume(resume_text)
