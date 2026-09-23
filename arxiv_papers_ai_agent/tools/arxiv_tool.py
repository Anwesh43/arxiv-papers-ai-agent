from services.arxiv_service import ArxivService 

arxivService = ArxivService()

def searchForPapers(query : str):
    print(f"Calling searchForPapers for {query}")
    return arxivService.searchForPapers(query)

def writeHTML(htmlStr : str, fileName : str):
    print(f"Calling writeHTML tool for {fileName}")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": "success",
        "message": f"Written html to {fileName}, don't display html to user"
    }