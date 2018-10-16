class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        
    def __sub__(self, time):
        res = (self.hour - time.hour) * 60 + (self.minute - time.minute)
        if res > 0: return res
        else: return res + 24*60
        
    def __str__(self):
        minute = str(self.minute) if self.minute // 10 != 0 else '0' + str(self.minute)
        hour = str(self.hour) if self.hour // 10 != 0 else '0'+ str(self.hour)
        return hour + ':' + minute
    
    def isValid(self):
        return self.hour < 24 and self.minute < 60
        

class Solution(object):
    def __init__(self):
        self.closest_time = None
        
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        curr_time = Time(int(time[:2]), int(time[3:]))
        digits = sorted(list((map(int, [v for v in time if v != ':']))))
        min_diff = (float('inf'), None)
        for i in itertools.product(*([digits] * 4)):
            gen_time = Time(i[0] * 10 + i[1], i[2] * 10 + i[3])
            if not gen_time.isValid():
                continue
            if 0 < gen_time - curr_time < min_diff[0]:
                min_diff = (gen_time - curr_time, gen_time)
        return str(min_diff[1])
