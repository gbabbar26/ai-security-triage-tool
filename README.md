# AI Security Alert Triage Tool

A Python-based AI tool that simulates a real SOC environment — automatically ingesting security alerts (the way SIEM tools like Splunk and Microsoft Sentinel would generate them),
and using the Claude API to analyse each alert for severity, likely threat, and recommended actions. Instead of manually scrolling through hundreds of alerts, analysts can instantly 
see which alerts need immediate attention and which are likely false positives.

## What is this?

As a cybersecurity professional with hands-on SOC and network security experience, I wanted to explore how AI could enhance defensive security workflows. Alert fatigue is a real 
problem in SOC environments — analysts often deal with hundreds of alerts daily, making it difficult to prioritise effectively. I built this tool to understand how LLMs like Claude 
can be integrated into security pipelines to assist with triage, reduce manual effort, and improve response time.

## Update v2.0 — Interactive Analyst Interface

The tool now features a fully interactive menu giving analysts complete control over their workflow. Instead of running the script and analysing all alerts every time, analysts can choose exactly what they need:

--Option 1 — Analyse all alerts at once
--Option 2 — Analyse critical and high severity alerts only, filtering out noise
--Option 3 — Analyse a single alert by its unique Alert ID for targeted investigation

All reports are automatically saved as timestamped .txt files — making it easy to identify when a report was generated and maintain a clean audit trail. This reduces unnecessary API calls, saves time, and keeps records organized — exactly how a real SOC environment operates.

## Features

- **Interactive Menu** — Analysts can choose exactly what they need: analyse all alerts, filter by severity, or investigate a specific alert by ID
- **Auto File Detection** — Automatically detects whether alert data is in JSON or CSV format — no manual configuration needed
- **Severity Filtering** — Option to analyse only Critical and High priority alerts, reducing noise
- **Alert ID Search** — Targeted investigation of a single alert by its unique ID
- **Timestamped Reports** — All reports saved with timestamp in filename for clean audit trail and easy identification
- **Summary Report** — Each report ends with a summary: total alerts processed, critical count, high count, medium/low count
- **Error Handling** — Graceful error handling throughout — no crashes, analyst is always informed

## How it works

1. **Auto Detection** — Tool automatically detects alert.json or alerts.csv in the folder
2. **Interactive Menu** — Analyst selects what they need from a clean menu
3. **AI Analysis** — Each alert is sent to Claude API with a SOC analyst prompt
4. **Severity Filtering** — Results filtered based on analyst's choice
5. **Timestamped Report** — Output saved to a uniquely named .txt file
6. **Summary** — Report ends with key metrics for quick overview

## How to run

1. Clone the repository
   git clone https://github.com/gbabbar26/ai-security-triage-tool.git

2. Install dependencies
   pip install anthropic

3. Set your API key
   Windows: set ANTHROPIC_API_KEY=your-key-here
   Mac/Linux: export ANTHROPIC_API_KEY=your-key-here

4. Add your alerts to alert.json or alerts.csv

5. Run the tool
   python3 alert.py

6. View results in generated report file (e.g. report_all_2026-04-01_14-30.txt)
