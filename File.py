task = "task.txt"

import os.path

inp = ''
def My_Func_Task (inp) :

    while inp.lower() != 'n' :
        userInput = input('Введіть нове завдання: \t')
        with open('task.txt', 'a') as file :
            file.write(userInput)
            file.close()

        inp = input('Бажаєте продовжити? Y/N \t')
        if inp.lower() != 'y' and inp.lower() != 'n':
            print('Невірний символ!')

def My_Task () :
    if os.path.exists(task) :
        with open(task, 'r') as file :
            print(file.read())
            file.close()

def My_Func_Task_Delete () :
    if os.path.exists(task):
        os.remove(task)

def  My_Func_Made () :
    if not os.path.exists(task) :
        with open('task.txt', 'w') as file:
            file.close()

def MyFunk (inp) :
    while inp.lower() != 'n':
        print('Записати завдання в файл символ 1.')
        print('Подивитися записані завдання символ 2.')
        print('Видалити файл символ 3.')
        print('Створити файл символ 4.')

        userIn = int(input('Задайте, що треба зробити: \t'))

        if userIn == 1 :
            My_Func_Task(inp)
        elif userIn == 2 :
            My_Task()
        elif userIn == 3 :
            My_Func_Task_Delete()
        elif userIn == 4 :
            My_Func_Made()
        else:
            print('Невірно заданий символ! \n')

        inp = input('Бажаєте продовжити? Y/N \t')
        if inp.lower() != 'y' and inp.lower() != 'n':
            print('Невірний символ!')

MyFunk(inp)





