import telebot
import random

token = "введите сюда ваш токен"

bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Покормить рыбок", "Полить помидоры", "Покормить кошку", "Помыть машину", "Погладить собаку"]

HELP = """
Прочтите!
/help - напечатать справку по прогпрамме.
/add - добавить задачу в список(название задачи запрашиваем у пользователя).
/show - напечатать все добавленные задачи.
/random - добавить случайную задачу на дату Сегодня"""

tasks = {}

def add_todo(date, task):
    if date in tasks:
        # Дата в словаре есть
        # Добавляем в список задачу
        tasks[date].append(task)
    else:
        # Даты в словаре нет
        # Создаём запись с ключом даты
        # tasks[date] = [task]
        # или так:
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = 'Задача ' + task + ' добавлена на дату ' + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = 'сегодня'
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = 'Задача ' + task + ' добавлена на дату ' + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"

    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

# Постоянно обращается к серверам Телеграм
bot.polling(none_stop=True)
