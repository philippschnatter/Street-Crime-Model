import arcpy
import numpy
import csv
import os, sys

# Konvertieren Sie ein NumPy-Array in eine Geodatabase-Feature-Class
# https://pro.arcgis.com/de/pro-app/arcpy/get-started/working-with-numpy-in-arcgis.htm

# execfile("CreateFeatureClasses.py")
sr = arcpy.SpatialReference(102022)
for agent in range(0, 1000, 1):
    path = os.path.abspath("C:/ESRIPress/Maputo IMPOSM SHP/project2/07_create_activity_paths/spaces")
    reader = csv.reader(open(path+"\\a"+str(agent)+".csv", "rb"), delimiter=",")
    uid = []
    x = []
    y = []
    next(reader, None)
    for row in reader:
        uid.append(int(row[0]))
        x.append(float(row[1].replace(',','.')))
        y.append(float(row[2].replace(',','.')))
    outdir = "C:/ESRIPress/Maputo IMPOSM SHP/project2/07_create_activity_paths/FC2021/aShape"+str(agent)+".shp"
    # Create a numpy array with an id field, and a field with a tuple 
    #  of x,y coordinates
    #
    array = numpy.array([(uid[0], (x[0], y[0]), x[0], y[0]),
                         (uid[1], (x[1], y[1]), x[1], y[1]),
                         (uid[2], (x[2], y[2]), x[2], y[2]),
                         (uid[3], (x[3], y[3]), x[3], y[3]),
                         (uid[0], (x[0], y[0]), x[0], y[0])],
                        numpy.dtype([('id',numpy.int32),('XY', '<f8', 2), ('point_x',numpy.float64), ('point_y',numpy.float64)]))
    arcpy.da.NumPyArrayToFeatureClass(array, outdir, ['XY'], sr)

        
