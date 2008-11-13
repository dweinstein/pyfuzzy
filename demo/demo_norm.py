#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: demo_norm.py,v 1.5 2008-11-13 20:43:09 rliebscher Exp $"


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
    g('set style data lines')
    g('set hidden')
    g('set contour surface')
    g('set cntrparam levels 10')
    g('set border 4095')
    g('set xyplane at 0')
    g('set colorbox user origin 0.9,0.05 size 0.05,0.5')
    g('set noautoscale xy')
    g('set xrange [0:1]')
    g('set yrange [0:1]')
    g('set zrange [0:1]')
    g('set cbrange [0:1]')
    g.xlabel('x')
    g.ylabel('y')
    g('set pm3d at s')
    return g


def plot(norm,title,filename,gnuplot=None,interactive=False):
    # Demonstrate a 3-d plot:
    # set up x and y values at which the function will be tabulated:
    import Numeric
    # use values  0.00 0.02 0.04 ... 0.96 0.98 1.00
    x = Numeric.arange(51)/50.0
    y = Numeric.arange(51)/50.0

    g = gnuplot or get_Gnuplot()
    g.title(title) 
    print "Plot %s ... " % title
    #g.splot(Gnuplot.funcutils.compute_GridData(x,y, norm, binary=1))
    if interactive == False:
        g("set terminal png small truecolor nocrop")
        g("set output 'norm/%s.png'" % filename)
    g.splot(Gnuplot.funcutils.compute_GridData(x,y, norm, binary=0))
    if interactive == True:
        raw_input('Please press return to continue...\n')
    if gnuplot is None:
        g("reset")
    g = None


def plotNorm(norm,name,params=[0.05,0.25,0.50,0.75,0.95],gnuplot=None,interactive=False):
    import fuzzy.norm.ParametricNorm
    if isinstance(norm,fuzzy.norm.ParametricNorm.ParametricNorm):
        for p in params:
            norm.p = p
            title = "%s (p=%4.2f)" % (name,p)
            filename = "%s_%.2f" % (name,p)
            plot(norm,title,filename,gnuplot,interactive)
    else:
        title = "%s" % (name)
        filename = title
        plot(norm,title,filename,gnuplot,interactive)


def test():
    """Show examples for all norm in package fuzzy.norm"""
    objects = get_classes()
    keys = objects.keys()
    keys.sort()

    for name in keys:
        try:
            norm = objects[name]
            plotNorm(norm,name)
        except Exception,e:
            print "Exception: " , e

def interactive(name,params):
    objects = get_classes()
    try:
        norm = objects[name]
    except KeyError:
        print "%s is unknown." % name 
        return

    g = get_Gnuplot()

    if len(params) > 0:
        plotNorm(norm,name,params,gnuplot=g,interactive=True)
    else:
        plotNorm(norm,name,gnuplot=g,interactive=True)


# when executed, just run test():
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        interactive(sys.argv[1],[float(x) for x in sys.argv[2:]])
    else:
        test()

