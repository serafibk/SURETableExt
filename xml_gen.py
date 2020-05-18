import xml.etree.ElementTree as ET
import xml.dom.minidom
import json

#read in json file
with open("/Users/serafinakamp/Desktop/TableExt/datasheet-scrubber/src/Table_Extraction_Weight_Creation/getCoords/coords.json") as f:
    info = json.load(f);

# create the new table (generic outline)
data = ET.Element('document')
table = ET.SubElement(data,'table')
xMin = str(info["table"][0]["minX"])
yMin = str(info["table"][0]["minY"])
xMax = str(info["table"][0]["maxX"])
yMax = str(info["table"][0]["maxY"])
table_outline = ET.SubElement(table,'Coords',points=
xMin+","+yMin+" "+xMin+","+yMax+" "+xMax+","+yMax+" "+xMax+","+yMin)
# rest of the cells
for n in range(1,len(info["table"])):
    xMin = str(info["table"][n]["minX"])
    yMin = str(info["table"][n]["minY"])
    xMax = str(info["table"][n]["maxX"])
    yMax = str(info["table"][n]["maxY"])
    cell = ET.SubElement(table,'cell',start_row=str(n),start_col=str(n),end_row=str(n),end_col=str(n))
    coords = ET.SubElement(cell,'Coords',points=xMin+","+yMin+" "+xMin+","+yMax+" "+xMax+","+yMax+" "+xMax+","+yMin)

#write to xml file
#table = ET.ElementTree(data)
table = ET.tostring(data)
tablePretty = xml.dom.minidom.parseString(table).toprettyxml(indent="  ")
with open("modern_xml/from_modern99TEST.xml","w") as f:
    f.write(tablePretty)
