# Program Impact Reporting System
----------------------------
! Why I Built This Project !

I built this project to practice and demonstrate how data can be used to measure the real-world impact of community programs.

Many organizations collect data but struggle to turn it into useful insights. This project simulates a complete data workflow — from raw data generation to clean analysis and reporting — using only Python and open-source tools.

My goal was to keep the project simple, reliable, and easy to understand, while still following professional data practices.
----------------------------
! What This Project Does !

This project follows a simple ETL-style process:

Extract;
- Generate realistic community program participation data

Transform;
- Clean the data
- Remove duplicate records
- Handle missing values safely
- Validate outcome scores

Analyze & Report;
- Calculate key performance metrics
- Generate visual charts
- Print clear summaries that can support decision-making
----------------------------
! Project Structure !
program-impact-reporting-system
├── generate_data.py
├── clean_data.py
├── report.py
├── requirements.txt
├── data/
│ ├── raw_program_data.csv
│ └── clean_program_data.csv
└── reports/
    ├── completion_status_distribution.png
    └── average_outcome_by_category.png
----------------------------
How to Run This Project (Step-by-Step)
1. Install required libraries
Run this once:
pip install -r requirements.txt

2. Generate raw data
This creates fake but realistic program data;
python generate_data.py

3. Clean the data
This removes duplicates, fixes issues, and validates values;
python clean_data.py

4. Generate reports
This analyzes the data and creates charts;
python report.py

After running all steps, the charts will be saved inside the reports/ folder.
----------------------------
Key Outputs

This project produces:
- Total number of participants
- Program completion rate
- Average outcome score per program category
- Visual charts showing:
      - Completion status distribution
      - Average outcome score by category

These outputs help organizations understand what is working well and where improvements may be needed.
----------------------------
! Tools and Technologies Used !
- Python
- pandas
- matplotlib
- CSV files
- Standard Python libraries only

The project runs fully offline and works in Termux (Android).
----------------------------
! Possible Future Improvements !

If I continue developing this project, I would consider:
- Adding time-based analysis (monthly or yearly trends)
- Tracking participant progress across multiple programs
- Exporting reports as PDF files
- Adding automated data quality checks
- Writing unit tests for data validation
- Turning the analysis into a simple command-line dashboard
