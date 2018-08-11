import redis

class Task():
    def __init__(self):
        self.rconn=redis.Redis(host='127.0.0.1',db=2)
        print(dir(self.rconn))
        self.queue='taskdata:queue'
    def process_task(self):
        while True:
            task=self.rconn.blpop(self.queue,0)[1]
            print('收到数据 : ',task)

Task().process_task()
