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
	with open("weekly_data.json","r") as f:
		data=json.load(f)
except Exception as e:
	print("File not found")
	print(f"Error details: {e}")
	exit()


def generate_report(data):
	try:
		prompt="You are going to write an executive summary report for CISO, CEO and other non technical stakeholders, in a non-technical language with focus on business impact of the incidents that have occurred in that week along with the key metrics such as how many incidents happened, how many were resolved, how many are pending (or in progress) and so on and any recommendations for the leadership. Include a team performance section showing which team member handled which incidents. " + json.dumps(data, indent=2)

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
		print("This incident failed to summarised, moving onto next. Check Manually")
		return None
result=generate_report(data)
if result is None:
	print("Report Generation failed, check manually!")
else:
	with open("executive_report.txt", "w", encoding="utf-8") as output_file:	
		output_file.write(result)
		print("Report saved to executive_report.txt")
	