calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    string_print = (len(string), string.upper(), string.lower())
    print(string_print)
    count_calls()


def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    list_to_search_up = [s.upper() for s in list_to_search]
    if string in list_to_search_up:
        print(True)
    else:
        print(False)


string_info('Alcatel')
string_info('Heroes')
is_contains('Laptop', ['laptip', 'LApTOP', 'laltap'])
is_contains('Modem', ['madem', 'Mdem', 'MIDEM'])
print(calls)