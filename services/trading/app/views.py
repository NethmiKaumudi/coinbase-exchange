# /trading/app/views.py

from flask import request, jsonify
from .model import db, Trade

def register_routes(app):
    @app.route('/trade', methods=['POST'])
    def trade():
        data = request.json
        
        user_id = data.get('user_id')
        asset = data.get('asset')
        quantity = data.get('quantity')
        price = data.get('price')
        
        if not all([user_id, asset, quantity, price]):
            return jsonify({'message': 'Missing required fields'}), 400
        
        trade = Trade(user_id=user_id, asset=asset, quantity=quantity, price=price)
        db.session.add(trade)
        db.session.commit()
        
        return jsonify({'message': 'Trade completed', 'trade_id': trade.id}), 200
