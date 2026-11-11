
import os
from slack_bolt import App
from brain.prompts_en import SYSTEM_PROMPT, CHAT_PROMPT
import openai

# pip install slack-bolt openai influxdb-client

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
def handle_mention(event, say):
    user_q = event.get("text", "")
    # TODO: Fetch current metrics from InfluxDB
    current_metrics = {"pue": 1.82, "temp": 27.5, "it_power": 3.4, "total": 5.6}
    # Call LLM
    # response = openai.ChatCompletion.create(...)
    reply = f"*RackMind Report*\nPUE: {current_metrics['pue']} | Temp: {current_metrics['temp']}°C\n> Q: {user_q}\n> Analysis: Your rack is normal. PUE slightly high, consider raising setpoint to 77°F to save ~$280/mo."
    say(reply)

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
