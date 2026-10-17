class Solution:
    def kthCharacter(self, k: int) -> str:
        word='a'
        while len(word)<k:
            new_word=""
            for i in word:
                new_word+=chr((ord(i)-ord('a')+1) %26+ord('a'))
            word += new_word
        count=0
        for i in word:
            count+=1
            if count==k:
                return i