import openai
import json
from config import OPENAI_API_KEY

# Correct OpenAI client initialization
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_weekly_summary(team_scrum_data):
    prompt_intro = """
You are an AI assistant summarizing daily scrum updates from team members for the past week. 
Create a concise weekly summary per team member with:
1. ✅ Key accomplishments
2. 📅 Major planned tasks
3. ⛔ Recurring or unresolved blockers
4. ⚠️ Notes (if needed)

Format:
👤 [Name]
✅ Key Work Completed:
- …
📅 Major Plans:
- …
⛔ Blockers or Issues:
- …
⚠️ Notes (Optional):
- …

Here is the input:
"""

    input_data = ""
    for member in team_scrum_data:
        input_data += f"\n👤 {member['name']}\n"
        for update in member["updates"]:
            input_data += f"📆 {update['date']}\n"
            input_data += f"  Yesterday: {update['yesterday']}\n"
            input_data += f"  Today: {update['today']}\n"
            input_data += f"  Blockers: {update['blockers'] or 'None'}\n"

    full_prompt = prompt_intro + input_data

    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content

    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    with open("sample_data.json", "r") as f:
        team_data = json.load(f)

    summary = generate_weekly_summary(team_data)
    print("\n=== WEEKLY SUMMARY ===\n")
    print(summary)