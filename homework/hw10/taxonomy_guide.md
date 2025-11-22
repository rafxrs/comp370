# Taxonomy Guide for Reddit Post Annotation  
COMP 370 – Homework 10  
Rafael Reis

## 1. Motivation

The goal of this taxonomy is to provide a consistent and reliable way to annotate the main topics discussed on the /r/mcgill and /r/concordia subreddits.  
These subreddits contain a wide variety of student-generated posts: academic questions, campus life discussions, administrative issues, lost-and-found posts, and more.
This guide defines each category, provides examples, and describes edge cases to reduce ambiguity.

## 2. Taxonomy Categories

Below are the **six final categories** used for annotation.

### **1. Academics & Coursework**

**Definition:**  
Posts primarily about courses, exams, assignments, studying, professors, tutoring, or academic performance.

**Examples (IN):**
- “How do you study for COMP 232 final?”
- “PHIL 210 Quiz 3”
- “Course recommendations for next semester?”
- “COMP 335 tutor needed”
- “Exam conflict rules?”

**Edge Cases:**
- If a post is about switching majors or choosing programs → **Programs, Majors & Academic Pathways**
- If academic stress is the main focus (not the exam itself) → **Well-being & Personal Issues**

### **2. Programs, Majors & Academic Pathways**

**Definition:**  
Posts related to choosing programs, switching majors, admission questions, transfers, or navigating degree requirements.

**Examples (IN):**
- “Transferring from Arts to Education?”
- “New admits to Psych program”
- “BA in Economics—worth it?”
- “How hard is it to transfer from Concordia to McGill?”

**Edge Cases:**
- If the post is about specific course content (e.g., math 204 difficulty) → **Academics & Coursework**
- If the post is about job prospects for a major → **Career, Co-op & Post-Grad**

### **3. Career, Co-op & Post-Grad**

**Definition:**  
Posts involving jobs, internships, co-op programs, CVs, certifications, and questions about post-graduation outcomes.

**Examples (IN):**
- “Working as a front desk attendant at the gym”
- “ACCO GPA requirement for CPA?”
- “Salary after grad?”
- “Is it OK to apply for multiple grad programs?”
- “CV for grad school applications”

**Edge Cases:**
- Posts about course requirements for a major → **Programs, Majors & Academic Pathways**
- Posts about the academic logistics of grad school (credits, prereqs) → **Programs, Majors & Academic Pathways**

### **4. Campus Life & Facilities**

**Definition:**  
Posts about life on campus, study spaces, buildings, events, social happenings, problems in facilities, campus news, Wi-Fi, and day-to-day student experience.

**Examples (IN):**
- “Anyone know what happened in Strathcona?”
- “Study spots near JMSB?”
- “Wicked theme at the bar tonight”
- “Wifi issues today?”
- “Stealing at the library??”
- “PSA to all bathroom users”

**Edge Cases:**
- Lost items → **Lost & Found / Classifieds**
- Mental-health related locations (“place to cry”) → **Well-being & Personal Issues**

### **5. Well-being & Personal Issues**

**Definition:**  
Posts involving physical or mental health, stress, burnout, emotional struggles, or personal well-being.

**Examples (IN):**
- “Final exam stress”
- “Good places to nap and cry?”
- “Colonoscopy”
- “Feeling overwhelmed by deadlines”

**Edge Cases:**
- Academic stress about a specific assignment or exam → **Academics & Coursework**
- Housing or roommate stress (if it existed in dataset) would go under housing-related categories (not present here)

### **6. Lost & Found / Classifieds**

**Definition:**  
Posts about lost items, found items, personal listings, giveaways, or adoption posts.

**Examples (IN):**
- “Found a USB-C charger at JMSB”
- “Lost ring near Burnside”
- “Cat for adoption”
- “Selling old textbooks” (if present)

**Edge Cases:**
- Posts about campus theft → **Campus Life & Facilities**
- Posts about pets causing emotional issues → **Well-being & Personal Issues**

## 3. Annotation Instructions

- Assign **exactly one** category per post  
- Base the label on the **main topic** of the title  
- When unclear, choose the category that best reflects the **primary intent**  
- Use “Miscellaneous / Other” only when no reasonable categ
