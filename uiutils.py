def get_user_input():
    while True:
        answer = input("Do you want to enter or view recipes? Type 'enter' or 'view'. ")
        if answer.lower() not in ('enter', 'view'):
            print("Please type 'enter' or 'view'. ")
            continue
        else:
            break
    return answer.lower()
    
def get_recipe_name():
    recipe_name = input("Enter recipe name: ")
    return recipe_name

def get_recipe_notes():
    recipe_notes = input("Enter recipe notes: ")
    return recipe_notes

def get_recipe_difficulty():
    while True:
        recipe_difficulty = input("Enter recipe difficulty (easy, average, difficult): ")
        if recipe_difficulty not in ('easy', 'average', 'difficult'): 
            print("Please enter a valid difficulty.")
            continue
        else:
            break
    return recipe_difficulty

def get_recipe_cuisine():
    recipe_cuisine = input("Enter recipe cuisine: ")
    return recipe_cuisine

def get_recipe_course():
    while True:
        recipe_course = input("Enter recipe course (appetizer, main, dessert, drinks, soups / stews): ")
        if recipe_course not in ('appetizer', 'main', 'dessert', 'drinks', 'soups / stews'): 
            print("Please enter a valid course.")
            continue
        else:
            break
    return recipe_course

def get_recipe_diet():
    while True:
        recipe_diet = input("Enter recipe diet (None, vegan, vegetarian, gluten-free): ")
        if recipe_diet not in ('None', 'vegan', 'vegetarian', 'gluten-free'): 
            print("Please enter a valid difficulty.")
            continue
        else:
            break
            
    return recipe_diet
        
def get_recipe_ingredient():
    recipe_ingredient_li = []
    recipe_ingredient = {'ingredient': [], 'unit': [], 'quantity': [], 'prepmethod': []}
    while True:
        ingredient = input("""Enter one ingredient at a time with comma separations: ingredient name, unit, quantity, prep method. \nIf attribute does not exist, enter as 'None'. To quit, enter 'q'. """)
        if ingredient == 'q':
            break
        elif len(list(ingredient.split(","))) != 4:
            print("Please enter the four attributes: ingredient name, unit, quantity, and preparation method. Or enter 'q' to quit. ")
            continue
        else:     
            recipe_ingredient_li.append(list(ingredient.split(","))) 
            continue
      
    for entry in recipe_ingredient_li:
        
        recipe_ingredient['ingredient'].append(entry[0].lstrip()) # strip leading white spaces for aesthetic purposes
        recipe_ingredient['unit'].append(entry[1].lstrip())
        recipe_ingredient['quantity'].append(entry[2].lstrip())
        recipe_ingredient['prepmethod'].append(entry[3].lstrip())            
    
    return recipe_ingredient

def get_recipe_instructions():
    recipe_instructions = input("Enter recipe instructions: ")
    return recipe_instructions

def get_search_criteria():
    criteria_li = []
    criteria_dict = {}
    while True:
        criteria = input("Enter each search criteria by [category, value] (e.g. ingredient, fish). Enter 'q' to quit. ")
        if criteria == 'q':
            break
        elif len(list(criteria.split(','))) != 2:
            print("Please enter one category with one value. ")
            continue
        else:
            criteria_li.append(list(criteria.split(',')))
            continue

    for entry in criteria_li:
        criteria_dict[entry[0]] = entry[1]
 
    return criteria_dict
