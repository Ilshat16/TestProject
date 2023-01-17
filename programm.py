# В качестве БД использовал текстовый документ
# С базами данных еще не знаком, но всё еще впереди :)
def main():
    ShowMenu()
    chosenAction = int(input('Введите цифру меню: '))
    while chosenAction != 0:
        if chosenAction == 1:
            AddData()
        elif chosenAction == 2:
            ShowAllEntries()
        elif chosenAction == 3:
            ShowOneEntry()
        elif chosenAction == 4:
            RemoveData()
        else:
            print('Такого пункта в меню нет')
        print()
        print('Если хотите продолжить работу')
        ShowMenu()
        chosenAction = int(input('Введите цифру меню: '))
    print('Программа завершена')
            
def ShowMenu():
    print('Выберите один из предложенных вариантов действия:')
    print('1 - Ввести запись в базу данных')
    print('2 - Вывод всех записей из базы двнных')
    print('3 - Вывод записей по наименоваию вакансии из базы данных')
    print('4 - Стереть все записи из базы данных')
    print('0 - Выход из программы')
def AddData():
    dataBase = open('DataBase.txt', 'a')
    dataBase.write(input('Введите наименование вакансии: ') + '\n')
    dataBase.write(input('Введите ключевые навыки: ') + '\n')
    dataBase.write(input('Введите описание: ') + '\n')
    dataBase.write(input('Введите зарплату: ') + '\n')
    dataBase.write(input('Введите вид работы (удаленный, смешанный, в офисе): ') + '\n')
    dataBase.close()
def ShowAllEntries():
    dataBase = open('DataBase.txt', 'r')
    vacancy = dataBase.readline()
    while vacancy != '':
        skills = dataBase.readline()
        descr = dataBase.readline()
        salary = dataBase.readline()
        workType = dataBase.readline()
        vacancy = vacancy.rstrip('\n')
        skills = skills.rstrip('\n')
        descr = descr.rstrip('\n')
        salary = salary.rstrip('\n')
        workType = workType.rstrip('\n')
        print('Наименование вакансии:', vacancy)
        print('Ключевые навыки:', skills)
        print('Описание:', descr)
        print('Зарплата:', salary)
        print('Вид работы:', workType)
        print()
        vacancy = dataBase.readline()
    dataBase.close()
def ShowOneEntry():
    found = False
    searchVacancy = input('Введите искомое название вакансии: ')
    dataBase = open('DataBase.txt', 'r')
    vacancy = dataBase.readline()
    while vacancy != '':
        skills = dataBase.readline()
        descr = dataBase.readline()
        salary = dataBase.readline()
        workType = dataBase.readline()
        vacancy = vacancy.rstrip('\n')
        skills = skills.rstrip('\n')
        descr = descr.rstrip('\n')
        salary = salary.rstrip('\n')
        workType = workType.rstrip('\n')
        if vacancy == searchVacancy:
            print('Наименование вакансии:', vacancy)
            print('Ключевые навыки:', skills)
            print('Описание:', descr)
            print('Зарплата:', salary)
            print('Вид работы:', workType)
            print()
            found = True
        vacancy = dataBase.readline()
    dataBase.close()
    if not found:
        print('Такой вакансии в базе нет')
def RemoveData():
    dataBase = open('DataBase.txt', 'w')
    dataBase.close()
main()
