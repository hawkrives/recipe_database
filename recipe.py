class Recipe:
    def __init__(self, recipe_name, recipe_notes, ingredients_dict, difficulty, cuisine, course, diet, instructions):
        self.recipe_name = recipe_name
        self.recipe_notes = recipe_notes
        self.ingredients_dict = ingredients_dict #keys: ingredient, unit, quantity, prep method
        self.difficulty = difficulty
        self.cuisine = cuisine
        self.course = course
        self.diet = diet
        self.instructions = instructions
        
    #################
    # inserting recipes
    #################

    def insert_cuisine(self, cnn):
        cur = cnn.cursor()

        sql = "INSERT INTO cuisine (cuisine) SELECT (?) WHERE NOT EXISTS (SELECT 1 FROM cuisine WHERE cuisine = ?)"
        values = (self.cuisine, self.cuisine)
        
        cur.execute(sql, values)
        cnn.commit()
        
    def insert_instructions(self, cnn):
        cur = cnn.cursor()

        sql = "INSERT INTO instructions (instructions) VALUES (?)"
        values = (self.instructions,)
        
        cur.execute(sql, values)
        cnn.commit()
        
    def insert_recipe(self, cnn):
        cur = cnn.cursor()

        sql = """INSERT INTO recipe(recipe_name, recipe_notes, 
                    difficulty_id, cuisine_id, course_id, diet_id, instructions_id)
                    VALUES (?, ?, 
                        (SELECT difficulty_id FROM difficulty WHERE difficulty = ?), 
                        (SELECT cuisine_id FROM cuisine WHERE cuisine = ?),
                        (SELECT course_id FROM course WHERE course = ?),
                        (SELECT diet_id FROM diet WHERE diet = ?), 
                        (SELECT instruction_id FROM instructions WHERE instructions = ?))"""
        
        values = (self.recipe_name, self.recipe_notes, self.difficulty, self.cuisine, self.course, self.diet, self.instructions)

        cur.execute(sql, values)
        cnn.commit()
        
    # ingredients_dict is dictionary with keys: ingredient, unit, quantity, prepmethod
    def insert_ingredient_attr(self, attr, cnn):
        cur = cnn.cursor()

        sql = "INSERT INTO {key} ({key}) SELECT (?) WHERE NOT EXISTS (SELECT 1 FROM {key} WHERE {key} = ?)".format(key = attr)
        
        values = []
        for x in self.ingredients_dict[attr]: 
            values.append((x, x))
            
        cur.executemany(sql, values)
        cnn.commit()
        
    def insert_recipe_ingredient(self, cnn):
        cur = cnn.cursor()

        sql = """INSERT INTO recipe_ingredient (recipe_id, ingredient_id, unit_id, quantity_id, prepmethod_id) VALUES
                ((SELECT recipe_id FROM recipe WHERE recipe_name = ?),
                (SELECT ingredient_id FROM ingredient WHERE ingredient = ?),
                (SELECT unit_id FROM unit WHERE unit = ?),
                (SELECT quantity_id FROM quantity WHERE quantity = ?),
                (SELECT prepmethod_id FROM prepmethod WHERE prepmethod = ?))"""
        
        count = 0
        temp = [self.recipe_name]
        values = []
        while count < len(self.ingredients_dict['ingredient']):
            for key in self.ingredients_dict:
                temp.append(self.ingredients_dict[key][count])
            values.append(tuple(temp))
            temp = [self.recipe_name]
            count = count + 1
        
        cur.executemany(sql, values) #values is a list of tuples
        cnn.commit()
        
    def insert_all(self, cnn):
        self.insert_cuisine(cnn)
        self.insert_instructions(cnn)
        self.insert_recipe(cnn)

        for key in self.ingredients_dict:
            self.insert_ingredient_attr(key, cnn)
        
        self.insert_recipe_ingredient(cnn)
