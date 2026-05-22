# Resume Parser 📄

A command-line tool that extracts key information from PDF resumes and scores them against a job description, built with Python.

## Features
- Extracts name, email, and phone number
- Extracts skills, experience, and education sections
- Exports parsed results to a JSON file
- Scores resume against a job description based on skill matches
- Handles messy PDF formatting with text normalization

## How to Use
Run the script:

python resume_parser.py

Then follow the prompts:

Please enter the file path of the resume: C:/Users/YourName/Documents/resume.pdf

View the extracted results then paste a job description to get a match score:

Paste the job description to check match score:
> Looking for a Python developer with experience in pandas, requests, and SQL...

Match Score: 75.0%

## Example Output

--- Resume Results ---
Name: John Doe
Email: johndoe@example.com
Phone: +1234567890
Skills: Python, pandas, SQL, requests
Experience: 2 years at XYZ Company as a Data Analyst
Education: BSc Computer Science, University of XYZ

Results exported to resume.json

## Output Files
- resume.json - auto-generated file containing all extracted resume data

## Project Files
- resume_parser.py - main script
- sample_resume.pdf - sample resume for testing

## Requirements
- Python 3.x
- pypdf

## Installation
pip install pypdf
