# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = []
        self.expirationTime = []
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens.append(tokenId)
        self.expirationTime.append(currentTime+self.timeToLive)

    def renew(self, tokenId: str, currentTime: int) -> None:
        tokenIdx = self.tokens.index(tokenId) if tokenId in self.tokens else -1
        if tokenIdx != -1 and self.expirationTime[tokenIdx] > currentTime:
            self.expirationTime[tokenIdx] = currentTime + self.timeToLive
                  
    def countUnexpiredTokens(self, currentTime: int) -> int:
        unexpiredTokens = list(filter(lambda x: x > currentTime,self.expirationTime))
        return len(unexpiredTokens)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)