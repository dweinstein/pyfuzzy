                             Python Fuzzy 
                             release 0.0.2
                            April 22th, 2003


INTRODUCTION
------------

...
This package is intended ...

REQUIREMENTS
------------

This release of the pyfuzzy requires Python 1.5.2 or later.

...

INSTALLATION
------------

Obviously, in order to use pyfuzzy you must first install it.
This is quite easy:

    python setup.py install

Note that this installs to the "site" library directory of your local
Python installation: /usr/local/lib/python1.5/site-packages by default
on Unix, "C:\Program Files\Python" by default on Windows.  Since 
pyfuzzy is "package-ized", the installation process will create a
subdirectory "fuzzy" under the site library directory.

The installation is by default quite verbose.  You can silence it with
the "-q" option:

    python setup.py -q install

but unfortunately the verbosity (of the underlying distutils installer)
is (currently) all or nothing.


USAGE
-----

...

EXAMPLES
--------

...
See at the project website.
In the examples directory you can find three subdirectories:

mixer:
    This is an example of a mixer where you can control the temperature of 
    incoming substances (eg. water) and tries t control to hold the temperature 
    on a constant value.
    It is controlled by a fuzzy controller and shows the typical results of 
    a P controller with time lag.
    
    The example shows how to define and use fuzzy variable, ruler, and the 
    controller. It also realizes storing/loading the controller object to/from 
    a pickled file.
    
pendel:
    This is a (currently) unfinished example of controller for an inverted 
    pendulum. (Also called sometimes pole balancer.)
    The simulation of the pendulum is finished (But the visualisation is not 
    perfect for now.) Uses the menu item Process/View to get it.
    Currently it is controlled by an (imperfect) neural network, which was 
    trained with data from a fuzzy controller (used in the Delphi fuzzy 
    system which was the base of this python fuzzy project)

pendel2:
    This is an (also) unfinished example of controller for the inverted 
    pendulum.
    It uses a simpler pendulum simulation and has already parts of the 
    fuzzy rules in it. (You will see this if you start this example it 
    can only hold it for a moment when it goes to the left side.) 


BUGS AND LIMITATIONS
--------------------

...

CONTRIBUTING
------------

contact : René Liebscher <R.Liebscher@gmx.de>

ACKNOWLEDGMENTS
---------------

[tangible, in roughly chronological order]
  * Rene Liebscher: initial version (basically a heavily imporved 
                                     port of a previous work in Delphi)
  * Marc Vollmer: initial version, examples


$Id: README.txt,v 1.2 2003-04-22 08:38:40 plafoucr Exp $
