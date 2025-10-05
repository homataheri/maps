# Getting started with python programming in QGIS3
# Reference: https://www.qgistutorials.com/en/docs/3/getting_started_with_pyqgis.html

# read the shape file
path = r"C:\Users\homat\Dropbox\projects\11-Self-learning\13-qgis_with_python\ne_10m_airports\ne_10m_airports.shp"

# Create a vector layer via GDAL/OGR provider
vl = QgsVectorLayer(path, "Airports", "ogr")

# Check and add to the project
if vl.isValid():
    QgsProject.instance().addMapLayer(vl)
    print("Layer added:", vl.name(), vl.featureCount(), "features")
else:
    print("Failed to load:", path)


# For interacting with the QGIS environment, we must use the iface variable. To access the currently active layer in QGIS, you can type the following and press 

layer = iface.activeLayer()

# There is a handy function called dir() in python that shows you all available methods for any 
# object. This is useful when you are not sure what functions are available for the object. 
# Run the following command to see what operations we can do on the layer variable.

dir(layer)

# we will use a function called getFeatures() which will gets you the reference to all features of a layer. 
# In our case, each feature will be a point representing an airport. You can type the following command to iterate 
# through each of the features in the current layer.

for f in layer.getFeatures():
    print(f)
    
# The reference to the feature is stored in the f variable. We can use the f variable to access the attributes of 
# each feature. Type the following to print the name and iata_code for each airport feature.

for f in layer.getFeatures():
    print(f['name'], f['iata_code'])
    

# The coordinates of a vector feature can be accessed by calling the geometry() function. This function returns a geometry object that we can store in the variable geom. 
# You can run asPoint() function on the geometry object to get the x and y coordinates of the point. If your feature 
# is a line or a polygon, you can use asPolyline() or asPolygon() functions. Type the following code at the prompt 
# and press Enter to see the x and y coordinates of each feature.

for f in layer.getFeatures():
    geom = f.geometry()
    print(geom.asPoint())

# You can call the x() function on the point object and get its x coordinate.

for f in layer.getFeatures():
    geom = f.geometry()
    print(geom.asPoint().x())

# Now we have all the pieces that we can stitch together to generate our desired output. 
# Type the following code to print the name, iata_code, latitude and longitude of each of the airport features. 
# Here we are using the .format() method which gives more control on printing multiple variables. 
# The .2f notation is to limit the coordinates to 2 decimals.

for f in layer.getFeatures():
  geom = f.geometry()
  print('{},{},{:.2f},{:.2f}'.format(f['name'], f['iata_code'], geom.asPoint().y(), geom.asPoint().x()))

#  create a file and write the output there. 

with open(r'C:\Users\homat\Dropbox\projects\11-Self-learning\13-qgis_with_python\airports.txt', 'w') as file:
  for f in layer.getFeatures():
    geom = f.geometry()
    line = '{},{},{:.2f},{:.2f}\n'.format(f['name'], f['iata_code'], geom.asPoint().y(), geom.asPoint().x())
    file.write(line)








