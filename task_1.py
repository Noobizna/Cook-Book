def my_cook_book(path='recipes.txt'):
    """
    Creates a dictionary with recipes from a file.

    Args:
        path (str): Path to the file with recipes. Defaults to 'recipes.txt'.

    Returns:
        dict: Dictionary where the key is the recipe name and the value is a list of ingredients.
    """
    with open(path, encoding='utf-8') as file:
        cook_book = {}
        for i in file.read().split('\n\n'):
            name, _, *args = i.split('\n')
            lst = []
            for arg in args:
                ingredient_name, quantity, measure = map(
                    lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                lst.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            cook_book[name] = lst
    return cook_book


def view_cook_book():
    """
    Displays the recipes from the cookbook in a readable format.

    Returns:
        None
    """
    for key, value in my_cook_book().items():
        print(f"'{key}':")
        for row in value:
            print(f'    {row},')


def get_shop_list_by_dishes(dishes, person_count):
    """
    Creates a shopping list based on the given dishes and number of people.

    Args:
        dishes (list): List of dishes.
        person_count (int): Number of people.

    Returns:
        dict: Shopping list with the necessary ingredients.
    """
    cook_book = my_cook_book()
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                ing_name = ing['ingredient_name']
                quantity = ing['quantity'] * person_count
                measure = ing['measure']

                if ing_name in shop_list:
                    shop_list[ing_name]['quantity'] += quantity
                else:
                    shop_list[ing_name] = {'measure': measure, 'quantity': quantity}
    return shop_list


def view_shop_list():
    """
    Displays the shopping list for the given dishes.

    Returns:
        None
    """
    for key, value in get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2).items():
        print(f"'{key}': {value}")


view_shop_list()
