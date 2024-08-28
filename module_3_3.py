def print_params(a=1, b='line', c=True):
    print(a, b, c)


print_params()
print_params(a=2)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'line2', False]
values_dict = {'a': 11.15, 'b': 2, 'c': 'Правда'}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [12.15, 'line3']
print_params(*values_list2, 42)
