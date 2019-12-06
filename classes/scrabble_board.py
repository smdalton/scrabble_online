import random
#from PyDictionary import PyDictionary

class ScrabbleBoard():

    def __init__(self, *args, **kwargs):

        self.scrbl = "A-9-1, B-2-3, C-2-3, D-4-2,\
                        E-12-1, F-2-4, G-3-2, H-2-4,\
                        I-9-1, J-1-8, K-1-5, L-4-1,\
                        M-2-3, N-6-1, O-8-1, P-2-3,\
                        Q-1-10, R-6-1, S-4-1, T-6-1,\
                         U-4-1, V-2-4, W-2-4, X-1-8,\
                        Y-2-4, Z-1-10"
        self.reset_bag()

        #self.dictionary=PyDictionary()

    def reset_bag(self):
        self.letter_dict =  dict([((ltrs.split('-')[0], \
                            int(ltrs.split('-')[1]))) \
                            for ltrs in \
                            self.scrbl.replace(' ', '').split(',')])

        self.score_dict  =  dict([((ltrs.split('-')[0], \
                            int(ltrs.split('-')[2]))) \
                            for ltrs in \
                            self.scrbl.replace(' ', '').split(',')])

        # create the bag
        self.bag = []
        for key, value in self.letter_dict.items():
            [self.bag.append(key) for i in range(value)]
            random.shuffle(self.bag)
            self.tile_sum = ''

    # def translate_word(self, word=None):
    #     language_code = 'vi'
    #     return self.dictionary.translate(word, language_code)

    def get_hand(self, num_tiles):
        # pop 7 tiles off of the bag
        if num_tiles >7:
             return -1

        if len(self.bag) < num_tiles:
            result = [ x for x in self.bag]
            return result
        else:
            return [self.bag.pop() for i in range(num_tiles)]

    # def word_is_valid(self, word):
    #     try:
    #         if self.dictionary.meaning(word):
    #             return True
    #         else:
    #             return False
    #     except:
    #         return False

    def get_bag(self):
        # returns the current bag
        return self.bag

    def game_over(self):
        # tallies scores and declares a winner
        pass

