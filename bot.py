import random

help  = """help - напечатать справку по программе
add - добавить задачу в список(назавание задачи у пользователя)
show - напечатать все добавленные задачи
show today -  задачи на сегодня
show tommorow - задачи на завтра
show other day - задачи на остальные дни
exit-завершить работу программы
random - добовлять случайную задачу на дату Сегодня"""


RANDOM_TASKS = ['Зписаться на курс в Нетологию','Написать Гвидо письмо','Покормить кошку ','Помыть машину']
tasks = {}

run = True

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print('Задача', task, 'добавлена на дату', date)
    

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(help)
    elif command == 'show':
        date = input('Введите дату для отоброжения списка задач: ')
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
             print('Такой даты нет')
    elif command == 'add':
        date = input('Введите дату выполнения задачи: ')
        task = input('Введите название задачи: ')
        add_todo(date, task)
    elif command == 'random':
        task = random.choice(RANDOM_TASKS)
        add_todo('Сегодня', task)
    elif command == 'exit':
        print('До свидание')
        break
            
    else:
        print('Неизвестная команда ' )
        
    


