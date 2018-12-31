import numpy as np
import nltk
nltk.download('averaged_perceptron_tagger')
import random


"""
Ignore: CC, DT, LS, MD, PDT, POS, TO, IN
    ing: CD, EX, PRP$, UH, WDT, WP, WP$, WRB
    ing/ingest: NN, PRP, NNPS, NNP, FW, SYM
    ing/ingly: VB, VBD, VBG, VBN, VBP, VBZ, RB, RBR, RBS, JJ, JJR, JJS
"""

endings = {
    'ignorelist': ["CC", "IN", "DT", "LS", "MD", "PDT", "POS", "TO", "PRP"],
    'ing': ["CD", "EX", "PRP$", "UH", "WDT", "WP", "WP$", "WRB"],
    'ingest': ["NN", "NNPS", "NNP", "FW", "SYM"],
    'ingly': ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "RB", "RBR", "RBS", "JJ", "JJR", "JJS"]

}

class theFuckifier():
    """
    Will add fucks to your sentences so that you don't have to give any.
    """

    endings_dict = None
    max_fucks_given = 0

    def __init__(self, endings_dict=endings_dict, max_fucks_given=10):

        self.endings_dict = endings
        self.max_fucks_given = max_fucks_given

    def parse_and_pos_tag(self, input_string, reset_max_fucks=True):
        pos_tagged_list = nltk.pos_tag(input_string.split(" "))

        if reset_max_fucks == True:
            self.set_max_fucks(max_fucks_given=len(pos_tagged_list))

        return pos_tagged_list


    def fuckify_string(self, input_string, fucks_to_give=10, fuck_indexes=None):

        pos_tagged_list = self.parse_and_pos_tag(input_string)

        if fuck_indexes == None:
            fuck_indexes = self.calculate_fuck_insert_indexes(pos_tagged_list, number_of_fucks=fucks_to_give)

        fucked_list = []

        for i in range(len(pos_tagged_list)):
            word = pos_tagged_list[i][0]
            tag = pos_tagged_list[i][1]

            if i in fuck_indexes:
                if tag in self.endings_dict["ing"]:
                    fucked_list.append("fucking " + word)
                elif tag in self.endings_dict["ingest"]:
                    if np.random.randint(0, high=20) > 7:
                        fucked_list.append("fuckingest " + word)
                    else:
                        fucked_list.append("fucking " + word)
                elif tag in self.endings_dict["ingly"]:
                    if np.random.randint(0, high=20) > 7:
                        fucked_list.append("fuckingly " + word)
                    else:
                        fucked_list.append("fucking " + word)
                elif tag in self.endings_dict["ignorelist"]:
                    fucked_list.append(word)
            else:
                fucked_list.append(word)

        return " ".join(fucked_list)

    def set_max_fucks(self, max_fucks_given=0):
        self.max_fucks_given = max_fucks_given

    def calculate_fucks_given(self, max_fucks=1):
        return np.random.randint(1, high=(max_fucks+1))

    def calculate_fuck_insert_indexes(self, taggedlist, number_of_fucks=0):
        fuck_indexes = np.arange(len(taggedlist))
        random.shuffle(fuck_indexes)

        if number_of_fucks == 0:
            number_of_fucks = self.calculate_fucks_given(self.max_fucks_given)
        else:
            number_of_fucks = self.calculate_fucks_given(number_of_fucks)

        return sorted(fuck_indexes[:number_of_fucks])
