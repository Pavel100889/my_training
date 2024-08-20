print('Введите три числа:')
first=input()
second=input()
third=input()
if first==second==third:
    print('Три числа равны между собой')
elif first==second or first==third or second==third:
    print('Два числа равны между собой')
else: print('Нет равных чисел')