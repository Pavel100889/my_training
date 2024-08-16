my_dict={'Alexey': 1987, 'Andrey': 2001, 'Sergey': 1999, 'Anton': 1995}
print(my_dict)
print(my_dict['Alexey'])
print(my_dict.get('Anna'))
my_dict.update({'Alexandr': 1998, 'Marina': 2002})
delete=my_dict.pop('Andrey')
print(delete)
print(my_dict)

my_set={1,2,3,4,3,2,1,"set",'set',1.101,1.101 }
print(my_set)
my_set.add(5)
my_set.add(1.102)
my_set.discard(1)
print(my_set)