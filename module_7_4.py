team1_num = int(input('Kоличество участников "Мастера кода": '))
team2_num = int(input('Kоличество участников "Волшебники данных": '))
score_1 = int(input('Kоличество задач решенных "Мастера кода": '))
score_2 = int(input('Kоличество задач решенных "Волшебники данных": '))
team1_time = float(input('"Мастера кода" решили задачи за:'))
team2_time = float(input('"Волшебники данных" решили задачи за:'))

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
ending_1 = str
if team1_num == 1:
    ending_1 = 'к'
elif team1_num > 1 and team1_num < 5:
    ending_1 = 'ка'
else:
    ending_1 = 'ков'

ending_2 = str
if score_2 == 1:
    ending_2 = 'у'
elif score_2 > 1 and score_2 < 5:
    ending_2 = 'и'
else:
    ending_2 = ''

print('В команде Мастера кода %s участни%s' % (team1_num, ending_1))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print('Команда Волшебники данных решила {} задач{}'.format(score_2, ending_2))
print('Волшебники данных решили задачи за {}с'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
