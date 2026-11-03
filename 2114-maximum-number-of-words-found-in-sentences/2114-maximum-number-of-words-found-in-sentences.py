class Solution(object):
    def mostWordsFound(self, sentences):
        i=0
        sen2 = 0
        while i<len(sentences):
            sen1 = sentences[i].split()
            result = len(sen1)
            sen2 = max(result,sen2)
            i+=1
        
        return sen2