import os
from os.path import isfile, join
from dotenv import load_dotenv
import random

from send_methods import SendMethods

class GetMessagesMethods:
    def __init__(self):
        load_dotenv()
        self.send_methods = SendMethods()


    def get_message_to_send(self):
        try:
            messages_to_send_file = open("responses/responses_to_send.txt")
            sent_messages_file = open("responses/sent_responses.txt", "r+")
            messages_to_send_file = messages_to_send_file.readlines()
            sent_messages = sent_messages_file.readlines()
            messages_list = []
            for line in messages_to_send_file:
                if line not in sent_messages:
                    messages_list.append(line)
                    
            if messages_list:
                if len(messages_list) == 1:
                    self.send_methods.send_direct_message(os.getenv("USER_ID"), os.getenv("LAST_MESSAGE_SENT"))
                message_to_send = random.choice(messages_list)
                sent_messages_file.write(message_to_send)
                
                print("Mensagem escolhida para ser enviada:", message_to_send)
                return message_to_send
        except Exception as error:
            self.send_methods.send_direct_message(os.getenv("USER_ID"), os.getenv("ERROR_MESSAGE"))
            print("Erro ao escolher mensagem para ser enviada:", error)
        
    
    def get_media_to_send(self):
        try:
            medias_to_send = [media for media in os.listdir("images/send/")]
            if medias_to_send:
                if len(medias_to_send) == 1:
                    self.send_methods.send_direct_message(os.getenv("USER_ID"), os.getenv("LAST_MEDIA_SENT"))
                chosen_media = random.choice(medias_to_send)
                os.replace(f"images/send/{chosen_media}", f"images/sent/{chosen_media}")
                print("Mídia escolhida para ser enviada:", chosen_media)
                return f"images/sent/{chosen_media}"
        except Exception as error:
            self.send_methods.send_direct_message(os.getenv("USER_ID"), os.getenv("ERROR_MESSAGE"))
            print("Erro ao escolher mídia para ser enviada:", error)