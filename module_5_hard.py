import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.coming_of_age = False

    def log_in(self, nickname, password):
        hashed_password = hash(password)
        for i in self.users:
            if i.nickname == nickname and i.password == hashed_password:
                self.current_user = i.nickname
                if i.age >= 18:
                    self.coming_of_age = True
                else:
                    self.coming_of_age = False
                return f"Здравсствуйте {nickname}"
        return "Неверно имя пользователя или пароль"

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = nickname
        if age >= 18:
            self.coming_of_age = False
        else:
            self.coming_of_age = True
        print(f"Пользователь {nickname} зарегистрирован.")

    def log_out(self):
        self.current_user = None
        print("Вы вышли.")

    def add(self, *videos):
        for i in videos:
            if not any(v.title == i.title for v in self.videos):
                self.videos.append(i)

    def get_videos(self, keyword):
        result = [video.title for video in self.videos if keyword.lower() in video.title.lower()]
        return f'Найдено: {result}'

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for i in self.videos:
            if i.title == title:
                if i.adult_mode and self.coming_of_age:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                while i.time_now < i.duration:
                    print(i.time_now, end="")
                    time.sleep(1)
                    i.time_now += 1
                print(' Конец видео')
                i.time_now = 0
                return
        print("Видео не существует.")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, 5, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.log_out()
print(ur.current_user)

ur.log_in('vasya_pupkin', 'lolkekcheburek')
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
