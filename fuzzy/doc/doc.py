
def getMinMax(set):
    """get tuple with minimum and maximum x-values used by the set."""
    min = None
    max = None

    ig = set.getIntervalGenerator()

    next = ig.nextInterval(None,None)
    min = next
    while next is not None:
        max = next
        next = ig.nextInterval(next,None)

    return (min,max)

def getGlobalMinMax(variable):
    """get tuple with minimum and maximum x-values used by the sets of this variable."""
    min = None
    max = None
    for a in variable.adjectives.values():
        (min2,max2) = getMinMax(a.set)
        if min is None or min2 < min:
            min = min2
        if max is None or max2 > max:
            max = max2
    return (min,max)


def getPoints(variable):
    """Collect all important points of all adjectives in this variables."""

    from fuzzy.set.Set import merge
    # merge them all
    temp = None
    for a in variable.adjectives.values():
        if temp is None:
            temp = a.set;
        else:
            temp = merge(max,temp,a.set)

    # collect points
    points = []
    ig = temp.getIntervalGenerator()
    next = ig.nextInterval(None,None)
    prev = None
    only_once = 0
    while next is not None:
        if next != prev: # avoid to have same value twice
            points.append(next)
            only_once = 0
        else:
            if only_once == 0:
                points = points[:-1]
                points.append(next-0.001) # not the best solution !!!!
                points.append(next)
                points.append(next+0.001) # not the best solution !!!!
                only_once = 1
        prev = next
        next = ig.nextInterval(prev,None)

    return points


class Doc:

    def __init__(self,directory="doc"):
        self.directory=directory

    def initGnuplot2D(self,filename="plot",xlabel=None,ylabel=None,title=None,xrange_=None,yrange=None,x_logscale=0,y_logscale=0):
        import Gnuplot
        g = Gnuplot.Gnuplot(debug=0)
        if xlabel:
            g.xlabel(xlabel)
        if ylabel:
            g.ylabel(ylabel)
        if title:
            g.title(title)
        if xrange_:
            g('set xrange [%f:%f]' % xrange_)
        else:
            g('set autoscale x')
        if yrange:
            g('set yrange  [%f:%f]' % yrange)
        else:
            g('set autoscale y')
        if x_logscale:
            g('set logscale x')
            g('set autoscale x')
        if y_logscale:
            g('set logscale y')
            g('set autoscale y')
        g("set terminal png small transparent truecolor nocrop")
        g("set output '%s/%s.png'" % (self.directory,filename))

        return g

    def initGnuplot3D(self,filename="plot3D",xlabel=None,ylabel=None,zlabel=None,title=None,xrange_=None,yrange=None,zrange=None,x_logscale=0,y_logscale=0,z_logscale=0):
        import Gnuplot
        g = Gnuplot.Gnuplot(debug=0)
        if xlabel:
            g.xlabel(xlabel)
        if ylabel:
            g.ylabel(ylabel)
        if zlabel:
            g("set zlabel '%s'" % zlabel)
        if title:
            g.title(title)
        if xrange_:
            g('set xrange [%f:%f]' % xrange_)
        else:
            g('set autoscale x')
        if yrange:
            g('set yrange  [%f:%f]' % yrange)
        else:
            g('set autoscale y')
        if zrange:
            g('set zrange  [%f:%f]' % zrange)
        else:
            g('set autoscale z')
        if x_logscale:
            g('set logscale x')
            g('set autoscale x')
        if y_logscale:
            g('set logscale y')
            g('set autoscale y')
        if z_logscale:
            g('set logscale z')
            g('set autoscale z')
        g("set terminal png small transparent truecolor nocrop")
        g("set output '%s/%s.png'" % (self.directory,filename))
        #g('set style data lines')
        g('set style data pm3d')
        #g('set hidden3d')
        g('set pm3d flush begin ftriangles scansforward interpolate 10,10')
        g('set contour')
        return g

    def getValues(self,v):
        (min,max) = getGlobalMinMax(v)
        width = max - min
        min = min - 0.1 * width
        max = max + 0.1 * width
        width = max - min

        values = [min]+getPoints(v)+[max]

        return (min,max,values)

    def createDoc(self,system):
        """create plots of all variables defined in the given system."""

        for v_name in system.variables.keys():
            #try:
                v = system.variables[v_name]

                self.createDocVariable(v,v_name)
            #except:
            #    print "no doc for " + v_name

    def createDocVariable(self,v,name,x_logscale=0,y_logscale=0):
        """Creates a 2D plot of a variable"""

        import Gnuplot
        import Gnuplot.funcutils

        # sort adjectives by lowest x values
        adjs = v.adjectives.keys()
        def cmp(a1,a2):
            s1 = v.adjectives[a1].set
            s2 = v.adjectives[a2].set
            x1 = s1.getIntervalGenerator().nextInterval(None,None)
            x2 = s2.getIntervalGenerator().nextInterval(None,None)
            # get lower x values
            if x1 > x2:
                return +1
            if x1 < x2:
                return -1
            # get higher membership value
            return int(s2(x2)-s1(x1))

        adjs.sort(cmp)

        (min,max,x) = self.getValues(v)

        # calculate values
        plot_items = []
        for a_name in adjs:
            a = v.adjectives[a_name]
            plot_items.append(Gnuplot.funcutils.compute_Data(x, a.set, title=a_name, inline=1))

        g = self.initGnuplot2D(filename=name,xlabel="",ylabel="membership",title=name,xrange_=(min,max),yrange=(-0.2,1.2))
        g('set style fill transparent solid 0.5 border')
        g('set style data filledcurves y1=0')
        apply(g.plot,plot_items)
        g("reset")

    def create2DPlot(self,system,x_name,y_name,input_dict={},output_dict={},x_logscale=0,y_logscale=0):
        """Creates a 2D plot of an input variable and an output variable.
        Other (const) variables have to be set beforehand in the dictionary input_dict."""

        import Gnuplot
        import Gnuplot.funcutils

        (x_min,x_max,x) = self.getValues(system.variables[x_name])

        def f(x,
                system=system,
                x_name=x_name,
                y_name=y_name,
                input_dict=input_dict,
                output_dict=output_dict):
            input_dict[x_name]=x
            output_dict[y_name]=0.0
            try:
                system.calculate(input_dict,output_dict)
            except:
                pass
            return output_dict[y_name]

        g = self.initGnuplot2D(filename=x_name+"_"+y_name,xlabel=x_name,ylabel=y_name,title=y_name+"=f("+x_name+")",xrange_=(x_min,x_max))
        g('set style data lines')
        g.plot(Gnuplot.funcutils.compute_Data(x, f, inline=1))
        g("reset")

    def create3DPlot(self,system,x_name,y_name,z_name,input_dict={},output_dict={},x_logscale=0,y_logscale=0,z_logscale=0):
        """Creates a 3D plot of 2 input variables and a output variable.
        Other (const) variables have to be set beforehand in the dictionary input_dict."""

        import Gnuplot
        import Gnuplot.funcutils

        (x_min,x_max,x) = self.getValues(system.variables[x_name])
        (y_min,y_max,y) = self.getValues(system.variables[y_name])

        def f(x,y,
                system=system,
                x_name=x_name,
                y_name=y_name,
                z_name=z_name,
                input_dict=input_dict,
                output_dict=output_dict):
            input_dict[x_name]=x
            input_dict[y_name]=y
            output_dict[z_name]=0.0
            try:
                system.calculate(input_dict,output_dict)
            except:
                pass
            return output_dict[z_name]

        g = self.initGnuplot3D(filename=x_name+"_"+y_name+"_"+z_name,xlabel=x_name,ylabel=y_name,zlabel=z_name,title="%s=f(%s,%s)" % (z_name,x_name,y_name),xrange_=(x_min,x_max),yrange=(y_min,y_max),x_logscale=x_logscale,y_logscale=y_logscale,z_logscale=z_logscale)
        g.splot(Gnuplot.funcutils.compute_GridData(x,y, f,binary=0,inline=1))
        g("reset")


    def create3DPlot_adjective(self,system,x_name,y_name,z_name,adjective,input_dict={},output_dict={},x_logscale=0,y_logscale=0,z_logscale=0):
        """Creates a 3D plot of 2 input variables and a output variable.
        Other (const) variables have to be set beforehand in the dictionary input_dict."""

        import Gnuplot
        import Gnuplot.funcutils

        (x_min,x_max,x) = self.getValues(system.variables[x_name])
        (y_min,y_max,y) = self.getValues(system.variables[y_name])

        def f(x,y,
                system=system,
                x_name=x_name,
                y_name=y_name,
                z_name=z_name,
                adjective=adjective,
                input_dict=input_dict,
                output_dict=output_dict):
            input_dict[x_name]=x
            input_dict[y_name]=y
            output_dict[z_name]=0.0
            try:
                system.calculate(input_dict,output_dict)
            except:
                pass
            return output_dict[z_name][adjective]

        g = self.initGnuplot3D(filename=x_name+"_"+y_name+"_"+z_name,xlabel=x_name,ylabel=y_name,zlabel=z_name,title="%s.%s=f(%s,%s)" % (z_name,adjective,x_name,y_name),xrange_=(x_min,x_max),yrange=(y_min,y_max),x_logscale=x_logscale,y_logscale=y_logscale,z_logscale=z_logscale)
        g.splot(Gnuplot.funcutils.compute_GridData(x,y, f,binary=0,inline=1))
        g("reset")
