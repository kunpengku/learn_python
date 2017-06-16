#coding:utf8
import time
from threading  import Thread



def send_msg(msg):


    print 'send msg:' + msg


class Task(Thread):
    def __init__(self, msg):
        super(Task, self).__init__()
        self.msg = msg

    def run(self):
        send_msg(self.msg)


start = time.time()
t_l = []
for i in range(50):
    msg = "{t} vipkid msg {i} ".format(t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), i=i)
    print i
    t_name = Task(msg)
    t_l.append(t_name)


for t in t_l:
    t.start()


for t in t_l:
    t.join()
#t_name.join()


end = time.time()
print 'end'
