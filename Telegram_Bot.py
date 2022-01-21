import requests


def bot_info():

    """provide the all imformation about the BOT"""

    try:

        data = requests.get(
            "https://api.telegram.org/bot5007843462:AAHevzlKWR08mKDZPZcUV_fISz1ySO3FkQE/getme"
        )

        print(data.text)  # useing the "text" attirbute for reading the JSON data

    except Exception as system_error:
        print(f"\nplz connect to the internet\n\nsystem error ==>\n\n{system_error}")


def all_converstion():

    """providing every information bot intract with"""

    try:

        data = requests.get(
            "https://api.telegram.org/bot5007843462:AAHevzlKWR08mKDZPZcUV_fISz1ySO3FkQE/getupdates"
        )

        print(data.text)  # useing the "text" attirbute for reading the JSON data

    except Exception as system_error:
        print(f"\nplz connect to the internet\n\nsystem error ==>\n\n{system_error}")

import requests 


def send_messages():
    
    try:

        print("\npost code = 1 ( positive )\n")

        base_URL = "https://api.telegram.org/bot5007843462:AAHevzlKWR08mKDZPZcUV_fISz1ySO3FkQE/sendMessage"

        parameters = {"chat_id": "-1001615360166", "text": ""}

        parameters["text"] = input("Message ? : ")

        data = requests.get(base_URL, data=parameters)

        main = str(data)

        if main == "<Response [200]>" :
    
            print("\nsend successfully")

        else:
            print("\ncannot send")
    
    except Exception as System_error:
        print(f"\nplz connect to the internet\n\nsystem error ==>\n\n{System_error}")


def send_Images():
    
    try:

        print("\npost code = 1 ( positive )\n")

        base_URL = "https://api.telegram.org/bot5007843462:AAHevzlKWR08mKDZPZcUV_fISz1ySO3FkQE/sendPhoto"

        path = str(input("enter the path of IMG: "))

        parameters = {"chat_id": "-1001615360166", "caption":""}

        files = { "photo": path }

        parameters["caption"] = input("write caption: ")

        data = requests.get(base_URL, data=parameters, files=files)

        main = str(data)

        if main == "<Response [200]>" :
    
            print("\nsend successfully")

        else:
            print("\ncannot send")
    
    except Exception as System_error:
        print(f"\nplz connect to the internet\n\nsystem error ==>\n\n{System_error}")


def send_audio():
    
    try:

        print("\npost code = 1 ( positive )\n")

        base_URL = "https://api.telegram.org/bot5007843462:AAHevzlKWR08mKDZPZcUV_fISz1ySO3FkQE/sendAudio"

        path = str(input("enter the path of audio file: "))

        audio_file = open(path, mode='rb')

        parameters = {"chat_id": "-1001615360166", "track":""}

        files = { "audio": audio_file }

        parameters["track"] = input("title of track: ")

        data = requests.get(base_URL, data=parameters, files=files)

        main = str(data)

        if main == "<Response [200]>" :
    
            print("\nsend successfully")

        else:
            print("\ncannot send")
    
    except Exception as System_error:
        print(f"\nplz connect to the internet\n\nsystem error ==>\n\n{System_error}")

send_Images()