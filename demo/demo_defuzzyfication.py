#!/usr/bin/env python

__revision__ = "$Id: demo_defuzzyfication.py,v 1.2 2003-03-20 08:47:28 rliebscher Exp $"


def get_classes():
    import os,sys,imp
    import fuzzy.set.Set
    classes_dir = os.path.dirname(fuzzy.set.__file__)
    suffixes = []
    for suffix in imp.get_suffixes():
        suffixes.append(suffix[0])
    sys.path = [classes_dir] + sys.path
    objects = {}
    for class_file in os.listdir(classes_dir):
        for suffix in suffixes:
            class_name = class_file[:-len(suffix)]
            if class_name == "__init__":
                break
            if  class_file[-len(suffix):] == suffix:
                module = __import__(class_name) 
                objects.update({class_name: module.__dict__[class_name]()})
                break
    return objects


def test():
    """test all found set classes with defuzzyfication method in specific kind
       of output variable class"""
    objects = get_classes()
    keys = objects.keys()
    keys.sort()
    print "%-25s | %s" % ("class","defuzzyfication value")
    print "%25s-+-%s" % ("-------------------------","----------------------")
    for o in keys:
	try:
	    import fuzzy.Adjective
	    a = fuzzy.Adjective.Adjective(objects[o])
	    a.setMembership(1.0)
	    import fuzzy.OutputVariableMaxRight
	    v = fuzzy.OutputVariableMaxRight.OutputVariableMaxRight()
	    v.adjectives["test"] = a
	    print "%-25s | %s" % (objects[o].__class__,str(v.getValue()))	    
        except Exception,e:
            print "%-25s |                %s" % (objects[o].__class__,e)

# when executed, just run test():
if __name__ == '__main__':
    test()

