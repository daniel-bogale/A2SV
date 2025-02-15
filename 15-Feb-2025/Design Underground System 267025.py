# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.check_in_users = {}
        self.records = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.check_in_users:
            self.check_in_users[id] = [stationName, t]
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_in_users:
            [start_station, start_time] = self.check_in_users[id]
            self.records[start_station+"-"+stationName] = self.records.get(start_station+"-"+ stationName, [])+ [t-start_time]
            self.check_in_users.pop(id)
        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        recs = self.records[startStation+"-"+endStation]
        return sum(recs)/len(recs)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)