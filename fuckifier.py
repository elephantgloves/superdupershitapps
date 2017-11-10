import numpy as np
import nltk
import random
"""A really, really shit program just to test the nltk tagging facility
Will add fucks to your sentences so that you don't have to give any.
"""

class stringParser():
    
    numberofwords=0
    """
Ignore: CC, DT, LS, MD, PDT, POS, TO, IN
    ing: CD, EX, PRP$, UH, WDT, WP, WP$, WRB
    ing/ingest: NN, PRP, NNPS, NNP, FW, SYM
    ing/ingly: VB, VBD, VBG, VBN, VBP, VBZ, RB, RBR, RBS, JJ, JJR, JJS
    """
    
    ignorelist=["CC", "IN", "DT", "LS", "MD", "PDT", "POS", "TO", "PRP"]
    ing=["CD", "EX", "PRP$", "UH", "WDT", "WP", "WP$", "WRB"]
    ingest=["NN", "NNPS", "NNP", "FW", "SYM"]
    ingly=["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "RB", "RBR", "RBS", "JJ", "JJR", "JJS"]
    
    
    def getWordsInOrder(self, inputstring):                
        wordsInOrdertuple=tuple(inputstring.split(" "))
        self.numberofwords=np.size(wordsInOrdertuple)   
        return wordsInOrdertuple
    
    def parsemywords(self, inputstring):
        mywords=inputstring.split(" ")
        taggedlist=nltk.pos_tag(mywords)
        self.numberofwords=len(taggedlist)
        return taggedlist
    


class fingStringParser(stringParser):
    
    maxnumberofFs=0
    prefedlist=[]
    fedlist=[]
    
    def setmaxnumberofFs(self):
        self.maxnumberofFs=self.numberofwords
        
    def fstoadd(self):
        nroffs=np.random.randint(1, high=self.maxnumberofFs+1)
        print "Max number of fucks given this time: ", nroffs
        return nroffs
    
    def setprefedlist(self, mylist):
        self.prefedlist=mylist
    
    def getfindices(self):
        indexarray=np.arange(len(self.prefedlist))
        random.shuffle(indexarray)
        nrofFs=self.fstoadd()
        indexlist=sorted(indexarray[:nrofFs])
        return indexlist
        
    def fuckify(self, indexlist):
        #print indexlist
        #print self.prefedlist
        counter=0
        
        for i in self.prefedlist:
            if counter in indexlist:
                if self.prefedlist[counter][1] in self.ing:
                    self.fedlist.append("fucking "+self.prefedlist[counter][0])
                elif self.prefedlist[counter][1] in self.ingest:
                    if np.random.randint(0, high=20)>7: self.fedlist.append("fuckingest "+self.prefedlist[counter][0])
                    else: self.fedlist.append("fucking "+self.prefedlist[counter][0] )
                elif self.prefedlist[counter][1] in self.ingly:
                    if np.random.randint(0, high=20)>7: self.fedlist.append("fuckingly "+self.prefedlist[counter][0])
                    else: self.fedlist.append( "fucking "+self.prefedlist[counter][0] )
                elif self.prefedlist[counter][1] in self.ignorelist:
                    self.fedlist.append(self.prefedlist[counter][0])
            else:
                self.fedlist.append(self.prefedlist[counter][0])
            
            counter=counter+1
             
    def getFuckifiedString(self):
        return " ".join(self.fedlist)        

        
    def __init__(self, inputstring):
        self.setprefedlist(self.parsemywords(inputstring))
        self.setmaxnumberofFs()
        

myfparser=fingStringParser("hello, you sexy onerous beast full of everything good")
myfparser.fuckify(myfparser.getfindices())
print myfparser.getFuckifiedString()

