import os
import tweepy
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Autenticação bem-sucedida")
except Exception as e:
    print("Erro na autenticação:", e)

try:
    with open('MENSAGEM.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        recipient_screen_name = data["recipient_screen_name"]
        message_text = data["message_text"]
except Exception as e:
    print("Erro ao carregar a mensagem do arquivo MENSAGEM.json:", e)
    recipient_screen_name = "username_destinatario"
    message_text = "Mensagem padrão: Erro ao carregar mensagem."

try:
    recipient_id = api.get_user(screen_name=recipient_screen_name).id_str
    api.send_direct_message(recipient_id, text=message_text)
    print(f"Mensagem direta enviada para @{recipient_screen_name}: {message_text}")
except tweepy.TweepError as e:
    print(f"Erro ao enviar mensagem direta para @{recipient_screen_name}: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
