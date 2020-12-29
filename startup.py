import sqlite3

def create_cnn(file_name):
    # create database file by specifying location
    cnn = sqlite3.connect(file_name)

    return cnn

def create_tables(cnn):
    # initialize cursor object to interact with database
    cur = cnn.cursor()

    # create all necessary tables
    cur.execute("""CREATE TABLE recipe 
                (recipe_id INTEGER PRIMARY KEY NOT NULL, 
                recipe_name TEXT, 
                recipe_notes TEXT,
                difficulty_id INTEGER,
                cuisine_id INTEGER,
                course_id INTEGER,
                diet_id INTEGER,
                instructions_id INTEGER,
                FOREIGN KEY (difficulty_id) REFERENCES difficulty(difficulty_id),
                FOREIGN KEY (cuisine_id) REFERENCES difficulty(cuisine_id),
                FOREIGN KEY (course_id) REFERENCES difficulty(course_id),
                FOREIGN KEY (diet_id) REFERENCES difficulty(diet_id),
                FOREIGN KEY (instructions_id) REFERENCES difficulty(instructions_id))""")

    cur.execute("""CREATE TABLE difficulty
                (difficulty_id INTEGER PRIMARY KEY NOT NULL,
                difficulty TEXT)""")    

    cur.execute("""CREATE TABLE cuisine
                (cuisine_id INTEGER PRIMARY KEY NOT NULL,
                cuisine TEXT)""")

    cur.execute("""CREATE TABLE course
                (course_id INTEGER PRIMARY KEY NOT NULL,
                course TEXT)""")

    cur.execute("""CREATE TABLE diet
                (diet_id INTEGER PRIMARY KEY NOT NULL,
                diet TEXT)""")

    cur.execute("""CREATE TABLE instructions
                (instruction_id INTEGER PRIMARY KEY NOT NULL,
                instructions TEXT)""")

    cur.execute("""CREATE TABLE ingredient
                (ingredient_id INTEGER PRIMARY KEY NOT NULL,
                ingredient TEXT)""")

    cur.execute("""CREATE TABLE unit
                (unit_id INTEGER PRIMARY KEY NOT NULL,
                unit TEXT)""")

    cur.execute("""CREATE TABLE quantity
                (quantity_id INTEGER PRIMARY KEY NOT NULL,
                quantity TEXT)""")

    cur.execute("""CREATE TABLE prepmethod
                (prepmethod_id INTEGER PRIMARY KEY NOT NULL,
                prepmethod TEXT)""")

    cur.execute("""CREATE TABLE recipe_ingredient
                (recipe_id INTEGER,
                ingredient_id INTEGER,
                unit_id INTEGER,
                quantity_id INTEGER,
                prepmethod_id INTEGER,
                FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id),
                FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id),
                FOREIGN KEY (unit_id) REFERENCES unit(unit_id),
                FOREIGN KEY (quantity_id) REFERENCES quantity(quantity_id),
                FOREIGN KEY (prepmethod_id) REFERENCES prepmethod(prepmethod_id))""")

    cnn.commit()

def insert_known_table_values(cnn):
    cur = cnn.cursor()

    cur.execute("""INSERT INTO difficulty (difficulty) VALUES ("easy"), ("average"), ("difficult")""")
    cur.execute("""INSERT INTO course (course) VALUES ("appetizer"), ("main"), ("dessert"), ("drinks"), ("soups / stews")""")
    cur.execute("""INSERT INTO diet (diet) VALUES ("None"), ("vegan"), ("vegetarian"), ("gluten-free")""")

    cnn.commit()
