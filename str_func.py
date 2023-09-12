def scream():
    """
    Меняет символы в строке ввода на заглавные
    """
    user_text = str(input("Введите текст: "))
    shout = str.upper(user_text)
    return shout

scream()
