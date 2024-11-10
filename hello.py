# my_package/__init__.py
def hello(name):
    """
    Возвращает приветствие с именем.

    Args:
        name (str): Имя, которое нужно использовать в приветствии.

    Returns:
        str: Приветствие.
    """
    return f"Привет, {name}!"

def goodbye(name):
    """
    Прощается с пользователем.

    Args:
        name (str): Имя, которое нужно использовать в прощании.

    Returns:
        str: Прощание.
    """
    return f"До свидания, {name}!"
