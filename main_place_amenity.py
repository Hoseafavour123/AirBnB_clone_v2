#!/usr/bin/python3

"""Test link Place<>Amenity"""
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.city import City


#Creation of state
state = State(name="California")
state.save()

#Creation of city
city = City(state_id=state.id, name="San Francisco")
city.save()

#creation of User
user = User(email="hoseafavour2@gmail.com", password="ipuhi")
user.save()

#Creation of 2 Places
place1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place1.save()
place2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place2.save()

#Creation of 3 various amenities
amenity1 = Amenity(name="Wifi")
amenity1.save()
amenity2 = Amenity(name="Cable")
amenity2.save()
amenity3 = Amenity(name="Oven")
amenity3.save()

#Link place1 with 2 amenities
place1.amenities.append(amenity1)
place1.amenities.append(amenity2)

#Link place2 with 3 amenities
place2.amenities.append(amenity1)
place2.amenities.append(amenity2)
place2.amenities.append(amenity3)

storage.save()

print("Ok")
