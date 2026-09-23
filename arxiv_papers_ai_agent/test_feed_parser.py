from utils.parse_feed import parseRssText, getXMLFileContent
import time 

if __name__ == "__main__":
    xmlContent = getXMLFileContent("test_feed.xml")
    feed = parseRssText(xml=xmlContent)
    print(feed.feed.id)
    print(feed.feed.title)
    print("AAUTHORS", feed.feed.content.authors)
    
    for entry in feed.feed.entries:
        # print("____ENTRY____", entry.content.__dict__.keys())
        print(entry.id)
        print(entry.title)
        names = []
        # for author in entry.authors:
        #     print(author.name)
        #     #print(author.email)
        print(entry.summary)
        for link in entry.links:
            
            print(link.attributes['href'])
            print(link.attributes['type'])
        print(str(entry.published), type(str(entry.published)))
        for category in entry.categories:
            print(category.__dict__)
    


# ['id', 'title', 'updated', 'authors', 'links', 'content', 'summary', 'categories', 'contributors', 'rights', 'published', 'source'
