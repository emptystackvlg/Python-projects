import feedparser

NewsFeed = feedparser.parse("https://4pda.ru/feed/")

for i in range(0,(len(NewsFeed.entries))):
    entry = NewsFeed.entries[i]
    print (entry.title + ":\n"  + entry.link + "\n\n\n")
    i += 1
