#!/usr/bin python3
"""Console Module"""
import cmd
from imp import new_module
import sys
import shlex
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """HBNB Class"""
    prompt = ' (hbnb) '

    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}

    def do_quit(self, arg):
        """This defines the quit option"""
        return True
    def do_EOF(self, arg):
        """Use to define the end of file (EOF)"""
        print()
        return True
    def emptyline(self):
        """Use to define a new line, execute anything"""
        pass
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg:
            """If the argument exist"""
            if arg in self.classes:
                get_class = getattr[sys.modules[__name__], arg]
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")
    
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        string_split = shlex.split(arg)
        if len(string_split) == 0:
            print("** class name missing **")
        elif string_split[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(string_split) == 1:
            print("** instance id missing **")
        else:
            dictionary = models.storage.all()
            dic_key = string_split[0] + '.' + str(string_split[1])
            if dic_key in dictionary:
                print(dictionary[dic_key])
            else:
                print("** instance id missing **")
        return
    
    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        inst_del = shlex.split(arg)
        if len(inst_del) == 0:
            print("** class name missing **")
        elif inst_del[0] not in self.classes:
            print("** class doesn't exist **")
        elif (inst_del) == 1:
            print("** instance id missing **")
        else:
            dictionary_del = models.storage.all()
            del_key = inst_del[0] + '.' + str(inst_del[1])
            if del_key in dictionary_del:
                del dictionary_del[del_key]
                models.storage.save()
            else:
                print("** no instance found **")
        return
    
    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on the class name"""
        all_result = shlex.split(arg)
        new_list = []
        dictionary = models.storage.all() #show all if no class is passed

        if len(all_result) == 0:
            for key in dictionary:
                new_class = str(dictionary[key])
                new_list.append(new_class)
            print(new_list)
            return
        
        if all_result[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_class = ""
            for key in dictionary:
                class_name = key.split('.')
                if class_name[0] == all_result[0]:
                    new_class = str(dictionary[key])
                    new_list.append(new_class)
            print(new_list)
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        new_update = shlex.split(arg)
        if len(new_update) == 0:
            print("** class name missing **")
        elif len(new_update) == 1:
            print("** instance id missing **")
        elif len(new_update) == 2:
            print("** attribute name missing **")
        elif len(new_update) == 3:
            print("** value missing **")
        elif new_update[0] not in self.classes:
            print("** class doesn't exist **")
            return
        update_key = new_update[0] + '.' + str(new_update[1])
        dictionary = models.storage.all()
        try:
            update_instance = dictionary[update_key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(update_instance, update_key[2]))
            update_key[3] = typeA(update_key[3])
        except AttributeError:
            pass
        setattr(update_instance, update_key[2], update_key[3])
        models.storage.save()
    
    def do_count(self, arg):
        """retrieve the number of instances of a class"""
        inst_count = shlex.split(arg)
        dictionary = models.storage.all()
        instance_number = 0
        if inst_count not in self.classes:
            print("** class doesn't exist **")
        else:
            for key in dictionary:
                class_name = key.split('.')
                if class_name[0] == inst_count[0]:
                    instance_number =+ 1
            print(instance_number)










if __name__ == '__main__':
    HBNBCommand().cmdloop()
