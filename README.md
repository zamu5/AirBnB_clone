# AirBnB_clone 

![HBnB](https://github.com/zamu5/AirBnB_clone/blob/master/image/HBnB.png)

## Description

This project is the first step of a big project with the goal of deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.com/)

![Console](https://github.com/zamu5/AirBnB_clone/blob/master/image/console.png)

This fisrt step is manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”, at the end of this project we will have:
- [x] Create your data model
- [x] Manage (create, update, destroy, etc) objects via a console / command interpreter
- [x] Store and persist objects to a file (JSON file)

## Command interpreter 

### What is it? 🚀

A command interpreter allows the user to interact with a program using commands in the form of text lines. In this project we are going to use a command interpreter diferrent methods (table class) to a differents types of classes (table methos)

Class | Attributes
------------ | -------------
BaseModel | id, created_at, updated_at
User | email, password, first_name, last_name
Place | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
State | ame
City | state_id, name
Amenity | name
Review | place_id, user_id: string, text


Methods | Syntax
------------ | -------------
Create | create (class name)
Show | show (class name) (id)
Destroy | destroy (class name) (id)
All | all (class name) (optional)
(class name).(method) | (class name).(method)(arguments of the method) 

### How to start it 🔧

To start use the console is necesary execute the file console.py
```
# execute the file
$ AirBnB_clone ./console.py 
(hbnb) 
```

### How to use it 📦

To use the console is necesary follow the syntax of the table methods in base of the classes of the table class

```
(hbnb) create User
f65e5ae6-b555-44f4-9a36-15003963b63f
```

### Examples ⚙️

Let's start creating classes.

```
(hbnb) create User
f65e5ae6-b555-44f4-9a36-15003963b63f
(hbnb) create Place
f324857e-d73b-424d-b555-ab7795ddb1c9
```

Now show One of the classes and destoy it.
```
(hbnb) show User f65e5ae6-b555-44f4-9a36-15003963b63f
[User] (f65e5ae6-b555-44f4-9a36-15003963b63f) {'created_at': datetime.datetime(2019, 11, 13, 10, 30, 20, 674305), 'updated_at': datetime.datetime(2019, 11, 13, 10, 30, 20, 674368), 'id': 'f65e5ae6-b555-44f4-9a36-15003963b63f'}
(hbnb) destroy User f65e5ae6-b555-44f4-9a36-15003963b63f
(hbnb) show User f65e5ae6-b555-44f4-9a36-15003963b63f
** no instance found **
```
Finally updtate an attribute of a class and show it
```
(hbnb) update Place f324857e-d73b-424d-b555-ab7795ddb1c9 latitude 5.6
(hbnb) all
["[Place] (9ba0e72b-e2f5-4709-89c6-a674f545aa79) {'name': 'Betty', 'age': '89', 'id': '9ba0e72b-e2f5-4709-89c6-a674f545aa79', 'created_at': datetime.datetime(2019, 11, 13, 9, 30, 37, 403455), 'first_name': 'John', 'latitude': 89.0, 'updated_at': datetime.datetime(2019, 11, 13, 9, 40, 5, 280079)}", "[Place] (f324857e-d73b-424d-b555-ab7795ddb1c9) {'id': 'f324857e-d73b-424d-b555-ab7795ddb1c9', 'created_at': datetime.datetime(2019, 11, 13, 10, 30, 28, 366510), 'latitude': 5.6, 'updated_at': datetime.datetime(2019, 11, 13, 10, 31, 47, 761770)}"]
(hbnb)
```
## Files  📄

File| Description
------------ | -------------
[console.py](https://github.com/zamu5/AirBnB_clone/blob/master/console.py) | Contains the entry point of the command interpreter
[base_model](https://github.com/zamu5/AirBnB_clone/blob/master/models/base_model.py) | Defines all common attributes/methods for other classes
[amenity.py](https://github.com/zamu5/AirBnB_clone/blob/master/models/amenity.py) | Class Amenity
[city.py](https://github.com/zamu5/AirBnB_clone/blob/master/models/city.py) | Class City
[place.py](https://github.com/zamu5/AirBnB_clone/blob/master/models/place.py) | Class Place
[review.py](https://github.com/zamu5/AirBnB_clone/blob/master/models/review.py) | Class Review
[state.py](https://github.com/zamu5/AirBnB_clone/blob/master/models/state.py) | Class State
[user.py](https://github.com/zamu5/AirBnB_clone/blob/master/models/User.py) | Class User
[file_storage.py](https://github.com/zamu5/AirBnB_clone/blob/master/models/engine/file_storage.py) | Serializes instances to a JSON file and deserializes JSON file to instances

## Deployment  📦

[Python 3](https://www.python.org/) - the code 

## Author ✒️

* **David Peralta** - [david-develop](https://github.com/david-develop)
* **Sergio Zamudio** - [zamu5](https://github.com/zamu5)
