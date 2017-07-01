#coding:utf8

from flask import Flask, url_for, render_template 
from flask import request,abort,redirect,session,escape

#from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow

app = Flask(__name__)


ma = Marshmallow()

class DeviceUnbindSchema(ma.Schema):
    """APP(Gateway)设备请求解绑实体"""

    #: :class:`str` 用户设备唯一ID
    push_token = ma.String(dump_to='push_token_serialize', required=True)


device_unbind_schema = DeviceUnbindSchema()


@app.route("/hello/", methods=['POST'])
def hello(name=None):
    req = request.get_json()
    print 1,req
    print 2,type(req)

    schema = DeviceUnbindSchema()
    result = schema.load(req)

    print result.data
    print type(result.data)

    print result.errors
    print schema.dumps(result.data).data
    print type(schema.dumps(result.data).data)
    
    return "hello ffp"

if __name__ == "__main__":
    print __name__
    app.debug = True
    app.run(host='0.0.0.0')
