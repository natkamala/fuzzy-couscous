import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('example.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        self.cursor.execute("SELECT sqlite_version();")
        version = self.cursor.fetchone()
        print(f"SQLite Database Version: {version[0]}")
        return version[0]

    def get_all_users(self):
        self.cursor.execute("SELECT name, address, city FROM customers;")
        return self.cursor.fetchall()

    def get_user_address_by_name(self, name):
        self.cursor.execute("SELECT address, city, postalCode, country FROM customers WHERE name = ?", (name,))
        return self.cursor.fetchone()

    def update_product_qnt_by_id(self, product_id, qnt):
        self.cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (qnt, product_id))
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        self.cursor.execute("SELECT quantity FROM products WHERE id = ?", (product_id,))
        return self.cursor.fetchone()

    def insert_product(self, product_id, name, description, qnt):
        self.cursor.execute("REPLACE INTO products (id, name, description, quantity) VALUES (?, ?, ?, ?)",
                            (product_id, name, description, qnt))
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.connection.commit()

    def get_detailed_orders(self):
        self.cursor.execute("""
            SELECT o.id, c.name, p.name, p.description, o.date
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            JOIN products p ON o.product_id = p.id
        """)
        return self.cursor.fetchall()