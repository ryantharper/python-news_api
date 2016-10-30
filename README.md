# Simple Python Wrapper for newsapi.org

Use:
  - `news = news_api.load_news(api_key_news, source, sortBy, numberOfArticles)`
  - `titles = news.titles() # Only get titles, in list`
  - `titles_and_desc = news.titles_desc() # Get titles and descriptions, in dictionary {"title":"description"}`
  - `desc = news.desc() # Only get descriptions, in list`
  - `link = news.link() # Only get article URL, in list`
  - `titles_and_link = news.titles_url() # Get titles and links, in dictionary {"title":"url"}`
  
List of sources that can be used can be found at https://newsapi.org/sources
  - To use default source, use `None`. Default source is `bbc-news`

SortBy: `"top"|"latest"|"popular"`, to use default, use `None`. Some news sources do not sort by latest/popular.

Most of the time `numberOfArticles` goes up to 10. 

## To Do:
  - If numberOfArticles too large, show max amount of articles
  

