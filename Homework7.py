import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()


class Human:
    def __init__(self, name, age, height, weight, id):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.id = id

    def insert(self):
        try:
            cursor.execute('INSERT INTO humans VALUES (:name, :age, :height, :weight, :id)',
                           {'name': self.name, 'age': self.age, 'height': self.height, 'weight': self.weight,
                            'id': self.id})
            connection.commit()
        except Exception:
            cursor.execute('CREATE TABLE IF NOT EXISTS human (name TEXT, age INTEGER, height INTEGER, weight INTEGER,'
                           ' id INTEGER)')
            connection.commit()

    def select(self):
        selecting = input('SELECT with (name, age, height, weight, id): ').lower()
        if selecting == 'id':
            hum_id = int(input("Enter human's ID: "))
            cursor.execute('SELECT * FROM human WHERE id = :id', {'id': hum_id})
            print(cursor.fetchall())
            connection.commit()


    def update(self):
        updating = input('SELECT what to UPDATE (name, age, height, weight, id): ').lower()
        if updating == 'age':
            hum_a = int(input('Enter human age which you want to change: '))
            new_age = int(input("Enter new age: "))
            cursor.execute('UPDATE human SET age = :new_age WHERE age = :hum_a', {'new_age': new_age, 'hum_a': hum_a})
            connection.commit()

    def delete(self):
        deleting = input('SELECT with (name, age, height, weight, id) to DELETE: ').lower()
        if deleting == 'id':
            hum_id = int(input("Enter human's ID: "))
            cursor.execute('DELETE FROM human WHERE id = :id', {'id': hum_id})
            connection.commit()



human = Human("Cristiano", 36, 186, 78, 1)
human2 = Human("Lionel", 33, 170, 67, 2)


# human.insert()
# human2.insert()
# human.select()
# human2.select()
# human.update()
# human2.delete()


class Phone:
    def __init__(self, name, model, storage, id):
        self.name = name
        self.model = model
        self.storage = storage
        self.id = id

    def insert(self):
        try:
            cursor.execute('INSERT INTO phones VALUES (:name, :model :storage)',
                           {'name': self.name, 'model': self.model, 'storage': self.storage, 'id': self.id})
            connection.commit()
        except Exception:
            cursor.execute('CREATE TABLE IF NOT EXISTS phones (name TEXT, model TEXT, storage TEXT, id INTEGER)')
            connection.commit()

    def select(self):
        selecting = input('SELECT with (name, model, storage, id): ').lower()
        if selecting == 'id':
            ph_id = int(input("Enter phone's ID: "))
            cursor.execute('SELECT * FROM phones WHERE id = :id', {'id': ph_id})
            print(cursor.fetchall())
            connection.commit()


    def update(self):
        updating = input('SELECT what to UPDATE (name, model, storage, id): ').lower()
        if updating == 'id':
            ph_id = input('Enter phone ID which you want to change: ')
            new_id = int(input("Enter new ID: "))
            cursor.execute('UPDATE phones SET id = :new_id WHERE id = :r_id', {'new_id': new_id, 'ph_id': ph_id})
            connection.commit()


    def delete(self):
        deleting = input('SELECT with (name, model, storage, id): ').lower()
        if deleting == 'storage':
            ph_storage = int(input("Enter phone's storage: "))
            cursor.execute('DELETE FROM phones WHERE storage = :storage', {'storage': ph_storage})
            connection.commit()


phone = Phone('IPhone', 'IPhone 7', 128, 1)
phone2 = Phone('IPhone', 'IPhone 11', 256, 2)
# phone.insert()
# phone2.insert()

connection.close()