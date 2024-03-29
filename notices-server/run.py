from flask import Flask, send_from_directory
import threading
import time
from scraper_tools import AllNotices as al
import json
from decouple import config


app = Flask(__name__)
baseurl = "https://nitdgp.ac.in/p/noticesnitd/general-2"


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
        return send_from_directory('responses', 'response.json')
    except:
        data = {}
        return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")