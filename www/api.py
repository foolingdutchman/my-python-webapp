#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/28 0028.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import logging
from flask import Flask, jsonify

app = Flask(__name__)

routes = [
    {
        'id': 1,
        'url': 'http://www.sina.com',
        'done': False
    },
    {
        'id': 2,
        'url': 'http://www.baidu.com',
        'is_permission': True
    }
]

@app.route('/route', methods=['GET'])
def get_routes():
    return jsonify({'route': routes[1]})

if __name__ == '__main__':
    app.run(port=3389)