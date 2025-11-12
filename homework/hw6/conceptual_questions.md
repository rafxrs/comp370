
# 1.	What is refactoring? Give three examples of refactoring techniques.
    Refactoring is the process of rewriting exisiting code without changing its functionality.
    This can be done through:
    1. modularization: make the code more modular by writing classes, reusable functions etc
    2. cleaning: make the code cleaner -> easier to read, interpret, and thus debug. e.g. by removing redudant code
    3. optimization: make the code do the same thing but faster. this can be done by using a different approach or alogrithm

# 2.	In a data science project, why does code naturally go through “phases” of messiness?
    As we work through our project, we go through phases of exploration and analysis, and often so this happens in multiple "rounds". 
    we start writing code by exploring our data and doing preliminar steps, then we analyze/optimize, and we find that we have to do something else, or new, or that
    we need to slightly (or not) rewrite some of our code to be a bit more precise or get closer to what we want. All these steps involve writing new code or rewriting / adding to existing code, which can make our code base messy very fast.
# 3.	What are three techniques for creating more modular code?
    1. Write functions with clear purposes: don't let them do too many different things or be too many lines long.
    2. Think OOP: classes are a great way of creating modular code
    3. Avoid redundancy: try to limit copy pasting code as much as possible and make code that is very similar into 1 function or class of functions
