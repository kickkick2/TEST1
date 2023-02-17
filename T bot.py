import requests
import telepot


def display_message(bot_token, chat_id):
    if str(chat_id) == "5807169448":
        message = "https://www.apple.com/kr/macbook-pro/"
    elif str(chat_id) == "32332":
        message = "b"
    else:
        message = "Invalid ID"

    send_message(bot_token, chat_id, message)

def send_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

# Example usage
bot_token = "6156299516:AAGIVS3hVaqhz9bG9Gm6McfeXSYdF5X5tZM"
chat_id = 5807169448
display_message(bot_token, chat_id)