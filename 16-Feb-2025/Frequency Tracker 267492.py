# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:
    def __init__(self):
        self.num_freq = {} 
        self.freq_num = {}  

    def add(self, number: int) -> None:
        old_freq = self.num_freq.get(number, 0)
        if old_freq != 0:
            old_freq_dict = self.freq_num[old_freq]
            old_freq_dict.pop(number)
            # key part
            if not old_freq_dict:  
                self.freq_num.pop(old_freq)
        
        new_freq = old_freq + 1
        self.num_freq[number] = new_freq
        # setdefault
        self.freq_num.setdefault(new_freq, {})[number] = True

    def deleteOne(self, number: int) -> None:
        if number in self.num_freq:
            old_freq = self.num_freq[number]
            old_freq_dict = self.freq_num[old_freq]
            old_freq_dict.pop(number)
            # key part
            if not old_freq_dict:  
                self.freq_num.pop(old_freq)

            if old_freq == 1:
                self.num_freq.pop(number)  
            else:
                new_freq = old_freq - 1
                self.num_freq[number] = new_freq
                # setdefault
                self.freq_num.setdefault(new_freq, {})[number] = True

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_num and bool(self.freq_num[frequency])


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)