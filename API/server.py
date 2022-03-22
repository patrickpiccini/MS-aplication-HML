#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
from flask import Flask, request
from config.database_connection import ConnectionDatabase
from config.rabbitmq_connection import RabbitConnection

rabbit_queues = RabbitConnection()

class Api_server():
    
    app = Flask(__name__)
    ConnectionDatabase()
    rabbit_queues.create_queues()

    # User Routes

    @app.route("/user/create_user/", methods=['POST'])
    def create_user():
        if request.method == 'POST':
            imput_msg = request.get_json()
            imput_msg['type']='create'
            
            rabbit_return = rabbit_queues.send_msg(
                data=json.dumps(imput_msg),
                route="user")
            
            return {'Status': 200, 'Message': json.loads(rabbit_return)}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/list_user/", methods=['GET'])
    def list_user():
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/display_user/", methods=['GET'])
    def display_user():
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/edit_user/", methods=['POST'])
    def edit_user():
        if request.method == 'POST':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/delete_user/", methods=['DELETE'])
    def delete_user():
        if request.method == 'DELETE':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    # Order Routes
    @app.route("/order/create_order/", methods=['POST'])
    def create_order():
        if request.method == 'POST':
            imput_msg = request.get_json()
            rabbit_queues.send_msg(route="order", msg=imput_msg)

            return {'Status': 200, 'Message': imput_msg}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/list_order/", methods=['GET'])
    def list_order():
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/display_by_order/", methods=['GET'])
    def display_by_order():
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/edit_order/", methods=['POST'])
    def edit_order():
        if request.method == 'POST':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/delete_order/", methods=['DELETE'])
    def delete_order():
        if request.method == 'DELETE':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    app.run('0.0.0.0', 7000)


# if __name__ == '__main__':

#     APP = Api_server()
#     APP.app.run('0.0.0.0', 7000)
