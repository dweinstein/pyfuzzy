#!/usr/bin/env python

__revision__ = "$Id: demo_norm.py,v 1.2 2003-03-20 08:47:29 rliebscher Exp $"


try:
    # If the package has been installed correctly, this should work:
    import Gnuplot, Gnuplot.funcutils
except ImportError:
    print "Sorry, you need Gnuplot to use this."
    import sys
    sys.exit(1)


def get_classes():
    import os,sys,imp
    import fuzzy.norm.Norm
    classes_dir = os.path.dirname(fuzzy.norm.__file__)
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

def get_Gnuplot():
    # A straightforward use of gnuplot.  The `debug=1' switch is used
    # in these examples so that the commands that are sent to gnuplot
    # are also output on stderr.
    g = Gnuplot.Gnuplot(debug=0)
    g('set parametric')
    g('set data style lines')
    g('set hidden')
    g('set contour base')
    g('set noautoscale xy')
    g('set xrange [0:1]')
    g('set yrange [0:1]')
    g('set zrange [0:1]')
    g.xlabel('x')
    g.ylabel('y')
    return g

def test(single=0,use_p=0):
    """ single = 1 means use a single instance of Gnuplot for all.
        use_p = 1 means show parametric norm with different values of p."""
    import fuzzy.norm.ParametricNorm

    from Numeric import *

    # use values  0.01 0.03 0.05 ... 0.95 0.97 0.99
    x = arange(49)/50.0 + 0.01 
    y = arange(49)/50.0 + 0.01

    objects = get_classes()
    keys = objects.keys()
    keys.sort()

    if single != 0:
        g = get_Gnuplot()
    else:
        gnuplots = [] # hold references
    for o in keys:
        # Demonstrate a 3-d plot:
        # set up x and y values at which the function will be tabulated:    
        try:
            norm = objects[o]
            if isinstance(norm,fuzzy.norm.ParametricNorm.ParametricNorm):
                for p in [0.01,0.25,0.50,0.75,0.99]:
                    norm.p = p
                    title = "%s (p=%4.2f)" % (o,p)
                    if single == 0: g = get_Gnuplot()
                    g.title(title) 
                    print "Plot %s ... " % title
                    #g.splot(Gnuplot.funcutils.compute_GridData(x,y, norm, binary=1))
		    g("set terminal png small color")
		    g("set output 'norm/%s.png'" % ("%s_%.2f" % (o,p)))
                    g.splot(Gnuplot.funcutils.compute_GridData(x,y, norm, binary=1))
		    g("set terminal x11");
		    g("set output")
                    if single == 0: gnuplots.append(g)
                    else:             raw_input('Please press return to continue...\n')
            else:
                    title = "%s" % (o)
                    if single == 0: g = get_Gnuplot()
                    g.title(title) 
                    print "Plot %s ... " % title
                    #g.splot(Gnuplot.funcutils.compute_GridData(x,y, norm, binary=1))
		    g("set terminal png small color")
		    g("set output 'norm/%s.png'" % title)
                    g.splot(Gnuplot.funcutils.compute_GridData(x,y, norm, binary=1))
		    g("set terminal x11");
		    g("set output")
                    if single == 0: gnuplots.append(g)
                    else:             raw_input('Please press return to continue...\n')
        except Exception,e:
            print "Exception: " , e
            if single != 0: raw_input('Please press return to continue...\n')
    if single == 0:
        raw_input('Please press return to continue...\n')
        
# when executed, just run test():
if __name__ == '__main__':
    import sys
    single = 1
    use_p = 0
    if "all" in sys.argv[1:]:
        single = 0
    if "p" in sys.argv[1:]:
        use_p = 1  
    test(single,use_p)

