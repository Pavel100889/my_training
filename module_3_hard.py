data_structure = [[1,2,3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
def adder(args):
    total = 0
    # Если элемент — список, кортеж или множество,
    if isinstance(args[0], (list, tuple, set)):
        s = args[0]
        for i in s:
            if isinstance(i, (int, float)):
                total += i
            elif isinstance(i, str):
                total += len(i)
            elif isinstance(i, dict):
                for values in i.values():
                    if isinstance(values, (int, float)):
                        total += values
                    elif isinstance((values, str)):
                        total += len(values)
                for key in i.keys():
                    if isinstance(key, (int, float)):
                        total += key
                    elif isinstance(key, str):
                        total += len(key)
            elif isinstance(i, (list, tuple, set)):

                for y in i:
                    if isinstance(y, (int, float)):
                        total += y
                    elif isinstance(y, str):
                        total += len(y)
                    elif isinstance(y, dict):
                        for values in y.values():
                            if isinstance(values, (int, float)):
                                total += values
                            elif isinstance((values, str)):
                                total += len(values)
                        for key in y.keys():
                            if isinstance(key, (int, float)):
                                total += key
                            elif isinstance(key, str):
                                total += len(key)
                    elif isinstance(y, (list, tuple, set)):

                        for g in y:
                            if isinstance(g, (int, float)):
                                total += g
                            elif isinstance(g, str):
                                total += len(g)
                            elif isinstance(g, dict):
                                for values in g.values():
                                    if isinstance(values, (int, float)):
                                        total += values
                                    elif isinstance((values, str)):
                                        total += len(values)
                                for key in g.keys():
                                    if isinstance(key, (int, float)):
                                        total += key
                                    elif isinstance(key, str):
                                        total += len(key)
                            elif isinstance(g, (list, tuple, set)):

                                for m in g:
                                    if isinstance(m, (int, float)):
                                        total += m
                                    elif isinstance(m, str):
                                        total += len(m)
                                    elif isinstance(m, dict):
                                        for values in m.values():
                                            if isinstance(values, (int, float)):
                                                total += values
                                            elif isinstance((values, str)):
                                                total += len(values)
                                        for key in m.keys():
                                            if isinstance(key, (int, float)):
                                                total += key
                                            elif isinstance(key, str):
                                                total += len(key)
                                    elif isinstance(m, (list, tuple, set)):

                                        for l in m:
                                            if isinstance(l, (int, float)):
                                                total += l
                                            elif isinstance(l, str):
                                                total += len(l)
                                            elif isinstance(l, dict):
                                                for values in l.values():
                                                    if isinstance(values, (int, float)):
                                                        total += values
                                                    elif isinstance((values, str)):
                                                        total += len(values)
                                                for key in l.keys():
                                                    if isinstance(key, (int, float)):
                                                        total += key
                                                    elif isinstance(key, str):
                                                        total += len(key)

        if len(args) > 1:
            return total + adder((args[1:]))
        else:
            return total
    # Если элемент — целое число или число с плавающей точкой
    elif isinstance(args[0], (int, float)):
        total = args[0]
        if len(args) > 1:
            return total + adder((args[1:]))
        else:
            return total
    # Если элемент — строка,
    elif isinstance(args[0], str):
        total = len(args[0])
        if len(args) > 1:
            return total + adder((args[1:]))
        else:
            return total
    # Если элемент — словарь
    elif isinstance(args[0], dict):
        for values in args[0].values():
            if isinstance(values, (int, float)):
                total+=values
            elif isinstance((values, str)):
                total+=len(values)
        for key in args[0].keys():
            if isinstance(key, (int, float)):
                total+=key
            elif isinstance(key, str):
                total += len(key)
        if len(args) > 1:
            return total + adder((args[1:]))
        else:
            return total

print(adder(data_structure))
