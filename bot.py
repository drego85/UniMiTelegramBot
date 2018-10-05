#!/usr/bin/python3
import time
import Config
import telepot
import logging
from telepot.loop import MessageLoop

# Inizializzo i LOG
logging.basicConfig(filename="bot.log",
                    format="%(asctime)s - %(funcName)10s():%(lineno)s - %(levelname)s - %(message)s",
                    level=logging.INFO)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text" and chat_type == "private":
        bot.sendMessage(chat_id,
                        "*Bot privato* dedicato alle chat di gruppo degli studenti di SSRI Online, creato da @AndreaDraghetti.",
                        parse_mode="Markdown")
        logging.info("%s: %s" % (content_type, msg["from"]["first_name"]))

    if content_type == "new_chat_member" and chat_id in Config.chatidList:
        if msg["from"]["username"]:
            bot.sendMessage(chat_id,
                            "Benvenuto @%s, ti ricordiamo che questo è il gruppo dedicato agli studenti ONLINE di SSRI. *Ti preghiamo di leggere [questo messaggio](https://t.me/canalessri/86) poichè contiene informazioni importanti e sfrutta la ricerca prima di fare delle domande*. Grazie 😉" %
                            msg["from"]["username"], parse_mode="Markdown")
            logging.info("%s: %s" % (content_type, msg["from"]["username"]))

        else:
            bot.sendMessage(chat_id,
                            "Benvenuto @%s, ti ricordiamo che questo è il gruppo dedicato agli studenti ONLINE di SSRI. *Ti preghiamo di leggere [questo messaggio](https://t.me/canalessri/86) poichè contiene informazioni importanti e sfrutta la ricerca prima di fare delle domande*. Grazie 😉" %
                            msg["from"]["first_name"], parse_mode="Markdown")
            logging.info("%s: %s" % (content_type, msg["from"]["first_name"]))


try:
    bot = telepot.Bot(Config.tokenbot)
    MessageLoop(bot, handle).run_as_thread()
except Exception as e:
    logging.error(e, exc_info=True)
    pass

while True:
    time.sleep(10)
