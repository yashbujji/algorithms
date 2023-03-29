class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.counter =0
        self.w_sum = 0
        

    def next(self, val: int) -> float:
        # size = self.size 
        # queue = self.queue
        # queue.append(val)
        # print(queue)
        # summer = sum(queue[-size:])
        # print(summer,'summer')
        # print(len(queue),'length')
        # print(size,'size')
        # return summer/min(len(queue),size)

        self.counter = self.counter+1
        self.queue.append(val)
        tail = self.queue.popleft() if self.counter > self.size else 0
        self.w_sum = self.w_sum - tail+val
        return self.w_sum / min(self.size,self.counter)

