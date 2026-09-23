from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 
from utils.parse_feed import parseRssText

load_dotenv()

class ArxivService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ['ARXIV_BASE_URL'])

    def _handleError(self, e):
        print("Error", e)
        return {
            "status": "error",
            "message": str(e)
        }
    def searchForPapers(self, topic: str):
        try:
            qpParams = {
                "search_query": f"all:{topic}",
                "start": 0,
                "max_results": 3
            }
            response = self.client.getCall("query", qpParams = qpParams)
            feedObj =  parseRssText(response)
            feed = feedObj.feed 
            return feed 
            
        except Exception as e:
            return self._handleError(e)
