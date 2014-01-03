import feedparser
import json

def main():
    srcList = loadSource()
    for key in srcList:
        crawl(key, srcList[key]['link'])

def loadSource():
    with open("source.json") as src:
        return json.load(src)

def crawl(src, rss):
    feed = feedparser.parse(rss)
    for entry in feed.entries:
        print entry.title
        print entry.published
        print entry.link

if __name__ == "__main__":
    main()