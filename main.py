import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from telegram import MessageEntity

import youtube_dl

import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text(f'Hi! { update.message.from_user.first_name }\nRun /help for help in commands')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/photo for downloading your profile pic. \n/username to see your username.')


def photo(update, context):
    dp = update.message.from_user.get_profile_photos().photos[0][0]
    fie = dp.get_file().file_path
    update.message.reply_html(f'<a href="{fie}">Click Here</a>')

def ytmp3(update, context):
    urls = []
    url = update.message['text']
    urls.append(url)

    filename = ""

    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(urls, download=True)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)
        filename = video_title + "-" + video_id + ".mp3"
        update.message.reply_audio(open(filename, 'rb'))
    os.remove(filename)

def username(update, context):
    update.message.reply_text(f'Your username is {update.message.from_user.username}')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    updater = Updater("Your_TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("photo", photo))
    dp.add_handler(CommandHandler("username", username))
    dp.add_handler(MessageHandler(Filters.entity(MessageEntity.URL), ytmp3))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()