import json
import os
from sys import getdefaultencoding

def load_json_file_in_list(json_file):
    list_news = []
    with open(json_file, 'r', encoding=getdefaultencoding()) as news_file:
        new_file_data = json.load(news_file)
        for item_list in new_file_data['rss']['channel']['items']:
            temp_list_news = item_list['description'].split()
            list_news += temp_list_news
            # pprint(item_list['description'])
        return list_news

def frequency_count_word(name_file):
    list_news = load_json_file_in_list(name_file)

    word_count = {}
    for word_item in list_news:
        if len(word_item) >= 6:
            if word_item in word_count.keys():  # помезщаем каждое слово в словарь и считаем их количество
                word_count[word_item] += 1
            else:
                word_count[word_item] = 1

    temp_list = sorted(word_count, key=word_count.get, reverse=True)  # применям сортировку к словарю по значениям
    print('Список наиболее встречающихся слов длиной более 6 символов из файла {}'.format(name_file))
    for i in range(10):
        print('Слово "{}" встречается {}'.format(temp_list[i], word_count[temp_list[i]]))


current_dir = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(current_dir):
    for filename in files:
        if filename.endswith(".json"):
            way_file = os.path.join(current_dir, filename)
            frequency_count_word(way_file)
