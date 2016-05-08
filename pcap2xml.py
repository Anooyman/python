#coding:utf-8
import sys
import sqlite3
import xml.etree.cElementTree as ET
import string 
reload(sys)
sys.setdefaultencoding('utf8')

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
        if not e.tail or not e.tail.strip():
            e.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i
    return elem

def makepacketnode(par, mdict):
    packet = ET.SubElement(par, "packet")
    for key in mdict:
        item = ET.SubElement(packet, key)
        item.text = mdict[key]
    return packet

if (__name__ == "__main__"):
    #filename = sys.argv[1]
    print 'Create database......'
    db = sqlite3.connect("PACKETS.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS packet")
    sql = """CREATE TABLE packet(
             Num INT,
             Src_ip CHAR(20),
             Src_port CHAR(5),
             Protocol CHAR(5),
             Dst_ip CHAR(20),
             Dst_port CHAR(5),
             Data_size INT,
             Timestamp CHAR(50),
             Packet_size INT)"""
    cursor.execute(sql)
    
    print 'Insert into database...... '
    num = 1
    DOMTree = ET.parse("com.ophone.MiniPlayer.pdml")
    collection = DOMTree.getroot()
    for elem in DOMTree.iter(tag='packet'):
        src_ip = ""
        src_port = ""
        protocol = ""
        dst_ip = ""
        dst_port = "" 
        data_size = 0 
        timestamp = "" 
        packet_size = 0 
        for item in elem.iterfind('proto[@name="geninfo"]'):
            packet_size = item.attrib["size"]
            for x in item.iterfind('field[@name="timestamp"]'):
              
                timestamp = x.attrib["show"]
               
            for item in elem.iterfind('proto[@name="ip"]'):
                string = item.attrib["showname"]
                s = string.find("Src:", 0)
                t = string.find(" (",0)
                src_ip = string[s+5:t]
                s = string.find("Dst:", t)
                t = string.find(" (",t+1)
                dst_ip = string[s+5:t]
            for item in elem.iterfind('proto[@name="tcp"]'):
                data_size = item.attrib["size"]
                string = item.attrib["showname"]
                s = string.find("Src Port:",0)
                t = string.find(" (",0)
                src_port = string[s+10:t]
                s = string.find("Dst Port:",t)
                t = string.find(" (",t+1)
                dst_port = string[s+10:t]
                protocol = "tcp"
            for item in elem.iterfind('proto[@name="udp"]'):
                data_size = item.attrib["size"]
                string = item.attrib["showname"]
                s = string.find("Src Port:",0)
                t = string.find(" (",0)
                src_port = string[s+10:t]
                s = string.find("Dst Port:",t)
                t = string.find(" (",t+1)
                dst_port = string[s+10:t]
                protocol = "udp"
            if(src_ip != "" and protocol != ""):
                sql = """INSERT INTO packet(
                         Num,Src_ip,Src_port,Protocol,Dst_ip,
                         Dst_port,Data_size,Timestamp,Packet_size)
                         VALUES("%d","%s","%s","%s","%s","%s","%d","%s",'%d')
                         """
                cursor.execute(sql%(int(num),src_ip,src_port,protocol,dst_ip, dst_port,int(data_size),timestamp,int(packet_size) ))
                num += 1
    print "select from database...... " 
    root = ET.Element("packetcollection")
    sql = "SELECT * FROM packet"
    results = cursor.execute(sql)
    for line in results:
       num = line[0]
       src_ip = line[1]
       src_port = line[2]
       protocol = line[3]
       dst_ip = line[4]
       dst_port = line[5]
       data_size = line[6]
       timestamp = line[7]
       packet_size = line[8]
       m = {"source_ip":src_ip, "source_port":src_port,
            "protocol":protocol, "destination_ip":dst_ip,
            "destination_port":dst_port,"data_size":str(data_size),
            "timestamp":timestamp, "packet_size":str(packet_size)}
       x = makepacketnode(root,m)
    tree = ET.ElementTree(root)
    file0 = open("new.xml","w")
    indent(root)
    tree.write(file0, "utf-8","True")
    file0.close()
    print "Create XML(new.xml)"

