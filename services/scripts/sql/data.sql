-- Insert sample users
INSERT INTO users (username, password) VALUES ('admin', 'admin_password');
INSERT INTO users (username, password) VALUES ('user1', 'user1_password');

-- Insert sample wallets
INSERT INTO wallets (user_id, balance) VALUES (1, 1000.00);
INSERT INTO wallets (user_id, balance) VALUES (2, 500.00);

-- Insert sample trades
INSERT INTO trades (user_id, trade_type, amount, status) VALUES (1, 'buy', 100.00, 'completed');
INSERT INTO trades (user_id, trade_type, amount, status) VALUES (2, 'sell', 50.00, 'pending');

-- Insert sample transactions
INSERT INTO transactions (user_id, trade_id, amount, transaction_type) VALUES (1, 1, 100.00, 'debit');
INSERT INTO transactions (user_id, trade_id, amount, transaction_type) VALUES (2, 2, 50.00, 'credit');
