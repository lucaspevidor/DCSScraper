import requests
import colorama
from dotenv import load_dotenv
import os

def SendNotification(contents:str, tags='', priority='default', actions='', markdown=True, title=''):
    # Sends notification to url / topic with contents, and uses basic http auth
    # to authenticate
    load_dotenv()
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    url = os.environ.get('SERVER_URL')
    topic = os.environ.get('TOPIC')

    auth = (username, password)
    headers = {
        'Title': title,
        'Priority': priority,
        'Tags': tags,
        "Actions": actions,
        "Markdown": "yes" if markdown else "no"
    }
    data = contents.encode(encoding="utf-8")

    try:
        response = requests.post(url + topic, data=data, headers=headers, auth=auth)
        
        #if response.text contains "topic" then it was successful, else it was not.
        if response.text.find("topic") == -1:
            print(f"{colorama.Fore.RED}Error sending notification: {response.text}{colorama.Style.RESET_ALL}")
            return False
        else:
            print(f"{colorama.Fore.GREEN}Notification sent!{colorama.Style.RESET_ALL}")
            return True
    
    except Exception as e:
        print(f"{colorama.Fore.RED}Error sending notification: {e}{colorama.Style.RESET_ALL}")
        return False