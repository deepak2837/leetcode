class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            index = word.index(ch)
            
        
            front = word[:index][::-1]
            back = word[index+1:]
            return ch+front+back 
        except:
            return word
        