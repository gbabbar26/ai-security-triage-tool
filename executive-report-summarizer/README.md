## What is this?

A Python-based AI tool that automatically generates professional weekly executive security reports for leadership — CEO, CISO, and other non-technical stakeholders. It ingests a week's worth of incident data and produces a structured, business-focused summary including key metrics, business impact assessment, team performance, and strategic recommendations.


# Why did I build this?

As a SOC analyst, writing executive reports is one of the most time-consuming parts of the job. Manually compiling incident data, calculating metrics, and translating technical findings into business language pulls focus away from actual security work. I built this tool to automate that process — so analysts can spend less time writing reports and more time defending systems.

# How it works:


Data Ingestion — Reads weekly incident data from a JSON file, including incident type, priority, status, resolution time, handler, and compliance frameworks referenced
AI Report Generation — Entire week's data is passed to Claude API in one call, which generates a consolidated executive summary — not individual incident reports
Team Performance Section — Automatically identifies which team member handled which incidents for internal visibility
Error Handling — Gracefully handles API failures without crashing
Output — Saves complete report to executive_report.txt with professional formatting ready for leadership distribution

# How to run:
1. Clone the repository
   git clone https://github.com/gbabbar26/executive-report-summarizer.git

2. Install dependencies
   pip install anthropic

3. Set your API key
   Windows: set ANTHROPIC_API_KEY=your-key-here
   Mac/Linux: export ANTHROPIC_API_KEY=your-key-here

4. Add your weekly incident data to weekly_data.json

5. Run the tool
   python3 report_generator.py

6. View your executive report in executive_report.txt

