import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag, ne_chunk
from textblob import TextBlob

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def tokens(self, text):
        cleantext = []
        tokens = word_tokenize(text)
        for text in tokens:
            cleantext.append(text)

        return cleantext

    def clean_data(self, text):
        stop_words = set(stopwords.words('english'))
        cleantext = []
        for i in text:
            if i not in stop_words:
                cleantext.append(i)
        return cleantext

    def lemmatizer(self, text):
        cleantext = []
        lemma = WordNetLemmatizer()
        print(text)
        text=word_tokenize(text)
        for word in text:
              print(lemma.lemmatize(word))

    def ner(self, text):
        print(ne_chunk(pos_tag(word_tokenize(text))))

    def pos(self, text):
        result = TextBlob(text)
        print(result.tags)



ob=TextProcessing("sundar pichae is the CEO of GOOGLE company")
tokens = ob.tokens(ob.text)
stop_word = ob.clean_data(tokens)
stop_word=' '.join(stop_word)
#lemma = ob.lemmatizer(str(stop_word))
ob.ner(stop_word)
ob.pos(stop_word)

input_str = "Bill works for Apple so he went to Boston for a conference."

