import xml.etree.ElementTree as ET
import xml.dom.minidom
import json

#create new xml doc
data = ET.Element('document')

i=0

#read in json file
while(1):
    try:
        with open("/Users/serafinakamp/Desktop/TableExt/datasheet-scrubber/src/Table_Extraction_Weight_Creation/getCoords/coords"+str(i)+".json") as f:
            info = json.load(f)

        # create the new table
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
        i=i+1
    except:
        print("done reading tables")
        break
#write to xml file
#table = ET.ElementTree(data)
table = ET.tostring(data)
tablePretty = xml.dom.minidom.parseString(table).toprettyxml(indent="  ")
with open("xml_train/train_NUM.xml","w") as f:
    f.write(tablePretty)
