import pytest
import task_3_3
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method, get_reach_unreach


def test_class_created():
    '''Проверяем, что класс создан'''
    check_class_exists(task_3_3, 'User')


def test_methods_created():
    '''
    Проверяем, что у объекта есть переменные:
        _ping, scan
    '''
    user = task_3_3.User('testuser')
    check_attr_or_method(user, attr='username')


def test_username():
    '''Проверяем работу объекта'''
    user = task_3_3.User('testuser')
    assert user.username == 'testuser'

    # test user.username rewrite
    try:
        user.username = 'a'
    except AttributeError:
        pass
    else:
        pytest.fail("Запись переменной username должна быть запрещена")


def test_password_read_and_set(capsys):
    user = task_3_3.User('testuser')
    correct_password = 's1sfsaghjdfsdfsaf'
    try:
        user.password
    except ValueError:
        pass
    else:
        pytest.fail("Пока пользователь не установил пароль, при обращении к переменной должно генерироваться исключение ValueError")
    # Установка правильного пароль и проверка сообщения
    user.password = correct_password
    out, err = capsys.readouterr()
    assert "Пароль установлен" in out, 'Если пароль прошел проверки, должно выводиться сообщение "Пароль установлен"'

