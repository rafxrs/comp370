# Codebook for Reddit Post Typology
## Motivation & Context

This typology categorizes posts from the McGill and Concordia subreddits. Its purpose is to enable consistent human annotation and later automated classification. Following the COMP 370 guidelines, the typology was developed using open coding, consolidation, multiple passes of re-annotation, and refinement. It is designed to be comprehensive, well-defined, and objective-ish.

## Overview of Final Categories

All posts fit into exactly one of the five categories:

1. Academic Coursework & Study Support
2. Administrative, Registration & Institutional Issues
3. Campus Life, Community & General Discussion
4. Jobs, Internships & Opportunities
5. Lost & Found

## Academic Coursework & Study Support
**Definition**: 
Posts involving course content, assignments, exams, study strategies, or academic planning (e.g., major/minor help).

### Inclusion Criteria
- Discussion of specific courses
- Study tips, exam prep, or help with assignments
- Midterm/final-related questions
- Questions about academic pathways
- Course difficulty or recommendation requests
### Exclusion Criteria
- Exclude posts about:
- Registration logistics → Administrative
- Jobs or career development → Jobs
- General campus topics → Campus Life
- Lost items → Lost & Found

### Positive Examples
- “How do you study for BIOL 201 final?”
- “Tips for ENGR 242 Final”
- “Advice on statistics minor courses?”
- “Comp 218?”

### Negative Examples
- “Lost Beats headphones”
- “Where do people print stickers?”
- “Part-time job English speaker?”

### Edge Cases

- Questions about whether to take/drop a course → Academic
- Complaints about MyLab/WebWork:
- If academic (e.g., assignment problems) → Academic
- If technical/system access → Administrative

2. Administrative, Registration & Institutional Issues
### Definition

Posts about university policies, advising, registration procedures, financial aid, institutional logistics, or campus services.

### Inclusion Criteria
- Add/drop courses, S/U, waitlists as policies
- Financial aid, bursaries, tuition
- Academic advising support
- Exam scheduling or format questions
- Services like printing, library access, health services
- Institutional announcements or complaints

### Exclusion Criteria

Exclude posts about:

- Coursework or studying → Academic
- Jobs/internships → Jobs
- General campus life → Campus Life
- Lost items → Lost & Found

### Positive Examples

- “Need to take one more class as an independent student and advisors won’t help me”
- “Exam conflict date?”
- “Late S/U?”
- “ADHD bursaries Quebec government”
- “Where do people print stickers?”

### Negative Examples

- “Tips for BIOL 201 final” → Academic
- “Part-time job English speaker?” → Jobs
- “Lost glasses near Adams/McConnell” → Lost & Found

### Edge Cases

Waitlist posts:
- “Will I get in?” → Administrative
- “Is this course worth it?” → Academic
- Restroom/building complaints:
- Usually → Campus Life

3. Campus Life, Community & General Discussion
### Definition

Posts involving student life, campus navigation, general observations, informal discussions, humor, or campus culture.

### Inclusion Criteria
- Navigation and wayfinding
- Buiding/facility comments
- General observations or opinions
- Community posts or campus culture
- Campus history
- Open-ended questions

### Exclusion Criteria

Exclude posts about:

- Studying or coursework → Academic
- Policies or registration → Administrative
- Jobs → Jobs
- Lost items → Lost & Found

### Positive Examples

- “Where is Concordia?”
- “Burnside basement toilets”
- “A secret route from Leacock to McMed”
- “History between McGill and UVic”
- “Grey nuns”
- “Thoughts? Who tf made this?”

### Negative Examples

- “ENGR 242 final study tips?” → Academic
- “Part-time job for English speaker” → Jobs

### Edge Cases

Transit/strike posts:
- If focused on daily life → Campus Life
- If focused on policy details → Administrative

4. Jobs, Internships & Opportunities
### Definition

Posts involving employment, volunteering, certifications, training sessions, or career development.

### Inclusion Criteria
- Job postings or searches
- Part-time or on-campus work
- Hiring events or job fairs
- Certification/training opportunities
- Career advice
- Technical resources related to work (e.g., GPU rentals for ML)

### Exclusion Criteria

Exclude posts about:
- Courses, studying, or academics → Academic
- Registration/bureaucracy → Administrative
- General campus life → Campus Life
- Lost items → Lost & Found

### Positive Examples

- “Part time job English speaker”
- “Job”
- “Red Cross safety training this weekend”
- “Looking for input from students who rent GPU compute for ML”

### Negative Examples

- “Help choosing a minor” → Academic
- “Lost Beats headphones” → Lost & Found

### Edge Cases

Club announcements → Campus Life unless explicitly career-oriented.

5. Lost & Found
### Definition

Posts about missing or discovered personal items on or near campus.

### Inclusion Criteria
- Lost item reports
- Found item reports
- Attempts to find owners or return belongings
- Posts including location/time of loss

### Exclusion Criteria

Exclude posts about:
- Services or policies → Administrative
- General questions → Campus Life
- Non-literal “lost” statements (“lost motivation”)

### Positive Examples

- “Found a pair of Beats”
- “Lost glasses on rue University near Adams/McConnell”

### Negative Examples

- “Where is Concordia?” → Campus Life
- “Lost motivation for this semester lol” → Academic/General discussion

### Edge Cases

Stolen items → Usually Lost & Found unless involving policy/campus security → Administrative.

# Comprehensiveness Argument

This typology was developed using open coding and iteratively refined. All posts in both subreddits could be placed into one of these five categories without requiring an “Other” bucket. Edge-case rules ensure reproducibility, and the categories are distinct yet broad enough to cover the entire problem space. This results in a comprehensive, well-defined typology suitable for human annotation and later machine learning tasks.