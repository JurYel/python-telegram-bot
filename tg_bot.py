from telegram import *
from telegram.ext import *
import logging
import time
import multiprocessing

start = time.time()

bot = Bot("5318750378:AAFZ0G7i9UCT5nTOv_-08umKYj9hZ4XPrWw")
print(bot.get_me())

updater = Updater("5318750378:AAFZ0G7i9UCT5nTOv_-08umKYj9hZ4XPrWw", use_context=True)
dispatcher = updater.dispatcher

def test_function(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I can't talk right now, you are gay.",
    )


start_value = None
tokens = ["Hello", "Hi", "Jur"]

for token in tokens:
    start_value = CommandHandler(token, test_function)
    dispatcher.add_handler(start_value)

def time_elapsed(oldtime):
    if time.time() - oldtime > 59:
        exit()
if __name__ == '__main__':
    process1 = multiprocessing.Process(target=time_elapsed(start))
    process2 = multiprocessing.Process(target=updater.start_polling)

    process1.start()
    process2.start()
    end = time.perf_count()
    print(f"Finished in {round(end-start, 2)} second(s)")

