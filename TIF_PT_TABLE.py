# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
import os

# Set environment settings
env.workspace = r"W:\\WeatherData\\Normals\\Raster_Files"
env.overwriteOutput= True
print str("Environment Set")

#Set local variables
outworkspace = r"W:\WeatherData\Normals\DBF_Files"
print str("Local variables set")

#Iterate through rasters
for tifFile in arcpy.ListFiles("*.tif"):
    tifFileName = os.path.splitext(tifFile)[0]
    print tifFileName
    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print str("Spatial Extension")
    outPoints = os.path.join(outworkspace, tifFileName + ".shp")
    inPoints = r"W:\\SNODAS\\UFDB_US48.shp"
    #Execute ExtractValuesToPoints
    ExtractValuesToPoints(inPoints, tifFile, outPoints, "NONE", "VALUE_ONLY")
    print outPoints
    # Define field name and expression
    field = "FILENAME"
    expression = str(tifFileName) #populates field   
    # Create a new field with a new name
    arcpy.AddField_management(outPoints,field,"TEXT")
    # Calculate field here
    arcpy.CalculateField_management(outPoints, field, '"'+expression+'"', "PYTHON")
    print outPoints
    print str("Success")
    


