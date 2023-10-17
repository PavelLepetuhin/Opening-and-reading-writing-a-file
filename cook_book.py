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
    pprint(cook_book)