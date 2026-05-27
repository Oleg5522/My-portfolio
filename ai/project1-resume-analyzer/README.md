# AI-Powered Resume Analyzer

A prompt engineering project built with Google AI Studio as part of an AI Essentials course.

## Concept

While the original assignment was to build an AI writing assistant (cover letter generator, resume enhancer, etc.), I approached it differently — I configured the AI to act as a hiring manager analyzing resumes of job candidates.

Having conducted around 150 job interviews across Ukraine, Africa, and the US, and having been a job seeker myself, I had a strong personal interest in testing how well AI can evaluate candidates.

## What the project does

- A custom system prompt configures the AI to act as a professional recruiter
- The AI evaluates candidate resumes against a specific job description (Accountant with Procurement Responsibilities, Brooklyn, NY)
- The AI identifies inconsistencies, suspicious gaps, and inaccuracies in resumes
- The AI rates each candidate on a 10-point scale and recommends interview questions

## The three candidates

Three fictional resumes were created specifically to test the AI's analytical ability:

| Candidate | Background | Hidden challenge |
|-----------|------------|-----------------|
| Jean-Paul Bonhomme | Immigrant from Haiti | Two factual inaccuracies in the resume |
| Amanda Williams | American candidate | A suspicious gap in employment history concealing a past incident |
| Oleh Kovalenko | Ukrainian professional with international experience | Resume contained traces suggesting AI assistance |

## Results

The AI successfully identified inaccuracies in the first candidate's resume. For the second candidate, it initially missed the suspicious employment gap — after additional prompting it learned to flag such patterns. It also flagged the third candidate's resume as potentially AI-generated based on stylistic signals.

## Project files

| File | Description |
|------|-------------|
| `Project1.odt` | Full project description and observations |
| `Accountant with Procurement Responsibilities.pdf` | Job description used for evaluation |
| `Jean-Paul Bonhomme.pdf` | Candidate 1 resume |
| `Amanda Williams.pdf` | Candidate 2 resume |
| `Oleh Kovalenko.pdf` | Candidate 3 resume |

## Live project

- [Google AI Studio prompt](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221Cp7f4hcf_kVBmyUY0C9xhqHIbLnoqj8L%22%5D,%22action%22:%22open%22,%22userId%22:%22102054991704663471172%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
- [Dialogue part 1](https://drive.google.com/file/d/11p6bzd_nP3vnLwWhhI2tygBCxde_yhSL/view?usp=sharing)
- [Dialogue part 2](https://drive.google.com/file/d/16KFes1jc0tnyJRyyHqSF5jmbSZobsXd-/view?usp=sharing)
- [Dialogue part 3](https://drive.google.com/file/d/1DQOMvGDUk-heyozOYv8TEEd6Y8VJBJh5/view?usp=sharing)
- [Dialogue part 4](https://drive.google.com/file/d/1s_GO941dXHUjcNLWrfgmtZx2J9arHJBU/view?usp=sharing)

## Notes

Temperature was set to 0.4 for consistent and analytical responses. This project was completed as part of an AI Essentials course.