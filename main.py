import subprocess
import time
import requests

SIGNAL_CLI_PATH = "/app/signal-cli/bin/signal-cli"
SIGNAL_NUMBER = "+41788510297"  # Votre numéro Signal

def send_message(recipient, message):
    subprocess.run([SIGNAL_CLI_PATH, "-u", SIGNAL_NUMBER, "send", recipient, "-m", message])

def get_lucid_news():
    # Exemple : récupérer les dernières news Lucid Motors depuis une API
    response = requests.get("https://newsapi.org/v2/everything?q=Lucid%20Motors&apiKey=YOUR_NEWSAPI_KEY")
    articles = response.json().get("articles", [])
    news = []
    for a in articles[:3]:  # Prendre les 3 premières
        news.append(f"📰 {a['title']} ({a['source']['name']})\n{a['url']}")
    return "\n\n".join(news)

if __name__ == "__main__":
    while True:
        print("🔄 Checking for Lucid news...")
        news = get_lucid_news()
        if news:
            send_message(SIGNAL_NUMBER, f"🚨 Lucid News Update 🚨\n\n{news}")
        time.sleep(3600)  # Vérifie toutes les heures
