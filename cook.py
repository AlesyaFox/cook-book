recipes = {}

with open('recepts.txt', encoding='utf-8') as file:
    lines = file.readlines()
    step = 3
    i = 0
    while i < len(lines):
        recipe_name = lines[i].strip()
        n_ingredients = int(lines[i + 1].strip())
        ingredients = {}
        for j in range(n_ingredients):
            ing = lines[i + 2 + j].strip().split(' | ')
            name = ing[0]
            amount = float(ing[1])
            measure = ing[2]
            ingredients[name] = {'measure': measure, 'quantity': amount}
        recipes[recipe_name] = {'ingredients': ingredients}
        i += n_ingredients + step



def get_shop_list_by_dishes():

    dish_names = input("Введите список блюд через запятую: ").split(",")

    person_count = int(input("Введите количество гостей: "))

    shopping_list = {}
    for dish_name in dish_names:
        if dish_name in recipes:
            for ingredient in recipes[dish_name]['ingredients']:
                if ingredient not in shopping_list:
                    shopping_list[ingredient] = {'measure': recipes[dish_name]['ingredients'][ingredient]['measure'], 'quantity': 0}
                shopping_list[ingredient]['quantity'] += recipes[dish_name]['ingredients'][ingredient]['quantity'] * person_count

    print("Список продуктов и количества:")
    for item in shopping_list:
        print(item, shopping_list[item]['quantity'], shopping_list[item]['measure'])

get_shop_list_by_dishes()


import os

# список имен файлов
files = ["1.txt", "2.txt", "3.txt"]

# словарь для хранения содержимого и количество строк в каждом файле
file_contents = {}

# прочитать содержимое и количество строк в каждом файле
for file in files:
    with open(file, "r") as f:
        content = f.read()
        lines = content.count("\n") + 1
        file_contents[file] = {"content": content, "lines": lines}

# отсортировать файлы по количеству строк
sorted_files = sorted(files, key=lambda x: file_contents[x]["lines"])

# записать содержимое файлов в результирующий файл с указанием имени файла и количества строк
with open("result.txt", "w") as f:
    for file in sorted_files:
        content = file_contents[file]["content"]
        lines = file_contents[file]["lines"]
        f.write(file + "\n" + str(lines) + "\n" + content + "\n")