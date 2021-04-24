import sqlite3

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("CREATE TABLE classmates (name TEXT, surname TEXT, age: INTEGER, id INTEGER");

connection.close()

# У меня не про-шка изза этого все вместе.

(
INSERT INTO classmates VALUES (name: "Sultan", surname: "Kelsin", age: 16, id: 1);
INSERT INTO classmates VALUES (name: "Baiel", surname: "Shermatov", age: 16, id: 2);
INSERT INTO classmates VALUES (name: "Ulan", surname: "Nurbek Uulu", age: 16, id: 3);
INSERT INTO classmates VALUES (name: "Arslan", surname: "Turdaliev", age: 16, id: 4);
INSERT INTO classmates VALUES (name: "Musa", surname: "Aitmamatov", age: 16, id: 5);
INSERT INTO classmates VALUES (name: "Ruslan", surname: "Asanov", age: 16, id: 6);
INSERT INTO classmates VALUES (name: "Adilet", surname: "Jienaliev", age: 15, id: 7);
INSERT INTO classmates VALUES (name: "Ruslan", surname: "Abdusalyamov", age: 16, id: 8);
INSERT INTO classmates VALUES (name: "Nurkamil", surname: "Maksatbekov", age: 17, id: 9);
INSERT INTO classmates VALUES (name: "Usen", surname: "Aliev", age: 16, id: 10);

SELECT name FROM classmates;

DELETE FROM classmates WHERE id = 9;

DELETE FROM classmates WHERE name = "Usen" or id = 10;

UPDATE students set surname = "Abdykerimov" where id = 3;
)
