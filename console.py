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
    
    def do_create(self, _input_class_name):
        """ creates new instance of BaseModel in JSON """
        if not _input_class_name:
            print("** class name missing **")
	    return
        if _input_class_name not in classes_dic.keys():
            print("** class doesnt exist **")
	    return
        newinstance = classes.dic[_input_class_name]()
        newinstance.save()
        print(newinstance.id)

    def do_show(self, _input):
        """ prints string representation of the instance based on the class name """
        input2 = _input
	if len(input2.split('')[0]) is 0:
            print("** class name missing **")
	    return
        if input2.split('')[0] not in self.collectio.keys:
            print("** class doesnt exist **")
	    return
        if len(input2.split()) is 1:
            print("** instance id missing **")
	    return
        models.storage.reload()
        for key, value in models.storage.all().items():
            if value.__class__.__name__ == input2.split('')[0] \ and value.id == input2.split('')[1]:
                print(value.__str__())
                return
            print("** no instance found **")

