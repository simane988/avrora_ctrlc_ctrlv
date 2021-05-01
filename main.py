import pyautogui
import time
import random
from os import path

en = "qwertyuiop[]asdfghjkl;'zxcvbnm,~./QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?1234567890-=_+~!@#$%^&*()|\\"
ru = 'йцукенгшщзхъфывапролджэячсмитьбюёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
key_bindigs = {'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i',
               'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f',
               'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': '\'', 'я': 'z',
               'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.',
               'ё': '`', 'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U',
               'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Х': '', 'Ъ': '', 'Ф': 'A', 'Ы': 'S', 'В': 'D',
               'А': 'F', 'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L', 'Ж': ':', 'Э': '\"',
               'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B', 'Т': 'N', 'Ь': 'M', 'Б': '<',
               'Ю': '>', 'Ё': '~'}


def main():
    print('SET LANGUAGE ON ENGLISH!!!')
    lang = 'en'
    print('Ready?')
    input()

    print('Writing will start in 5...')
    time.sleep(1)
    print('4...')
    time.sleep(1)
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print('GO!')

    cur_path = path.dirname(path.abspath(__file__))
    with open(path.join(cur_path, 'data.txt'), 'r') as file:

        for tmp_char in file.read():
            if (tmp_char in en) and (lang != 'en'):
                pyautogui.hotkey('win', 'space')
                lang = 'en'
            if (tmp_char in ru) and (lang != 'ru'):
                pyautogui.hotkey('win', 'space')
                lang = 'ru'

            if tmp_char in ru:
                pyautogui.write(key_bindigs[tmp_char])
            else:
                pyautogui.write(tmp_char)
            time.sleep((random.randint(50, 300))/1000)

    print('All work is done!')


if __name__ == '__main__':
    main()
