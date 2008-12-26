#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: demo_set.py,v 1.7 2008-12-26 18:14:24 rliebscher Exp $"

try:
    # If the package has been installed correctly, this should work:
    import Gnuplot, Gnuplot.funcutils
except ImportError:
    print "Sorry, you need Gnuplot to use this."
    import sys
    sys.exit(1)

from utils import get_classes

x_min,x_max = -1.5,+1.5

def getGnuplot():
    # A straightforward use of gnuplot.  The `debug=1' switch is used
    # in these examples so that the commands that are sent to gnuplot
    # are also output on stderr.
    g = Gnuplot.Gnuplot(debug=0)
    g(' set style fill solid 0.5 border')
    g('set style data filledcurves y1=0')
    g('set noautoscale xy')
    g('set xrange [%f:%f]' % (x_min,x_max))
    g('set yrange [-0.2:1.2]')
    g.xlabel('x')
    g.ylabel('y')
    return g

def test():
    """Plot all defined classes in fuzzy.set package"""

    import Numeric
    import fuzzy.set

    steps = 50
    # make array in range x_min,x_max
    x = Numeric.arange(int((x_max-x_min)*steps))/float(steps) + x_min 

    objects = get_classes(fuzzy.set)

    # add demo sets
    from fuzzy.set.Polygon import Polygon
    objects["Polygon (Demo)"] = Polygon([
            (-1.2,0),
            (-1.2,1),
            (-0.8,0.3),
            (-0.3,0.2),
            (-0.2,0.4),
            (-0.1,0.0),
            (0.0,0.0),
            (0.3,1),
            (0.6,0.5),
            (0.6,0.1),
            (1.3,0.6),
        ])
    for name in sorted(objects):
        if name in ["Set", "Function","Polygon"]:
            continue
        obj = objects[name]

        g = getGnuplot()
        g.title(name)

        try:
            print "Plot %s ... " % name
            g("set terminal png small truecolor")
            g("set output 'set/%s.png'" % name)
            if isinstance(obj,fuzzy.set.Polygon.Polygon):
                p = obj.points
                if len(p) == 0:
                    continue
                if p[0][0]>x_min:
                    p.insert(0,(x_min,p[0][1]))
                if p[-1][0]<x_max:
                    p.append((x_max,p[-1][1]))
                g.plot(p)
            else:
                g.plot(Gnuplot.funcutils.compute_Data(x,obj))
        except:
            import traceback
            traceback.print_exc()
        #raw_input('Please press return to continue...\n')
        g.close()
        g = None

# when executed, just run test():
if __name__ == '__main__':
    test()

