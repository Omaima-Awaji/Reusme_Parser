import re
import json
from pypdf import PdfReader

def extract_text_from_pdf(file_path):

    reader = PdfReader(file_path)
    text = ""
    for pages in reader.pages:
        text += pages.extract_text()
    return text

def extract_name(text):
    text = re.sub(r' +', ' ', text)
    lines = text.split("\n")[:5]
    lines = "\n".join(lines)

    match = re.search(r"^([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)",lines,re.MULTILINE)
    if match:
        name = re.split(r'\s(?:Email|Phone|Address)', match.group(1))[0]
        return name.strip()
    match =  re.search(r"^([A-Z]+(?:[\s-][A-Z]+)+)", lines, re.MULTILINE)
    if match:
        name = re.split(r'\s(?:Email|Phone|Address)', match.group(1))[0]
        return name.strip()

    return "Name not found"




def extract_skills(text):
    match = re.search(r"Skills\s*:?\s*(.*?)(?=Experience|Education|$)",text,re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()

def extract_experience(text):
    match = re.search(r"Experience\s*:?\s*(.*?)(?=Education|Skills|$)", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()

def extract_email(text):
    match = re.search(r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}", text)
    if match:
        return match.group().strip()

def extract_phone(text):
    match = re.search(r"[\+]?[\d\s\-\(\)]{7,15}",text)
    if match:
        return match.group().strip()

def extract_education(text):
    match = re.search(r"Education\s*:?\s*(.*?)(?=Experience|Skills|$)",text,re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()

def export_to_json(name, email, phone, skills, experience, education):
    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "experience": experience,
        "education": education,

    }
    with open("resume.json", "w") as f:
        json.dump(data, f, indent=4)

def match_job_description(skills, job_description):
    skills_list = skills.split(",")
    matches = 0
    for skill in skills_list:
        if skill.strip().lower() in job_description.lower():
            matches += 1
    return round((matches / len(skills_list)) * 100, 2)


if __name__ == "__main__":
    file_path = input("Please enter the file path of the resume: ")
    text = extract_text_from_pdf(file_path)
    text = re.sub(r' {4,}', '\n', text)
    text = re.sub(r' {2,}', ' ', text)

    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)
    experience = extract_experience(text)
    education = extract_education(text)

    print("\n--- Resume Results ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Skills: {skills}")
    print(f"Experience: {experience}")
    print(f"Education: {education}")

    export_to_json(name, email, phone, skills, experience, education)
    print("\n✅ Results exported to resume.json")

    job_description = input("\nPaste the job description to check match score:\n")
    if skills:
        score = match_job_description(skills, job_description)
        print(f"\n🎯 Match Score: {score}%")
    else:
        print("No skills found to match.")