from flask import Flask
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import flask


def create_blueprint(name, version, package_name, source_control=True, **kwargs):
    url_prefix = kwargs.pop('url_prefix', '/{}'.format(name))
    url_prefix = '/{version}{url_prefix}/<string:customer>'.format(
        version=version, url_prefix=url_prefix)
    print url_prefix

    bp_name = '{version}.{name}'.format(version=version, name=name)
    bp = flask.Blueprint(bp_name, package_name, url_prefix=url_prefix, **kwargs)

    return bp

bp = create_blueprint('biz', 'v1', __name__)

@bp.route('/users/filter')
def filter_users(customer):
    try:
        print customer
        return "get url customer[{customer}]".format(customer=customer)
    except TemplateNotFound:
        abort(404)

app = Flask(__name__)

app.register_blueprint(bp)


if __name__ == "__main__":
    print __name__
    app.debug = True
    app.run(host='0.0.0.0')


#http://192.168.8.128:5000/v1/biz/teacher/users/filter
