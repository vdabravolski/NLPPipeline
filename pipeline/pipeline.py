from nltk import data
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
import nltk

#General todo:
# 1. implement de-indentifications
#2. understand how the text processing can be trained.


class NLPPipeline:
    def __init__(self):
        # placeholder
        self. cl =""
        self. sent=[]
        self.non_nrml_words=[] # todo: need to implement sort of structure with normalized and non-normalized word. for now let's go with just normalized words
        self.nrml_words=[]

        self.stemmer = PorterStemmer()

    # todo: to be removed
    # self.tokenizer=data.load("tokenizers/punkt/english.pickle")

    def process(self, cl):
        # prepare the processing
        self.cl =cl

        #apply the default NLP pipeline sequence
        self.__boundary_detection__()
        self.__tokenization__()
        self.__normalization__()

    def __boundary_detection__(self):
        print self.cl
        self.sent = sent_tokenize(self.cl)

    def __tokenization__(self):
        for sentence in self.sent:
            self.non_nrml_words=word_tokenize(sentence)

        nltk.Text()

    def __normalization__(self):
        self.nrml_words= [self.stemmer.stem(word) for word in self.non_nrml_words]

    def __pos_tagger__(self):
        print "placeholder"

    def __shallow_parser__(self):
        print "placeholder"

    def __ner__(self):
        print "placeholder"




test_cl="Fx of obesity but no fx of coronary artery diseases. " \
        "Followup dietary consultation for hyperlipidemia, " \
        "hypertension, and possible metabolic syndrome."

x= NLPPipeline();
x.process(test_cl)
print x.non_nrml_words
print x.nrml_words
