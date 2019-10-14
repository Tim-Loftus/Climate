* Encoding: windows-1252.
SORT CASES BY Station_Code Date.
EXECUTE.

COMPUTE Snow_Depth_Lag = LAG(Snow_Depth_Inches).
EXECUTE.

STRING lag_station (A254).
COMPUTE lag_station = LAG(Station_Code).
EXECUTE.

COMPUTE Snow_Accumulation=0.
IF lag_station = Station_Code Snow_Accumulation= Snow_Depth_Inches-Snow_Depth_Lag. 
EXECUTE.

COMPUTE Snow_Melt =0. 
IF lag_station = Station_Code AND Snow_Accumulation LE 0 Snow_Melt = Snow_Accumulation.
EXECUTE.

COMPUTE Snow_Accum=0.
IF Snow_Accumulation GE 0 Snow_Accum=Snow_Accumulation.
EXECUTE.

COMPUTE Snow_Melt = ABS(Snow_Melt).
EXECUTE.

STRING Date (A11). 
COMPUTE Date = filename. 
EXECUTE.

COMPUTE Date=REPLACE(Date,"_","/").
EXECUTE.

COMPUTE Date=REPLACE(Date,"APR","04").
COMPUTE Date=REPLACE(Date,"MAR","03").
COMPUTE Date=REPLACE(Date,"JUN","06").
COMPUTE Date=REPLACE(Date,"MAY","05").
COMPUTE Date=REPLACE(Date,"JUL","07").
COMPUTE Date=REPLACE(Date,"AUG","08").
COMPUTE Date=REPLACE(Date,"SEP","09").
COMPUTE Date=REPLACE(Date,"OCT","10").
COMPUTE Date=REPLACE(Date,"NOV","11").
COMPUTE Date=REPLACE(Date,"DEC","12").
COMPUTE Date=REPLACE(Date,"JAN","01").
COMPUTE Date=REPLACE(Date,"FEB","02").
EXECUTE.

STRING VAR (A1). 
COMPUTE VAR = CHAR.SUBSTR(filename, 12,1).
EXECUTE.

STRING VARNAME (A10).
COMPUTE VARNAME ="0".
IF VAR = "H" VARNAME ="Norm_High".
IF VAR = "W" VARNAME ="Norm_Water".
EXECUTE.

FREQUENCIES VARNAME.

SORT CASES BY Station_Code Date_New. 
EXECUTE.

COMPUTE Norm_High2=RND(Norm_High).
EXECUTE.
COMPUTE Norm_Water2=RND(Norm_Water,0.01).
EXECUTE.



