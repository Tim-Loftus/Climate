import arcpy
import os
import glob

#Set model paths and extent 
shpworkspace = r"W:\\WeatherData\\Normals\\Daily_Files\\"
outworkspace = r"W:\\WeatherData\\Normals\\Raster_Files"
arcpy.env.overwriteOutput= True


#Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("GeoStats")
print "Geo Extension"

# Iterate through csv files in a folder
try:
# Create shapefiles
    arcpy.env.workspace = shpworkspace
    path = r"W:\\WeatherData\\Normals\\Daily_Files\\*.shp"
    for fc in list(glob.glob(path)):
        print fc
# Create rasters
        arcpy.env.extent = r"W:\\WeatherData\\Normals\\UFDB_US48.shp"
        outraster = os.path.join(outworkspace,(os.path.splitext(os.path.basename(fc))[0]+ "W.tif"))
        #Set local variables
        zField ="NORM_WATER"
        outgeo =""
        cellsize = 0.113778974686552
        power = 1
        kernelFunction = "EXPONENTIAL"
        bandwidth = ""
        useConNumber = ""
        conNumber = ""
        weightField= ""
        outSurface = "PREDICTION"
        #Set variables for search neighborhood
        majSemiaxis = 15.34321700703604
        minSemiaxis = 15.34321700703604
        angle = 0
        smoothFactor = 0.2
        searchNeighborhood = arcpy.SearchNeighborhoodSmooth(majSemiaxis, minSemiaxis, angle, smoothFactor)
        print "Begin Interpolation"
        arcpy.LocalPolynomialInterpolation_ga(fc, zField, outgeo, outraster, cellsize, power, searchNeighborhood, kernelFunction, bandwidth, useConNumber, conNumber, weightField, outSurface)
        print outraster
        
except:
    # If an error occurred print the message to the screen
    arcpy.AddError("This is not working")
    print "This is not working"
    print arcpy.GetMessages()
 
        
