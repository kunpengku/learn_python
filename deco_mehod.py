

dry_run=True
import time

def dry_run_deco(method):
    def m_dry_run(*arg, **k):
        if dry_run is True:
            print 'fake method'
            print 'sleep'
            time.sleep(0.2)
            print 'return the same'
        else:
            method(*arg, **k)
        


    return m_dry_run


@dry_run_deco
def send(msg):
    print 'send msg', msg






send('nihao')
