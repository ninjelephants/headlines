import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {"lanwan", "http://www.networkworld.com/category/lan-wan/index.rss",
             "datacenter", "http://www.networkworld.com/category/data-center/index.rss",
             "cisco", "http://www.networkworld.com/category/cisco-subnet/index.rss",
             "slashdot", "http://rss.slashdot.org/Slashdot/slashdotMain",
             "packetpushers", "http://feeds.packetpushers.net/packetpushersfatpipe",
            }



@app.route("/<publication>")
def get_news(publication = "lanwan"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1>Headlines </h1>
            <b>{0}<br/>
            <i>{1}</i><br/>
            <p>{2}</p><br/>
        </body>
        </html""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))


if __name__ == '__main__':
    app.run(port = 5000, debug = True)
