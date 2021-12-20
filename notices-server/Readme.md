# Server in Flask for nitdgp notices scraper

The process runs on another thread hence it doesnt affect the normal functioning as a server.

## Setup
```
git clone <repo> --recursive
virtualenv -v env
cd <repo>
pip3 install -r requirements.txt
python3 .
```

## Usage
Feel free to use any appropriate tool to fetch, we shall use curl here

```
curl https://127.0.0.1/notices
```

##### Note: if you get an empty json it just means the first time scraping process has not completed so wait for about 3-4 min