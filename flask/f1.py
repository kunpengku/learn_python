#coding:utf8

from flask import Flask, url_for, render_template 
from flask import request,abort,redirect,session,escape

from marshmallow import Schema, fields

app = Flask(__name__)



class DeviceUnbindSchema(Schema):
    """APP(Gateway)设备请求解绑实体"""

    #: :class:`str` 用户设备唯一ID
    push_token = fields.Str(dump_to='push_token2', required=True)


device_unbind_schema = DeviceUnbindSchema()


@app.route("/hello/", methods=['POST'])
def hello(name=None):
    req = request.get_json()
    print req
    print type(req)

    schema = DeviceUnbindSchema()
    result = schema.load(req)

    print result.data
    print type(result.data)

    print result.errors
    
    return "hello ffp"




if __name__ == "__main__":
    print __name__
    app.debug = True
    app.run(host='0.0.0.0')
