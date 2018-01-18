from bs4 import BeautifulSoup
import string
import requests
import clean

process = clean.process()

class NewsScrape:

    

    twitter_root = 'https://www.twitter.com/'

    def __init__(self):
       # punctuations = set(string.punctuation)
       # self.query = ''.join([i for i in query if i not in punctuations])
        self.root = 'https://www.twitter.com/'
        self.maximum = self.max_links()

    def max_links(self):
        return 15
    
    def build_url(self, keyword):
        params = 'i/streams/category/687094923246440476'
        return keyword + params

    def retrieve_source(self, url):
        try:
            return BeautifulSoup(requests.get(url).content, \
                             'html.parser')
        except:
            print 'Unexpected error occured'

    def process_record(self, html):
        table = html.find_all('div', attrs={'class':'js-tweet-text-container'})
        for each in table:
            news = each.find('p')
            print news.text
            tokenized_news = process.clean_news(news.text)
            print tokenized_news
            print '###########################################'
            
        #print tokenized_news
        return tokenized_news
      

    def __iter__(self):
        
        print self.root
        raw_html = self.retrieve_source(self.build_url(self.root))
        yield self.process_record(raw_html)
