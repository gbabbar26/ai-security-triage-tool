import anthropic
import os
import json

try:
	client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
except Exception as e:
	print("API KEY Not found/failed/wrong due to connectivity issues")
	print(f"Error details: {e}")
	exit()

try:
	with open("alert.json","r") as f:
		alerts=json.load(f)
except Exception as e:
	print("File not found")
	print(f"Error details: {e}")
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
	
with open("report.txt", "w", encoding="utf-8") as output_file:
	for item in alerts:
		result=analyse_alert(item)
		if result is None:
			continue
		else:
			output_file.write(result)
			output_file.write("\n\n" + "="*50 + "\n\n")

	