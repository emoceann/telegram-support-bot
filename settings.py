import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

TELEGRAM_SUPPORT_CHAT_ID = os.getenv("TELEGRAM_SUPPORT_CHAT_ID")
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)


WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "Привет)\n🦊TSquad Apps – сервис аренды качественных приложений.\nМы предоставляем Android прилки под разные источники трафика (FB в приоритете).\n🧡В прилках есть как нейминг так и дипка, потери сведены к минимуму.\n❗️Органика закрыта.\n📲Пуши настраиваем мы, сейчас работают пуши трижды в день на большинство ГЕО (по запросу покажем) + пуш через 15 мин после установки.\n💬Также мы следим за рейтингом прилок в сторе и поддерживаем его.\n🔸Делаем гемблинг и беттинг приложения (под заказ можем сделать крипто, дейтинг или обговорить другие вертикали).\n🔸Для удобной работы с нами мы сделали личный кабинет с балансом, статистикой и другими фичами (много чего сейчас в разработке).\n🔸Свой бот для пошарки прил в ФБ и отслеживания банов и меток.\n💳С ценами у нас всё максимально просто:\n🔸первые две недели – $0.05/инстал (в качестве приветственного бонуса),\n🔸дальше фикс для всех – $0.07,\n<span class="tg-spoiler">P.S. если наливаете 25к+ инсталов дейли\n– сможем обсудить другие условия.</span>\n🦊С радостью ответим на любые вопросы.\nЕсли все ок, то для начала интеграции нам нужно только навание команды и напиши, плз, как ты о нас узнал (просто интересно).\nНаш админ увидит твое сообщение, и напишет в ближайшее время⏳")
REPLY_TO_THIS_MESSAGE = os.getenv("REPLY_TO_THIS_MESSAGE", "REPLY_TO_THIS")
WRONG_REPLY = os.getenv("WRONG_REPLY", "WRONG_REPLY")
