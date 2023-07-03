# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
 
random_list_1=[]
for i in range(5):
    random_list_1.append(randint(1,20))

random_list_2=[]
for i in range(10):
    random_list_2.append(randint(1,20))

print(random_list_1)
print(random_list_2)

lst1=set(random_list_1)
lst2=set(random_list_2)

u = lst1.intersection(lst2) 
print(sorted(u))

