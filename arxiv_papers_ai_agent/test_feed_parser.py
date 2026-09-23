from utils.parse_feed import parseRssText, getXMLFileContent
import time 

if __name__ == "__main__":
    xmlContent = getXMLFileContent("test_feed.xml")
    feed = parseRssText(xml=xmlContent)
    print(feed.feed.id)
    print(feed.feed.title)
    print("AAUTHORS", feed.feed.content.authors)
    
    for entry in feed.feed.entries:
        print("____ENTRY____", entry.content.__dict__.keys())
        print(entry.id)
        print(entry.title)
        print(entry.authors)
        print(entry.summary)
    


# ['id', 'title', 'updated', 'authors', 'links', 'content', 'summary', 'categories', 'contributors', 'rights', 'published', 'source'
