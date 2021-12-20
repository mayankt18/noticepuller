from flask import Flask
import threading
import time
from scraper_tools import AllNotices as al
import json


app = Flask(__name__)
baseurl = 'https://nitdgp.ac.in/p/noticesnitd/general-2'


def getNotices():
    while True:
        print('Updating')
        al.AllNotices(baseurl)
        print('Waiting')
        time.sleep(30*60)


thread = threading.Thread(target=getNotices)
thread.daemon = True
thread.start()


@app.route('/')
def give_notices():
    try:
        f = open('response.json')
        data = json.load(f)
    except:
        data = {}
    return json.dumps(data)


if __name__ == '__main__':
    app.run()
