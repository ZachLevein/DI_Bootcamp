import psycopg2


HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Nanach123'
DATABASE = 'menu'

try:
    connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)
except:
    print("Unable to connect with DataBase")

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS menu_items (item_name VARCHAR, item_price VARCHAR);")
connection.commit()



class MenuItem():
    def __init__(self, item, price):
        self.item = item
        self.price = price
        cursor.execute(f"INSERT INTO menu_items VALUES ('{self.item}', '{self.price}')")
    
    def update(self, new_item, new_price):
        self.new_item = new_item
        self.new_price = new_price
        cursor.execute(f" UPDATE menu_items SET item_name = '{self.new_item}', item_price = '{self.new_price}' WHERE item_name = '{self.item}'")
        connection.commit()

    
    def get_by_name(self, name):
        self.name = name
        specific_item = f" SELECT * FROM menu_items WHERE item_name = '{self.name}'"
        result = cursor.execute(specific_item)
        if cursor.fetchall() == []:
            print("Not Available You Absolute Fucking Cunt")
        else: 
            return
    def delete (self):
        cursor.execute(f"DELETE FROM menu_items")
        connection.commit()
    def save (self):
        connection.commit()



item1 = MenuItem('Chorizo', 55)
item1.save()
item1.update('Salami', 12)

item2 = MenuItem("Cheese", 2)
item2.save()
item2.get_by_name('Cheese')



