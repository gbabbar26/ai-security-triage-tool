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

Option 1 — Analyse all alerts at once
Option 2 — Analyse critical and high severity alerts only, filtering out noise
Option 3 — Analyse a single alert by its unique Alert ID for targeted investigation

All reports are automatically saved as timestamped .txt files — making it easy to identify when a report was generated and maintain a clean audit trail. This reduces unnecessary API calls, saves time, and keeps records organized — exactly how a real SOC environment operates.

## How it works

Alert Ingestion — Reads security alerts from a JSON file, simulating how a SIEM tool like Splunk or Microsoft Sentinel would generate structured alert data
AI Analysis — Each alert is passed to Claude API with a SOC analyst prompt, which returns severity level, likely threat, and recommended immediate actions
Error Handling — If any alert fails to process, the tool logs the error and moves to the next alert — no crashes, no data loss
Report Generation — All analysis is saved to a structured report.txt file for analyst review

## How to run

1. Clone the repository
   git clone https://github.com/gbabbar26/ai-security-triage-tool.git

2. Install dependencies
   pip install anthropic

3. Set your API key
   Windows: set ANTHROPIC_API_KEY=your-key-here
   Mac/Linux: export ANTHROPIC_API_KEY=your-key-here

4. Add your alerts to alerts.json

5. Run the tool
   python3 alert.py

6. View results in report.txt.
