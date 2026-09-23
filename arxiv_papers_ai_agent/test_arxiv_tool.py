from tools.arxiv_tool import searchForPapers
from typing import Dict 
import json 

def writeFile(data : Dict, fileName : str):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"writing data string to {fileName}")
if __name__ == "__main__":
    searchData = searchForPapers("LLM")
    #print(searchData)
    writeFile(searchData.model_dump(), "test_search.json")