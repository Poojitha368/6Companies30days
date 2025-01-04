class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        n = len(secret)
        count = {}
        for char in secret:
            if char in count:
                count[char]+=1
            else:
                count[char]=1   
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
                count[guess[i]] -= 1 
        for i in range(n):
            if secret[i] != guess[i] and guess[i] in count and count[guess[i]] > 0:
                cows += 1
                count[guess[i]] -= 1 
        return f"{bulls}A{cows}B"
