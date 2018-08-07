# coding=utf-8
from flask import jsonify
from werkzeug.wrappers import Response

class JSONResponse(Response):
    #继承自Response类，实现Response的force_type方法
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response,dict):
            response=jsonify(response)
        return super(JSONResponse,cls).force_type(response,environ)