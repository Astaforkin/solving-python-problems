# 1. На easy
# На вход программе подаются два целых числа aaa и bbb. Напишите программу, которая выводит:
#     сумму чисел aaa и bbb;
#     разность чисел aaa и bbb;
#     произведение чисел aaa и bbb;
#     частное чисел aaa и bbb;
#     целую часть от деления числа aaa на bbb;
#     остаток от деления числа aaa на bbb;
#     корень квадратный из суммы их 101010-х степеней: a10+b10\sqrt{a^{10} + b^{10}}a10+b10
# Формат входных данных
# На вход программе подаются два целых числа aaa и b (b≠0)b \, (b \neq 0)b(b=0), каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести результаты математических операций в соответствии с условием задачи.

def task1():
    a, b = int(input()), int(input())
    print(a + b, a - b, a * b, a / b, a // b, a % b, (a**10 + b**10)**0.5, sep='\n')


#2. Индекс массы тела
# Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека. ИМТ показывает весит человек больше или меньше нормы для своего роста. ИМТ человека рассчитывают по формуле:
# ИМТ=масса  (кг)рост(м)×рост(м)ИМТ = \dfrac{масса \, (кг)}{рост(м) \times рост(м)}ИМТ=рост(м)×рост(м)масса (кг)​,
# где масса измеряется в килограммах, а рост — в метрах.
# Масса человека считается оптимальной, если его ИМТ находится между 18.518.518.5 и 252525. Если ИМТ меньше 18.518.518.5, то считается, что человек весит ниже нормы. Если значение ИМТ больше 252525, то считается, что человек весит больше нормы.
# Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.518.518.5 и 252525 (включительно). "Недостаточная масса", если ИМТ меньше 18.518.518.5 и "Избыточная масса", если значение ИМТ больше 252525.
# Формат входных данных
# На вход программе подается два числа: масса и рост человека, каждое на отдельной строке. Все входные числа являются вещественными, используйте для них тип данных float.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
def task2():
    imt = float(input())/float(input())**2
    print(('Оптимальная', 'Избыточная', 'Недостаточная')[(imt>25)-(imt<18.5)], 'масса')

#3. Стоимость строки
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 606060 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести стоимость строки.
def task3():
    price = len(input()) * 60
    print(f'{price // 100}р. {price % 100}коп.')

#4. Количество слов
# Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает количество слов в этой строке.
# Формат входных данных
# На вход программе подается строка.
# Формат выходных данных
# Программа должна вывести количество слов в строке.
# Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).
# Примечание 2. Решите задачу в одну строчку кода 😎.
def task4():
    print(len(input().split()))

#5. Зодиак
# Китайский гороскоп назначает животным годы в 121212-летнем цикле. Один 121212-летний цикл показан в таблице ниже. Таким образом, 201220122012 год будет очередным годом дракона.
# Напишите программу, которая считывает год и отображает название связанного с ним животного. Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.
def task5():
    print(("Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца")[int(input())%12])

#6. Переворот числа
# Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
# Формат входных данных
# На вход программе подается одно натуральное пятизначное или шестизначное число.
# Формат выходных данных
# Программа должна вывести число, которое получится в результате разворота, указанного в условии задачи. Число нужно выводить без незначащих нулей.
def task6():
    num = input()
    print(int(num[:-5] + num[-5:][::-1]))


#7. Standard American Convention
# На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.
# Формат входных данных
# На вход программе подаётся натуральное число n, (0<n<10100)n, \, (0 < n < 10^{100})n,(0<n<10100).
# Формат выходных данных
# Программа должна вывести число с запятыми в соответствии с условием задачи.
def task7():
    num = input()
    for i in range(len(num) - 3, 0, -3):
        num = num[:i]+','+ num[i:]
    print(num)


#8. Задача Иосифа Флавия 🌶️🌶️
# nnn человек, пронумерованных числами от 111 до nnn, стоят в кругу. Они начинают считаться, каждый kkk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.
# Формат входных данных
# На вход программе подаются два числа nnn и kkk, записанные на отдельных строках.
# Формат выходных данных
# Программа должна вывести одно число – номер человека, который останется в кругу последним.




if __name__ == "__main__":
    task7()