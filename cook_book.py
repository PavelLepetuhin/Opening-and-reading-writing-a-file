from pprint import pprint

cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name_dishes = line.strip()
        recipes = []
        count_of_ingredients = f.readline()
        for i in range(int(count_of_ingredients)):
            count_of_ing = f.readline()
            ingredients, quantity, measure = count_of_ing.strip().split(' | ')
            recipes.append({'ingredient_name': ingredients,
                        'quantity': quantity,
                        'measure': measure})
        dish = {name_dishes: recipes}
        line_2 = f.readline()
        cook_book.update(dish)
    print('cook_book: =')
    pprint(cook_book, width=120)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingredient_name'] in shop_list:
                shop_list[ingridient['ingredient_name']]['quantity'] += int(ingridient['quantity']) * person_count
            else:
                shop_list.update({ingridient['ingredient_name']: {'measure': ingridient['measure'], 'quantity': int(ingridient['quantity']) * person_count}})
    return shop_list

print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))