# /wallet/app/views.py

from flask import request, jsonify
from .model import db, Wallet

def register_routes(app):
    @app.route('/balance', methods=['GET'])
    def balance():
        user_id = request.args.get('user_id')
        wallet = Wallet.query.filter_by(user_id=user_id).first()
        if wallet:
            return jsonify({'user_id': user_id, 'balance': wallet.balance}), 200
        return jsonify({'message': 'Wallet not found'}), 404
