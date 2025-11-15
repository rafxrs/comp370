# COMP 370 – Data Science (Fall 2025)

This repository contains my work for COMP 370 (Data Science). Each homework walks through a different piece of the data science workflow: from raw data cleaning and annotation, to Unix tooling, scraping, sampling, dashboards, and typology design.

## Homework 1 – Mini Data Science Project (Russian Troll Tweets)

In HW1, I worked with a large tweet dataset released by FiveThirtyEight containing posts from Russian troll accounts during the 2016 U.S. election. The goal was to build a filtered subset of the first 10,000 tweets (English only, no questions), annotate them with a boolean `trump_mention` feature (based on precise word-boundary rules for “Trump”), and then compute the fraction of tweets that mention Trump. The assignment also required diagnosing where double-counting or other errors could creep into the pipeline and documenting that issue in a short README and accompanying TSV result files. 

## Homework 2 – Data Science Process & MLP Transcripts

HW2 connects the abstract “data science process” to hands-on work with My Little Pony transcripts. After mapping earlier homework activities into the first four phases of the process, the main tasks involved collecting all episode transcripts, transforming them into a clean CSV with `episode`, `speaker`, and `content` fields, and then adding an `addressee` annotation using a proxy rule (the next speaker is treated as the addressee). The assignment finishes by manually checking a block of lines to estimate how often this proxy matches human judgment and by documenting common failure modes. 

## Homework 3 – Unix Server & Command-Line Exercises

HW3 focuses on getting comfortable with a cloud-based Unix EC2 instance as both a data science machine and a networked service. Conceptually, it covers why cloud machines are useful for data science, stages of the data science process, and the distinction between data analytics and data science. Technically, the work includes configuring an Apache webserver on a nonstandard port to serve a simple text file and setting up a MariaDB database server (with a specific database and user) that is accessible from the public internet, with the steps documented in markdown. 

## Homework 4 – Unix Commands & My Little Pony Analysis

HW4 uses Unix command-line tools as the primary “data science environment.” The core dataset is the My Little Pony transcript data, and the tasks involve exploring the dataset structure and size using tools like `head`, `grep`, and `csvtool`, identifying at least one surprising or problematic aspect of the data, and then computing how often each main pony (Twilight Sparkle, Rarity, Pinkie Pie, Rainbow Dash, Fluttershy) speaks. The final deliverables include a markdown file describing the exploration commands and findings, plus a CSV summarizing total line counts and percentages of all lines by speaker. 

## Homework 5 – NYC 311 Data Analysis & Dashboard

HW5 pivots to NYC 311 service request data. After trimming the dataset to 2024 incidents, the first step is a Python CLI tool (`borough_complaints.py`) that, given a date range, outputs complaint-type counts by borough in a CSV-style format. Building on that, the homework moves into Jupyter to explore incident volumes over time and culminates in a Bokeh dashboard that visualizes monthly average response times (create-to-close) for all zip codes and for two user-selected zip codes, with interactive dropdowns and performance constraints that encourage pre-aggregation and efficient data handling. 

## Homework 6 – Question Formulation with 311 Data

HW6 stays with the 311 dataset but shifts the emphasis from raw analysis to question formulation and code structure. Conceptual questions cover refactoring and modular design. Technically, the assignment requires iteratively refining stakeholder questions about noise complaints and rodent issues into measurable, data-driven formulations (showing multiple versions of each question), then implementing Python-based visualizations that answer those refined questions. A final step is refactoring the code into a more modular, less redundant form and documenting the question formalizations and plots.

## Homework 7 – Web Scraping Montreal Gazette Trending Stories

HW7 introduces web scraping as a data collection method. The main technical task is to implement `collect_trending.py`, a scraper that finds the current “trending” stories on the Montreal Gazette site by first parsing the news page to discover which articles are trending and then visiting each article page to extract its title, publication date, author, and blurb. The script outputs a JSON array of article objects, and caching is required for both template types to avoid hitting the site excessively. Conceptual questions address “found” vs. “designed” data and why site owners may react differently to scraping versus API usage.

## Homework 8 – Data Sampling with Celebrity Relationships

HW8 is a deep dive into sampling design, using whosdatedwho.com as the data source and a target of 130 celebrities. One script implements a snowball sampling strategy, starting from a seed celebrity and following relationship links outward, while another script implements an alphabet-based sampling approach that walks through letters and grabs the first few names per letter. After collecting both samples via scraping (with careful caching), the assignment compares how these strategies lead to different populations in terms of gender distribution and age, with the analysis documented in a comparison write-up. 

## Homework 9 – Typology Creation from Reddit (/r/mcgill vs /r/concordia)

HW9 walks through the full typology-building workflow using Reddit data from /r/mcgill and /r/concordia. After manually downloading JSON dumps for each subreddit, a script `extract_to_tsv.py` randomly samples posts and writes them to TSV files with a blank “coding” column. The core of the assignment is an open-coding process: proposing initial categories, consolidating them, re-annotating, and iterating until a stable set of 5–8 categories emerges. The final deliverables include the raw JSON files, annotated TSVs, the extraction script, and a detailed codebook describing each category with definitions and examples. 
