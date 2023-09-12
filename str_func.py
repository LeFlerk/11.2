def scream():
    user_text = str(input("Введите текст: "))
    shout = str.upper(user_text)
    return shout

def title():
    """
    Делает заглавными первые буквы каждого слова в строке
    """
    user_text = str(input("Введите текст: "))
    title_text = str.title(user_text)
    return title_text

