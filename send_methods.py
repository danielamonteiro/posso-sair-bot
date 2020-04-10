import tweepy
from dotenv import load_dotenv
import os
import random

class SendMethods:
    def __init__(self):
        load_dotenv()
        self.auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET_KEY"))
        self.auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
        self.api = tweepy.API(self.auth)    

    def post_message(self, message):
        try:
            self.api.update_status(message)
            print("Tweet enviado com sucesso!")
        except Exception as error:
            self.send_methods.send_direct_message(os.getenv("USER_ID"), os.getenv("ERROR_MESSAGE"))
            print("Erro ao enviar Tweet:", error)

    def send_direct_message(self, user, message):
        try:
            self.api.send_direct_message(recipient_id = user, text = message)
            print("Mensagem enviada com sucesso!")
        except Exception as error:
            print("Erro ao enviar mensagem:", error)

    def post_image(self, image):
        try:
            self.api.update_with_media(filename=image)
            print("Mídia enviada com sucesso!")
        except Exception as error:
            self.send_methods.send_direct_message(os.getenv("USER_ID"), os.getenv("ERROR_MESSAGE"))
            print("Erro ao enviar mídia:", error)
