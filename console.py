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
            if value.__class__.__name__ == input2.split('')[0]  and value.id == input2.split('')[1]:
                print(value.__str__())
                return
            print("** no instance found **")

    def do_destroy(self, _input):
        """ Deletes an instance depending on class name and id """
        if len(_input.split('')[0]) is 0:
            print("** class name missing **")
            return
        if _input.split('')[0] not in self.collection.keys:
            print("** class doesn't exist **")
            return
        if len(_input.split('')) is 1:
            print("** instance id is missing**")
            return
        class_name, class_id = (_input.split('')[0], _input.split('')[1])
        query_key = class_name + '.' + class_id
        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return
        del models.storage.all()[query_key]
        models.storage.save()

    def do_all(self, _input_class):
        """ prints string representation of all instance """
        if _input__class:
            if _input_class not in self.collection.keys:
                print("** class doesn't exist **")
                return
        for key_items in models.storage.all().keys():
            key_items = models.storage.all()[key_items]
            print(key_items)
        return

    def do_update(self, _input):
        """ updates an instance based on the class name and id by adding attribute """
        _input = shlex.split(_input)
        query_key = ''

        if len(_input) is 0:
            print("** class name is missing **")
            return
        if _input[0] not in self.collection_keys:
            print("** class doesn't exist **")
            return
        if len(_input) is 1:
            print("** instance id missing **")
            return
        if len(_input) > 1:
            query_key = _input[0] + '.' + _input[1]
        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return
        if len(_input) is 2:
            print("** attribute name missing **")
            return
        if len(_input) is 3:
            print("** value missing **")
            return
        key_name = input[2]
        input_value = _input[3]
        setattr(models.storage.all()[query_key],key_name, input_value)
        models.storage.all()[query_key].save()

    def default(self, inp):
        """Retrieve all instances class using class name>.all()"""
        count = 0
        words = inp.split(".")
        if words[0] in classes_dic and words[1] == "all()":
            self.do_all(words[0])
        elif words[0] in classes_dic and words[1] == "count()":
            if (words[0] not in classes_dic):
                print("** class doesn't exist **")
                return
            else:
                for key in models.storage.all():
                    if key.startswith(words[0]):
                        count +=1
                print(count)
        else:
            print("*** Unknown syntax: {}". format(inp))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
