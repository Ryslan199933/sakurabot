import telebot
import random
import os

from telebot import TeleBot

bot: TeleBot = telebot.TeleBot('927320879:AAFY41HvWubtj0m7YVyuxO03kY8Yq5MESqs')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('ФОТО', 'ГИФКА')
keyboard1.row('БУДУЩЕЕ')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'ФОТО':
        directory = 'D:\\sakurbot\\files\\photo'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif  message.text == 'БУДУЩЕЕ':
        bot.send_message(message.chat.id, 'Уважаемый пользователь! В будущем обновлении мы'
                                          'бы хотели добавить вкладки "Чат" и "Видео", которые будут'
                                          'содержать отдельные подкатегории. Увы, в связи с политикой'
                                          'мессенджера Telegram, у нас установлено ограничение на'
                                          'отправку видео 25мб. Наша команда трудится над решением'
                                          'данного вопроса и мы нуждаемся в материальной поддержке, а'
                                          'именно в денежных средствах. Вы всегда можете нам помочь.'
                                          'Даже отправив незначительную сумму, Вы мотивируете'
                                          'работать нас дальше!'
                                          'Все выделенные средства пойдут на разработку. Спасибо! вам за пожертвование '
                                          'qivi+79870372086')
    elif message.text == 'ГИФКА':
        directory = 'D:\\sakurbot\\files\\gif'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        gif = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_video(message.from_user.id, gif)
        gif.close()

bot.polling()
