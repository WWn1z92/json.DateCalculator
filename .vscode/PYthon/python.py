print('калькулятор')
a= float(input('введи число'))
операция = input('выбери (+,-,/,*) ')
b= float(input('введи'))
if операция == '+':
    print(a+b)
elif операция =='-':
    print(a-b)
elif операция =='*':
    print(a*b)
elif операция =='/':
    if b != 0:
        print(a/b)
    else:
        print('0 деление болмайды акен аузын сыгынь')
