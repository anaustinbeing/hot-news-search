from getnews import NewsScrape


news = []

if __name__ == "__main__":

    tweets = NewsScrape()
    for tweet in tweets:
        if not tweet:
            pass
        else:
            news = tweet

    print news
            
