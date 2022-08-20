# DouglasPeuckerModified
Ramer-Douglas-Peucker algorithm modified to simplify height of polylines
Modify Ramer-Douglas-Peucker algorithm to work in the distance-elevation plane instead of the x-y plane. This will mark z entries that are placed close to a linear z development. These vertices, which will normally be eliminated by the algorithm, can now be adjusted to the z value exactly on the simplified line.

The UI is first designed using Qt Designer with QGIS, and then using python to compile and add some more codes.

The project consists of three python scripts:

* DouglasPeucker.py: the main script. Run this script to start the application. It consists of a QMainWindow class.

* ui_mainwindow.py: the script consists of code defining the UI of the application window. It is compiled from the .ui file generated in Qt Designer.

* functions.py: the script consists of functions used to perform Ramer-Douglas-Peucker algorithm.
