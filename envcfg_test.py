
from werkzeug.utils import import_string

mod = import_string('envcfg.json.foo')

config = {key: getattr(mod, key) for key in dir(mod) }
print config


# 运行方法
#  env $(cat .env | xargs) python envcfg_test.py 


# https://pypi.python.org/pypi/python-envcfg
# https://github.com/tonyseek/python-envcfg
