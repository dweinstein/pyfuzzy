
def __import_classes(dir):
    """ Import any classes in the named directory.
        So you can simply add new classes to the directory,
        you only have to define in each module a symbol(class)
        of the same name as the module itself.

        Similar to "from dir import *", but you dont need to specify
        all classes in dir in __init__.py.  
    """
    import os,sys,imp
    old_sys_path = sys.path
    classes_dir = os.path.dirname(__file__) + os.sep + dir
    suffixes = []
    for suffix in imp.get_suffixes():
        suffixes.append(suffix[0])
    sys.path = [classes_dir] + sys.path
    for class_file in os.listdir(classes_dir):
        for suffix in suffixes:
            class_name = class_file[:-len(suffix)]
            if class_name == "__init__":
                break
            if  class_file[-len(suffix):] == suffix:
                module = __import__(class_name) 
                globals()[class_name] = module.__dict__[class_name]
                break

    sys.path = old_sys_path

#__import_classes(".")
