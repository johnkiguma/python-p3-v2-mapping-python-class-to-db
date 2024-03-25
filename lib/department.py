from __init__ import CURSOR, CONN


# department.py

class Department:
    def __init__(self, name, location):
        # Initialize id attribute to None
        self.id = None 
        self.name = name
        self.location = location

    def save(self):
        # Insert department data into the database and assign the instance an ID
        CURSOR.execute("INSERT INTO departments (name, location) VALUES (?, ?)", (self.name, self.location))
        self.id = CURSOR.lastrowid  
        CONN.commit()

    def update(self):
        
        CURSOR.execute("UPDATE departments SET name = ?, location = ? WHERE id = ?", (self.name, self.location, self.id))
        CONN.commit()
    
     # Delete method to update the department record
    def delete(self):
        
        CURSOR.execute("DELETE FROM departments WHERE id = ?", (self.id,))
        CONN.commit()

    @classmethod
    #create method to instantiate and save a new department in one step
    def create(cls, name, location):
        
        department = cls(name, location)
        department.save()  
        return department

    @staticmethod
        # Method to create the "departments" table if it doesn't exist
    def create_table():
      
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            )
        """)
        CONN.commit()

    @staticmethod
       # Method to drop the "departments" table if it exists
    def drop_table():
        
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        CONN.commit()

