from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 
from utils.parse_feed import parseRssText
from models.arxiv_search_result import ArxivSearchEntry, ArxivSearchResult

load_dotenv()

class ArxivService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ['ARXIV_BASE_URL'])

    def _handleError(self, e):
        #print("Error", e)
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
            entries = []
            for entry in feed.entries:
                authorNames = []
                for author in entry.authors:
                    #print(author.name)
                    authorNames.append(author.name.content)
                print("AuthorNames", authorNames)
                pdfLink = ''
                for link in entry.links:
                    if link.attributes['type'] == 'application/pdf':
                        pdfLink = link.attributes['href']
                        break 
                searchEntry = ArxivSearchEntry(id = entry.id.content, title = entry.title.content, authors = authorNames, summary = entry.summary.content, pdfLink=pdfLink, published=str(entry.published))
                entries.append(searchEntry)
            return ArxivSearchResult(entries=entries, id = feed.id.content, title = feed.title.content)
        except Exception as e:
            return self._handleError(e)
