import meduza
url = "https://meduza.io/en/brief/"

article = meduza.get(url)
for article in meduza.section('news', n=10, lang='ru'):
    print(f" - '{article['title']}'")
    