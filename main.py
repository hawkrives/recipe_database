def main():
    cnn = create_cnn(r"C:\Users\jenni\Documents\sqlite\db\mealpreprecipes3.db")

    with cnn:
        # if first starting out, otherwise remove
#         create_tables(cnn)
#         insert_known_table_values(cnn)
        
        # enter option menu
        ans = get_user_input()
        
        #### If user wants to enter a recipe ####
        if ans == 'enter':        
            recipe_name = get_recipe_name()
            recipe_notes = get_recipe_notes()
            difficulty = get_recipe_difficulty()
            cuisine = get_recipe_cuisine()
            course = get_recipe_course()
            diet = get_recipe_diet()
            ingredients_dict = get_recipe_ingredient()
            instructions = get_recipe_instructions()

            recipe = Recipe(recipe_name, recipe_notes, ingredients_dict, difficulty, cuisine, course, diet, instructions)

            recipe.insert_all(cnn)
        
        #### If user wants to view recipes ####
        if ans == 'view':
            criteria_dict = get_search_criteria()
            recipes_df = print_recipes(cnn, **criteria_dict) 
            
            print(ask_convert(recipes_df))
            
            return recipes_df

if __name__ == '__main__':
     main()
