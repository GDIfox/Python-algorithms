

# O(1)
def avtorizaya_1(users, user_name, user_pass):
    if users.get(user_name):
        if users[user_name]['password'] == user_pass and users[user_name]['activate']:
            return "Привет, доступ предоставлен"
        elif users[user_name]['password'] == user_pass and not users[user_name]['activate']:
            return "Привет, учетная записи не существует. Необходима регистрация"
        elif users[user_name]['password'] != user_pass:
            return "Не корректный пароль"
    else:
        return "Пользователь не найден"

# реализация с О(1) эффективние всвязи с тем что get(user_name)
# хешь таблица, т.к. у нее очень высокая скорость обработки

# O(n)
def avtorizaya_2(users, user_name, user_pass):
    for key, value in esers.items():
        if key == user_name:
            if value['password'] == user_pass and value['activate']:
                return "Привет, доступ предоставлен"
            elif value['password'] == user_pass and not value['activate']:
                return "Привет, учетная записи не существует. Необходима регистрация"
            elif value['password'] != user_pass:
                return "Не корректный пароль"
    return "Пользователь не найден"

# затраты по времени обработки словаря больше чем поиск по ключу(в первом варианте)