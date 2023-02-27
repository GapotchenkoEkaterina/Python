# Задача 34
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# Пример:

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам

def find_in_text(text: str):
    text = text.split()  
    text_res = []   
    for i in text:   
        text_res.append(list(filter(lambda x: x in 'аеиоуэюя', list(i))))
    res = map(lambda x: len(x) == len(text_res[0]), text_res)
    return all(res)


text_inlet = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if find_in_text(text_inlet):
    print('Парам пам-пам')
else:
    print('Пам парам')