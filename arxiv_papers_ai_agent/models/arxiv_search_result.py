from pydantic import BaseModel
from typing import List 

class ArxivSearchEntry(BaseModel):
    id : str 
    title: str 
    authors: List[str]
    summary: str 
    pdfLink : str 
    published: str

class ArxivSearchResult(BaseModel):
    id : str 
    title : str 
    entries : List[ArxivSearchEntry]

# ['id', 'title', 'updated', 'authors', 'links', 'content', 'summary', 'categories', 'contributors', 'rights', 'published', 'source'
