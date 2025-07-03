# Scrum Summary Bot 🤖📝

This bot generates weekly summaries of daily scrum inputs using OpenAI GPT models (e.g., `gpt-4o`).  
Perfect for integrating with Microsoft Teams via Azure Bot Service or Azure Functions.

## 🔧 Setup

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/scrum-summary-bot.git
cd scrum-summary-bot
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Set Your OpenAI API Key
Create a `.env` file or export the key in your terminal:
```bash
export OPENAI_API_KEY=your-key-here
```

### 4. Run the Bot
```bash
python main.py
```

---

## 📦 Project Files

- `main.py` – Core logic to generate summaries
- `config.py` – OpenAI key management
- `sample_data.json` – Dummy scrum inputs for testing

## ✨ Output Example

```
👤 Alice
✅ Key Work Completed:
- Completed login module
- Worked on payment gateway
📅 Major Plans:
- Test and integrate payment gateway
⛔ Blockers or Issues:
- Test environment not ready
⚠️ Notes (Optional):
- May need DevOps support
```

## 📈 Future Plans

- Integrate with Microsoft Teams
- Deploy as Azure Function
- Connect with CosmosDB for live input capture