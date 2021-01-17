## Py-Telegram-BOT

<img src="https://img.shields.io/badge/Python-100%25-yellow.svg">

This bot sends music file to the user and can send thier usernames and profile image.

#### API LIBRARY USED
I used `Telegram` api and `youtube_dl` library.

#### Setup

```sh
$ git clone https://github.com/aamit2267/Py-Telegram-Bot.git
$ cd ./Py-Telegram-Bot/
$ pip install -r requirements.txt
```
Now,
Enter Your token: (line 64)
```
updater = Updater("Your_TOKEN", use_context=True)
```

#### Test

```sh
$ python main.py
```