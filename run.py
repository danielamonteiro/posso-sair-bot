import time

from get_messages_methods import GetMessagesMethods
from send_methods import SendMethods

def main():
    shipments = 1
    while True:
        if shipments % 2 > 0:
            message = GetMessagesMethods().get_message_to_send()
            if message:
                SendMethods().post_message(message)
                shipments += 1
                time.sleep(86400)
        else:
            media = GetMessagesMethods().get_media_to_send()
            if media:
                SendMethods().post_image(media)
                shipments += 1
                time.sleep(86400)
            

if __name__ == "__main__":
    main()
