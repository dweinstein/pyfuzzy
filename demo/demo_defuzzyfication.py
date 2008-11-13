#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: demo_defuzzyfication.py,v 1.6 2008-11-13 20:42:30 rliebscher Exp $"


def get_classes(classes_dir):
    import os,sys,imp
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
    import os,types
    import fuzzy.set
    import fuzzy.defuzzify
    import fuzzy.OutputVariable
    import fuzzy.Adjective

    row1 = 10
    row2 = 25

    sets = get_classes(os.path.dirname(fuzzy.set.__file__))
    sets_keys = sets.keys()
    sets_keys.sort()
    defuzzy = get_classes(os.path.dirname(fuzzy.defuzzify.__file__))
    defuzzy_keys = defuzzy.keys()
    defuzzy_keys.sort()

    for d in defuzzy_keys:
        defuzzy_ = defuzzy[d]
        # filter out abstract base classes
        if defuzzy_.__class__.__name__ in ["Base"]:
            continue

        v = fuzzy.OutputVariable.OutputVariable(defuzzy=defuzzy_)
        print "Using %s:" % defuzzy_.__class__.__name__
        print "%-*s | %s" % (row1,"class","defuzzyfication value")
        print "%s-+-%s" % ("-"*row1,"-"*row2)

        for o in sets_keys:
            set = sets[o]
            # filter out classes without default values
            if set.__class__.__name__ in ["Set","Function","Polygon"]:
                continue
            try:
                a = fuzzy.Adjective.Adjective(set)
                a.setMembership(1.0)
                v.adjectives["test"] = a
                result = v.getValue()
                if isinstance(result,types.FloatType):
                    result = "%.3g" % result
                else:
                    result = str(result)
                print "%-*s | %s" % (row1,set.__class__.__name__,result) 
            except Exception,e:
                print "%-*s |         >>> %s <<<" % (row1,set.__class__.__name__,e)
        print

# when executed, just run test():
if __name__ == '__main__':
    test()

