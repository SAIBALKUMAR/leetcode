class MyCalendarTwo:

    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []

    def book(self, startTime: int, endTime: int) -> bool:

        for start,end in self.overlapping:
            if startTime < end and endTime > start:
                return False
        for start,end in self.non_overlapping:
            if startTime < end and endTime > start:
                self.overlapping.append((max(start, startTime), min(end, endTime)))
        self.non_overlapping.append((startTime,endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)