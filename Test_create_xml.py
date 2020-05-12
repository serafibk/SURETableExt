from xml.dom.minidom import Document

class XmlCreator:

    def __init__(self,txtpath,xmlpath):
        self.txtPath = txtpath
        self.xmlPath = xmlpath
        self.txtList = []
    
    def readtxt(self):
        txtfile = open(self.txtPath,"r",encoding='UTF-8',errors='ignore')
        self.txtList = txtfile.readlines()
        for i in self.txtList:
            oneline = i.strip().split(" ")
        print(self.txtList)

    def makexml(self):
        doc = Document()
        orderdoc = doc.createElement("document")
        orderdoc.setAttribute("filename", "test")
        doc.appendChild(orderdoc)
        orderpack = doc.createElement("table")
        orderdoc.appendChild(orderpack)
        objecname1 = "Coords"
        objecname2 = "cell"
        count = 0;
        for i in self.txtList:
            if(count == 0):
                oneline = i.strip().split(" ")
                objectE = doc.createElement(objecname1)
                objectE.setAttribute("points",oneline[0] + ","+ oneline[1] + " " 
                                            + oneline[2] + ","+ oneline[3] + " " 
                                            + oneline[4] + ","+ oneline[5] + " " 
                                            + oneline[6] + ","+ oneline[7] + " ")
                orderpack.appendChild(objectE)
                count += 1
            elif(count == 1):
                #print("test!!1")
                oneline = i.strip().split(" ")
                object_cell = doc.createElement(objecname2)
                object_cell.setAttribute("start-row", oneline[0])
                object_cell.setAttribute("start-col", oneline[1]) 
                object_cell.setAttribute("end-row", oneline[2])
                object_cell.setAttribute("end-col", oneline[3]) 

                object_coords = doc.createElement(objecname1)
                object_coords.setAttribute("points",oneline[4] + ","+ oneline[5] + " " 
                                            + oneline[6] + ","+ oneline[7] + " " 
                                            + oneline[8] + ","+ oneline[9] + " " 
                                            + oneline[10] + ","+ oneline[11] + " ")
                object_cell.appendChild(object_coords)

                orderpack.appendChild(object_cell)

        f = open(self.xmlPath, 'w')
        doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='UTF-8')
        f.close()


if __name__ == "__main__":
    read =XmlCreator("/Users/Renee/Desktop/research/Data Scrubber/test.txt", "/Users/Renee/Desktop/research/Data Scrubber/test.xml")
    read.readtxt()
    read.makexml()
    print(read.txtPath)
    for i in read.txtList:
        print(i)
