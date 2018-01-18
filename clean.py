import nltk
from nltk.corpus import stopwords
import string
import re



class process:
    
    # remove non ascii characters
    def remove_non_ascii(self, text):
        return ''.join([i if ord(i) < 128 else '' for i in text])
        
        # remove stopwords, puntuations and clean the input
    def cleanup_news(self, s):
        stop = set(stopwords.words('english'))
        puntuations = list(string.punctuation)
        tokens = [i for i in nltk.word_tokenize(re.sub(r'\d+', '', s.lower())) if i not in puntuations]
        cleanup = " ".join(filter(lambda words: words not in stop, tokens))
        cleanup = re.sub(r'http[s]?', '', cleanup, flags=re.MULTILINE)
        cleanup = re.sub(r'//.*', '', cleanup, flags=re.MULTILINE)
        cleanup = re.sub(r'.*[com]/.*', '', cleanup, flags=re.MULTILINE)
        cleanup = cleanup.replace('...','')
        cleanup = cleanup.replace("''",'')
        cleanup = cleanup.replace("'s",'')
        cleanup = cleanup.replace('-','')
        cleanup = cleanup.replace("'",'')
        cleanup = cleanup.replace('#','')
        cleanup = cleanup.replace('|','')
        return cleanup

        # obtain a list of tokenized words (after removing stopwords and puntuations) from title
    def clean_news(self, s):
        return nltk.word_tokenize(self.cleanup_news(s))



