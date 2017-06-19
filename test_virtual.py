import sys


if __name__ == '__main__':

    print dir(sys)

    print sys.real_prefix
    assert hasattr(sys, 'real_prefix'), 'called without virtualenv'
    manager.run()
