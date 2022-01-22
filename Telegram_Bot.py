import requests


def bot_info():

    """provide the all imformation about the BOT"""

    try:
        print("\npost code = 1 ( positive )\n")

        data = requests.get(
            "https://api.telegram.org/bot5007843462:AAHevzlKWR08mKDZPZcUV_fISz1ySO3FkQE/getme"
        )

        print(f"DATA\n\n{data.text}")  # useing the "text" attirbute for reading the JSON data

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

        path = str(input("enter the URL: "))

        parameters = {"chat_id": "-1001615360166", "caption":"","photo": path }

        parameters["caption"] = input("write caption: ")

        data = requests.get(base_URL, data=parameters)

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

        parameters["track"] = input("\ntitle of track: ")

        data = requests.get(base_URL, data=parameters, files=files)

        main = str(data)

        if main == "<Response [200]>" :
    
            print("\nsend successfully")

        else:
            print("\ncannot send")
    
    except Exception as System_error:
        print(f"\nplz connect to the internet\n\nsystem error ==>\n\n{System_error}")



def send_videos():

    try:

        print("\npost code = 1 ( positive )\n")

        base_URL = "https://api.telegram.org/bot5007843462:AAHevzlKWR08mKDZPZcUV_fISz1ySO3FkQE/sendVideo"

        path = str(input("enter the path of Video file: "))

        Video_file = open(path, mode='rb')

        parameters = {"chat_id": "-1001615360166", "caption":""}

        files = { "video": Video_file }

        parameters["caption"] = input("\ncaption of video: ")

        data = requests.get(base_URL, data=parameters, files=files)

        main = str(data)

        if main == "<Response [200]>" :
    
            print("\nsend successfully")

        else:
            print("\ncannot send")
    
    except Exception as System_error:
        print(f"\nplz connect to the internet\n\nsystem error ==>\n\n{System_error}")



def send_documents():

    try:

        print("\npost code = 1 ( positive )\n")

        base_URL = "https://api.telegram.org/bot5007843462:AAHevzlKWR08mKDZPZcUV_fISz1ySO3FkQE/sendDocument"

        path = str(input("enter the path Document file: "))

        Document_file = open(path, mode='rb')

        parameters = {"chat_id": "-1001615360166", "caption":""}

        files = { "document": Document_file }

        parameters["caption"] = input("\ncaption of Document: ")

        data = requests.get(base_URL, data=parameters, files=files)

        main = str(data)

        if main == "<Response [200]>" :
    
            print("\nsend successfully")

        else:
            print("\ncannot send")
    
    except Exception as System_error:
        print(f"\nplz connect to the internet\n\nsystem error ==>\n\n{System_error}")



def main():

    print("\n\t\t\t\t\twelcome to the Python BOT\n")

    user = input(f"want to see the BOT info press 1:\n\nwant to see the ALL conversion press 2:\n\nFOR sending meassage press 3\n\nFOR sending Images press 4\n\nFOR sending videos press 5\n\nFOR sending Documents press 6\n\nOption :")

    if user == "1":
        bot_info()
        user2 = input("\nDo you want BOT again Y \ N: ")
        if user2 == "Y" and "y":
            main()
        else:
            quit()
   
    else:
        print("\nOut of range PLZ choose again:\n")
        main()
        
        

main()
      


