#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: demo_set.py,v 1.3 2008-10-08 14:50:06 rliebscher Exp $"


try:
    # If the package has been installed correctly, this should work:
    import Gnuplot, Gnuplot.funcutils
except ImportError:
    print "Sorry, you need Gnuplot to use this."
    import sys
    sys.exit(1)


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
    """"""

    from Numeric import *

    # A straightforward use of gnuplot.  The `debug=1' switch is used
    # in these examples so that the commands that are sent to gnuplot
    # are also output on stderr.
    g = Gnuplot.Gnuplot(debug=0)

    x = arange(150)/50.0 - 1.5 
    g('set data style lines')
    g('set noautoscale xy')
    g('set xrange [-1.5:1.5]')
    g('set yrange [-0.2:1.2]')
    #g('set zrange [0:1]')
    g.xlabel('x')
    g.ylabel('y')

    objects = get_classes()
    keys = objects.keys()
    keys.sort()
    for o in keys:
        g.title(o)
        
        try:
            print "Plot %s ... " % o
#            g.plot(Gnuplot.funcutils.compute_Data(x,objects[o]))
	    g("set terminal png small color")
	    g("set output 'set/%s.png'" % o)
            g.plot(Gnuplot.funcutils.compute_Data(x,objects[o]))
	    g("set terminal x11");
	    g("set output")
        except Exception,e:
            print e
        raw_input('Please press return to continue...\n')

# when executed, just run test():
if __name__ == '__main__':
    test()

