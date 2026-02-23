# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "feedparser",
#     "jinja2",
#     "pyyaml",
# ]
# ///
import jinja2
import yaml
import feedparser
from datetime import datetime

# Set up templates
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template("TEMPLATE.md")

# Load config
with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# Get latest blog post
blog_rss = feedparser.parse("https://jacobtomlinson.dev/posts/feed.xml")
config["latest_blog_posts"] = blog_rss["entries"][0:5]
for post in config["latest_blog_posts"]:
    post["published"] = datetime.strptime(post["published"], "%a, %d %b %Y %H:%M:%S %z")

# Render remplate
print(template.render(**config))
