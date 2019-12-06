import os
import nltk

from nltk.corpus import wordnet as wn, words as w

class Dictionary():

    def load_dictionary(self, dictionary_dir=None):
        pass

    def __init__(self):
        self.w = set(w.words())

    def word_definition(self, word):
        definition = None
        try:
            return wn.synsets(word)[0].definition()
        except:
            print('Word lookup failed')
            return definition

    def word_exists(self,word):
        return word in self.w


