# /api-gateway/app/routes.py

from flask import request, jsonify

def register_routes(app):
    @app.route('/trade', methods=['POST'])
    def trade():
        data = request.json
        # Forward the request to the Trading Service
        response = {
            'message': 'Trade request forwarded',
            'data': data
        }
        return jsonify(response), 200

    @app.route('/balance', methods=['GET'])
    def balance():
        # Forward the request to the Wallet Service
        response = {
            'message': 'Balance request forwarded'
        }
        return jsonify(response), 200

    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        # Forward the request to the Account Management Service
        response = {
            'message': 'Login request forwarded',
            'data': data
        }
        return jsonify(response), 200

    @app.route('/logout', methods=['POST'])
    def logout():
        data = request.json
        # Forward the request to the Account Management Service
        response = {
            'message': 'Logout request forwarded',
            'data': data
        }
        return jsonify(response), 200
