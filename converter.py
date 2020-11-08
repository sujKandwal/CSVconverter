import csv
import pandas 

#Gets the CSV file via Pandas and detects the header of the columns
col_list = ["No.", 'PosX', "PosY", "PosZ", "Rx", "Ry", "Rz", "DWNx", "DWNy", "DWNz", "Lx", "Ly", "Lz"]
allCols = pandas.read_csv("rmc.csv", usecols = col_list)

#Each variable is assigned to the corresponding column list
number = allCols["No."]
posx = allCols["PosX"]
posy =  allCols["PosY"]
posz = allCols["PosZ"]
rx = allCols["Rx"]
ry = allCols["Ry"]
rz = allCols["Rz"]
dwnx = allCols["DWNx"]
dwny = allCols["DWNy"]
dwnz = allCols["DWNz"]
lx = allCols["Lx"]
ly = allCols["Ly"]
lz = allCols["Lz"]
