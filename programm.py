def main():
    print('Какую операцию хотите совершить?')
    flag = False
    while flag == False:
        operationType = input('Выберите ваш вариант (ввод/вывод): ')
        if operationType.lower() == 'ввод':
            flag = True
            AddData()
        elif operationType.lower() == 'вывод':
            flag = True
            ShowData()
        else:
            print('Не корректные данные')
    print('Ура вы справились!')
def AddData():
    dataBase = open('DataBase.txt', 'w')
    dataBase.write(input('Введите наименование вакансии: ') + '\n')
    dataBase.write(input('Введите ключевые навыки: ') + '\n')
    dataBase.write(input('Введите описание: ') + '\n')
    dataBase.write(input('Введите зарплату: ') + '\n')
    dataBase.write(input('Введите вид работы (удаленный, смешанный, в офисе): ') + '\n')
    dataBase.close()
def ShowData():
    dataBase = open('DataBase.txt', 'r')
    print('Наименование вакансии:', dataBase.readline())
    print('Ключевые навыки:', dataBase.readline())
    print('Описание:', dataBase.readline())
    print('Зарплата:', dataBase.readline())
    print('Вид работы:', dataBase.readline())
    dataBase.close()
main()
