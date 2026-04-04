import anthropic
import os
import json
from datetime import datetime 
import csv


timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M")

try:
	client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
except Exception as e:
	print("API KEY Not found/failed/wrong due to connectivity issues")
	print(f"Error details: {e}")
	exit()

if os.path.exists("alert.json"):
	try:
	
		with open("alert.json","r") as f:
			alerts=json.load(f)
	except Exception as e:
		print("JSON File not found")
		print(f"Error details: {e}")
		exit()

elif os.path.exists("alert.csv"):
	try:
	
		with open("alert.csv","r") as f:
			reader=csv.DictReader(f)
			alerts=list(reader)
	except Exception as e:
		print("CSV File not found")
		print(f"Error details: {e}")
		exit()

else:
	print("No file found!")
	exit()


def analyse_alert(alert): 
	try:
		prompt = "You are a SOC analyst. Analyse this security alert and tell me: how serious is it, what is likely happening, and what should be done immediately in a sequence. \n\n" + json.dumps(alert, indent=2)
		message = client.messages.create(
    		model="claude-sonnet-4-20250514",
    		max_tokens=1024,
    		messages=[
        		{"role": "user", "content": prompt}
    		]
		)
		return message.content[0].text
	except Exception as e:
		print(f"Error Details: {e}")
		print("This alert failed to analysed, moving onto next. Check Manually")
		return None


while True:
	print("="*50+"\n")
	print("\tWelcome to AI Alert Triage Tool\n")
	print("="*50+"\n")
	print("1. Analyse all alerts.\n")
	print("2. Analyse critical/high alerts only.\n")
	print("3. Analyse single alert by ID.\n")
	print("4. Exit\n")
	
	choice=input("Enter Your Choice (1-4) : ")
	
	if (choice=="1"):
		total = 0
		critical_count = 0
		high_count = 0
		medium_low_count = 0

		print("Analysing alerts... please wait.")
		with open(f"report_all_{timestamp}.txt", "w", encoding="utf-8") as output_file:
			for item in alerts:
				result=analyse_alert(item)
				if result is None:
					continue
				else:
					if "CRITICAL" in result:
						critical_count+=1
					if "HIGH" in result:
						high_count+=1
					if "MEDIUM" in result or "LOW" in result:
						medium_low_count+=1
					total+=1
					output_file.write(result)
					output_file.write("\n\n" + "="*50 + "\n\n")				
			output_file.write(f"SUMMARY\n")
			output_file.write(f"Total alerts analysed: {total} | Critical Alerts: {critical_count} | High Risk Alerts: {high_count} | Medium or Low Alert Count: {medium_low_count}")
		print(f"Done! All alerts saved to report_all_{timestamp}.txt!")
		
	
	elif choice=="2":
		total = 0
		critical_count = 0
		high_count = 0
		medium_low_count = 0

		print("Analysing alerts... please wait.")
		with open(f"report_critical_{timestamp}.txt", "w", encoding="utf-8") as output_file:
			for item in alerts:
				result=analyse_alert(item)
				if result is None:
					continue
				elif "CRITICAL" in result or "HIGH" in result:
					if "CRITICAL" in result:
						critical_count+=1
					if "HIGH" in result:
						high_count+=1
					total+=1
					output_file.write(result)
					output_file.write("\n\n" + "="*50 + "\n\n")
			output_file.write(f"SUMMARY\n")
			output_file.write(f"Total alerts analysed: {total} | Critical Alerts: {critical_count} | High Risk Alerts: {high_count}")

		print(f"Done! High/Critical alerts saved to report_critical_{timestamp}.txt!")
	elif choice=="3":
		alert_id=input("Enter Alert ID (in format ALT-001): ")
		print("Analysing alerts... please wait.")
		found=False
		for alert in alerts:
			if alert["alertID"] == alert_id:
				result=analyse_alert(alert)
				found= True
				if result:
					filename=f"report_{alert_id}_{timestamp}.txt"
					with open(filename,"w",encoding="utf-8") as output_file:
						output_file.write(result)
					print(f"Done! Report saved by {filename}")
				
				break
		if not found:
			print("Invalid Alert ID.")
	elif choice=="4":
		break
	else:
		print("\n Wrong number, choose from 1-4. \n")

	
	

	
