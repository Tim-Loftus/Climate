import arcpy
import os
import glob

#Set model paths and extent 
shpworkspace = r"W:\\WeatherData\\Normals\\Daily_Files\\"
outworkspace = r"W:\\WeatherData\\Normals\\Raster_Files\\"
Extent = "-13885188.4222 2870387.3962 -7454985.1465 6338173.2201"
arcpy.env.overwriteOutput= True

# Iterate through csv files in a folder
try:
# Create shapefiles
    arcpy.env.workspace = shpworkspace
    path = "W:\\WeatherData\\Normals\\Daily_Files\\*.csv"
    for csvfile in list(glob.glob(path)):
        print csvfile
        outlayer = os.path.splitext(csvfile)[0]+ ".shp"
        sr = arcpy.SpatialReference("WGS 1984")
        arcpy.MakeXYEventLayer_management(csvfile, "LON", "LAT", outlayer, sr, "")
        savedshp = os.path.splitext(outlayer)[0]+"_2017.shp"
        arcpy.CopyFeatures_management(outlayer,savedshp)
        print savedshp
        
except:
    # If an error occurred print the message to the screen
    arcpy.AddError("This is not working")
    print "This is not working"
    print arcpy.GetMessages()
 
        
