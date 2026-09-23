from rss_parser import parse 

def parseRssText(xml : str):
    return parse(xml)

def getXMLFileContent(fileName : str):
    fileNameStr = ""
    with open(fileName, "r") as f:
        fileNameStr = f.read()
    return fileNameStr