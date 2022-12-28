import json
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

"""
Парсер
Задача 1: Парсим сайт находим ссылками на другие сайиты 
Задача 2: Преходим на другой ссайт по полученой ссылке и собираем там все имеющиеся ссылки 
Задача 3: Вывести результат на экран и сохранить
"""

def deep_parser(urls):
    # Парсер заходит на первичного сайта забирает данные
    url_deep = urls[0]
    html = requests.get(url_deep).text
    soup = bs(html,'html.parser')
    web_deep_href = soup.find("div", class_='swiper-wrapper').find_all('a')


    list_deep_href = []
    # Выбираем данные ссылками и добавляем в словарь
    for deep in web_deep_href:
        href_deep = deep.get('href')
        list_deep_href.append(href_deep)

    # Вывести на результат на экран
    result = {
        "first_href_pars": urls[0:4],
        "deep_parser": {
            'deep_href_parser': list_deep_href
        }
    }

    print(json.dumps(result, indent=2))

    # Сахранить результат в таблицу
    data = {'price': result}
    df_filled = pd.DataFrame(data)
    # Сохраняем наш DataFrame в NewTable.xls
    writer = pd.ExcelWriter('Table.xlsx')
    df_filled.to_excel(writer)
    writer.save()
    print(f'Данные cохранили в Excel файл Table.xlsx')

def main():
    # Парсер заходит на первичного сайта забирает данные
    url = 'https://www.worldsurfleague.com/'
    html = requests.get(url).text
    soup = bs(html, 'html.parser')  # Исользуя библиотеку bs4 получаем объект "суп", подготовленный для дальнейшей работы
    # Применяем метод find_all , чтобы найти все тэги <a> с классом 'accordeon-inner__item-title', 'link', 'xls'
    web_href = soup.find("div", class_='home-next-hot-drops-item').find_all('a', class_='content-card-title')

    list_href = []
    # Выбираем данные ссылками и добавляем в словарь
    for tbl in web_href:
        href = tbl.get('href')
        list_href.append(href)

    deep_parser(list_href)


if __name__ == '__main__':
    main()