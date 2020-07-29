# Hey I'm Jacob 👋
[![Twitter Follow](https://img.shields.io/twitter/follow/{{ twitter_username }}?style=social)](https://twitter.com/{{ twitter_username }})

## Blog

Check out my latest blog posts.

{% for post in latest_blog_posts -%}
- [{{ post.title }}]({{ post.link }}) - *{{post.published.strftime("%a, %d %b %Y") }}*
{% endfor %}