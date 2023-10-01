
from pprint import pprint



def dict_collector(file_path):
    with open(file_path, 'r', encoding='utf 8') as file_work:
        cook_book = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingredient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingredient = file_work.readline().strip().split(' | ')
                for item in ingredient:
                    dish_items['ingredient_name'] = ingredient[0]
                    dish_items['quantity'] = ingredient[1]
                    dish_items['measure'] = ingredient[2]
                list_of_ingredient.append(dish_items)
                recept = {dish_name: list_of_ingredient}
                cook_book.update(recept)
            file_work.readline()

    return cook_book



dict_collector('recept.txt')


def get_shop_list_by_dishes(dishes, persons=int):

    cook_book = dict_collector('recept.txt')
    print('Наше меню:')
    pprint(cook_book)
    print()
    ingredients_list = {}
    try:
        for dish in dishes:
            for item in cook_book[dish]:
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], \
                                                               'quantity': int(item['quantity']) * persons})])
                if ingredients_list.get(item['ingredient_name']):

                    extra_item = (int(ingredients_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))

                    ingredients_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    ingredients_list.update(items_list)
        print(f"Для приготовления этого блюда на {persons} человек нам необходимо купить:")
        pprint(ingredients_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

