class Solution(object):
    def numRescueBoats(self, people, limit):
        
        people=sorted(people)
        i=counter=0
        j=len(people)-1
        while i<=j:
            if people[i]+people[j]<=limit:
                i+=1
                j-=1
                counter+=1
            elif i==j:
                counter+=1
                i+=1
                j-=1
            else:
                j-=1
                counter+=1
        return counter
