import json
import requests
import urllib
import os

TELEGRAM_BOT_TOKEN =  os.getenv("TELEGRAM_BOT_TOKEN", "temporary bot token")
URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/"
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID","@pingme_network")

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def send_telegram_notification(text, chat_id=TELEGRAM_CHAT_ID):
    text = urllib.parse.quote_plus(text)
    url = URL + f"sendMessage?text={text}&chat_id={chat_id}"
    get_url(url)