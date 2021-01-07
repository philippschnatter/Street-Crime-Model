import arcpy
import os
from arcpy import env

# Routen-Layer erstellen
# https://desktop.arcgis.com/de/arcmap/10.3/tools/network-analyst-toolbox/make-route-layer.htm

try:
    #Check out the Network Analyst extension license
    arcpy.CheckOutExtension("Network")
        
    # execfile("CreatePathLayers.py")
    #Set environment settings
    env.workspace = "C:/ESRIPress/Maputo IMPOSM SHP/project2/07_create_activity_paths/Maputo.gdb"
    env.overwriteOutput = True
        
    #Set local variables
    inNetworkDataset = "Maputo/Maputo_ND"
    impedanceAttribute = "Length"
    outNALayerName = "BestRoute"
    searchTolerance = "5000 Meters"
    
    for agent in range(0, 1000, 1):

        outStops = "C:/ESRIPress/Maputo IMPOSM SHP/project2/07_create_activity_paths/FC2021/aShape" + str(agent) + ".shp" #hier shapefiles
        outLayerFile = "C:/ESRIPress/Maputo IMPOSM SHP/project2/07_create_activity_paths/layers2021" + "/" + "a" + str(agent) + "route" + ".lyr" #output
     
        #Create a new Route layer. For this scenario, the default value for all the
        #remaining parameters statisfies the analysis requirements
        outNALayer = arcpy.na.MakeRouteLayer(inNetworkDataset, outNALayerName, impedanceAttribute)
        
        #Get the layer object from the result object. The route layer can now be
        #referenced using the layer object.
        outNALayer = outNALayer.getOutput(0)

        #Get the names of all the sublayers within the route layer.
        #subLayerNames = arcpy.na.GetNAClassNames(outNALayer)
        #Stores the layer names that we will use later
        #stopsLayerName = subLayerNames["Stops"]
        #candidateFields = arcpy.ListFields(outNALayer)
        #fieldMappings = arcpy.na.NAClassFieldMappings(outNALayer, "Route", True, candidateFields)
        fieldMappings = arcpy.na.NAClassFieldMappings(outNALayer, "Stops")
        arcpy.na.AddLocations(outNALayer, "Stops", outStops, fieldMappings,
                              searchTolerance, exclude_restricted_elements = "EXCLUDE")
        
        #Solve the route layer, ignore any invalid locations such as those that
        #can not be geocoded
        arcpy.na.Solve(outNALayer,"SKIP", "CONTINUE")
        
        #Save the solved route layer as a layer file on disk with relative paths
        arcpy.management.SaveToLayerFile(outNALayer,outLayerFile, "RELATIVE")
    
    print "Script completed successfully"


except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print "An error occured on line %i" % tb.tb_lineno
    print str(e)
