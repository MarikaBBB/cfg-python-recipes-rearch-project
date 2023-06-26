import requests
import csv
import os.path
from tabulate import tabulate

def recipe_search(ingredient):
    app_id = '41c6ae72'
    app_key = '2a81d2423116ca876974f24f5cf9e8af'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key))
    data = result.json()
    return data['hits']


def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    label = []
    url = []
    ingredientlist = []
    kcal = []
    mealType_list = []
    result_to_file = []
    for result in results:
            recipe = result['recipe']
            label.append(recipe['label'])
            url.append(recipe['url'])
            kcal.append(recipe['totalNutrients']['ENERC_KCAL']['quantity'])
            ingredientlist.append(recipe['ingredientLines'])
            mealType_list.append(recipe['mealType'])
            sorted_outcome = sorted(zip(label, url, ingredientlist, kcal, mealType_list), key=lambda x: x[3]) #zip function allows to iterate over multiple iterables and creates a list of tuples with each tuple having elements from all the iterables(i.e. if multi iterables are passed as the parameter).
    mealtype_choice = input('Do you have a choice of meal type? yes/no : ')
    if mealtype_choice == 'yes':
        mealtype_type = input("Select an option from the following: \n breakfast \n brunch \n lunch \n dinner \n: ")
        for i in range(len(sorted_outcome)):
            meal_type = ''.join(sorted_outcome[i][4]) #Slices the list and get the entire sublist at 4th index and joins it to an empty string.
            if mealtype_type in meal_type:
                result_to_file.append(sorted_outcome[i])
    else:
        result_to_file = sorted_outcome
    return result_to_file


def add_recipe_to_file():
    file_exists = os.path.isfile("final_recipe.csv") #os.path.isfile() method in Python is used to check whether the specified path is an existing regular file or not. It returns a boolean value.The os.path module is always the path module suitable for the operating system Python is running on.
    if not file_exists:
        with open('final_recipe.csv', 'w', newline='', encoding='utf-8') as recipe_file:
            c = csv.writer(recipe_file)
            c.writerow(("label", "url", "ingredientlist", "kcal", "mealType"))

    with open('final_recipe.csv', 'a', newline='', encoding='utf-8') as recipe_file:
        c = csv.writer(recipe_file)
        c.writerows(run())


def read_recipe_from_file():
    add_recipe_to_file()
    with open('final_recipe.csv', 'r') as csv_file:
        spreadsheet = csv.reader(csv_file, delimiter=',')
        table = tabulate(spreadsheet, headers="firstrow", tablefmt="github")
    return table

read_recipe_from_file()

ingredient_two = 'yes'
while True:
    ingredient_choice = input('Would you like to search for something else?: yes/no \n')
    if ingredient_choice == ingredient_two:
        final_output = read_recipe_from_file()
    else:
        with open('final_recipe.csv', 'r') as csv_file:
            spreadsheet = csv.reader(csv_file, delimiter=',')
            table = tabulate(spreadsheet, headers="firstrow", tablefmt="github")
        print(table)
        quit()
