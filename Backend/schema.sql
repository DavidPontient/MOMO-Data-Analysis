-- this will define my db schema and creates transactions table with indexes, useful if switching to PostgreSQL/MySQL.
CREATE TABLE IF NOT EXISTS transactions (
  id SERIAL PRIMARY KEY,
  address VARCHAR(255),
  date TIMESTAMP,
  type VARCHAR(50),
  body TEXT,
  category VARCHAR(100),
  amount INTEGER,
  sender VARCHAR(100),
  receiver VARCHAR(100),
  readable_date VARCHAR(50)
);
CREATE INDEX idx_category ON transactions(category);
CREATE INDEX idx_date ON transactions(date);
CREATE INDEX idx_amount ON transactions(amount);
