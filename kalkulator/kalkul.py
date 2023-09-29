from summa import sum
from raznost import razn
from proizvedenie import proizv
from chastnoe import chast

def kalkul():
    while True:
        num1 = int(input('введи число'))
        actions = input('введи знак')
        num2 = int(input('введи число'))
        if  actions == '+':
            print(sum(num1, num2))
        if  actions == '-':
            print(razn(num1, num2))
        if  actions == '*':
            print(proizv(num1, num2))
        if  actions == '/':
            print(chast(num1, num2))