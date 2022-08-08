#!/usr/bin/python3
""" console """

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex

classes_dic = {"BaseModel":BaseModel, "User":User, "State":State, "City":City, "Place":Place, "Amenity":Amenity, "Review":Review}

class HBNBCommand(cmd.Cmd):
    """ Start of the command interpreter """
    collection_keys = classes_dic.keys()
    prompt = '(hbnb)'

    def do_quit(self, _input):
        """ command to exit the programm """
        return True

    def do_EOF(self, _input):
        """ exit command cosole """
        return True

    def emptyline(self):
        """ Empty line should not excute anything """
        return False

