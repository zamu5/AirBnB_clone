# AirBnB_clone 

![HBnB](https://github.com/zamu5/AirBnB_clone/HBnB.png)

## Description

This project is the first step of a big project with the goal of deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.com/)

![Console](https://github.com/zamu5/AirBnB_clone/console.png)

This fisrt step is manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”, at the end of this project we will have:
- [x] Create your data model
- [x] Manage (create, update, destroy, etc) objects via a console / command interpreter
- [x] Store and persist objects to a file (JSON file)

## Command interpreter

### Classes

Class | Attributes
------------ | -------------
BaseModel | id, created_at, updated_at
User | email, password, first_name, last_name
Place | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
State | ame
City | state_id, name
Amenity | name
Review | place_id, user_id: string, text