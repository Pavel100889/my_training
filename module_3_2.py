def send_email(message, recipient, sender='university.help@gmail.com'):
    condition1 = '@'
    condition2 = '.com'
    condition3 = '.ru'
    condition4 = '.net'
    if condition1 in recipient and condition1 in sender:
        if condition2 in recipient or condition3 in recipient or condition4 in recipient:
            if condition2 in sender or condition3 in sender or condition4 in sender:
                if recipient != sender:
                    if sender == 'university.help@gmail.com':
                        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                    else:
                        print('Нестандартный отправитель')
                else:
                    print('Нельзя отправить письмо самому себе!')
            else:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
send_email('Hello', 'pavel@mail.net')
send_email('Hello', 'pavel@mail.uk')
send_email('Hello', 'pavelmail.com')
send_email('Hello', 'pavel@mail.ru', sender='urban@mail.net')
send_email('Hello', 'university.help@gmail.com')