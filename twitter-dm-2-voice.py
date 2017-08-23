import time, os, json, oauth2 as oauth, datetime, pyttsx3
from gtts import gTTS


def test_internet_connection():

    if os.system("ping -n 1 8.8.8.8") != 0:
        print("cannot connect to the internet. Exiting application")
        exit(1)

def authenticate_to_twitter():
    client = oauth.Client(consumer, access_token)

def get_latest_direct_message():
    #https://dev.twitter.com/rest/public

    direct_messages = "https://api.twitter.com/1.1/direct_messages.json?count=1"
    response, data = client.request(direct_messages)

    dm_data = json.loads(data)
    for dm in dm_data:
        latest_msg_id = (dm['id_str'])
        latest_msg_text =(dm['text'])
    return(latest_msg_id, latest_msg_text)

def check_and_update_id_file(latest_msg_id):
    with open(file_path + db_file, 'w') as fw:
        ts = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        fw.write(ts + "," + latest_msg_id)
        fw.close()

def read_twitter_text(t):
    engine = pyttsx3.init()
    engine.say(t)
    engine.runAndWait()

consumer_key = "dsOoDjc25nIYmKkzwJWIwCIuA"
consumer_secret = "NzOvUQGBu48tWJIWU0cIPtY60gbXPtwvpeeXaCLY25DM2oLtd3"
access_key = "11989332-hr3e3a83lnUuTrk854XpQVCzts3gw8k9ZAH0N6bdZ"
access_secret = "KvA6nRnhnJF3zyExwULlwGuEvyY7eUeTL2a5qdaEGRV5O"

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth.Token(key=access_key, secret=access_secret)
client = oauth.Client(consumer, access_token)

file_path = "/tmp/"
db_file = "twitter_msg_id.db"

test_internet_connection()

authenticate_to_twitter()

latest_msg_id, latest_msg_text = get_latest_direct_message()

check_and_update_id_file(latest_msg_id)

read_twitter_text(latest_msg_text)
