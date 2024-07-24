#!/usr/bin/env python3.12

telegram_token = config.TELEGRAM_TOKEN
telegram_chat_id = config.TELEGRAM_CHAT_ID
telegram_base_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat_id}"
# parse_mode=markdown
# parse_mode=html (default)

def send_telegram_message(telegram_text):
    telegram_url = f"{telegram_base_url}&text={telegram_text}"
    telegram_response = requests.get(telegram_url)
    print(telegram_response)


def main():

    hostname = 'x'
    telegram_message = f"Host {hostname} is up!"
    send_telegram_message(telegram_message)


if __name__ == "__main__":
    main()
