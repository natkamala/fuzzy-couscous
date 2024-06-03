import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    version = db.test_connection()
    assert "3." in version

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)  # Припустимо, що база даних налаштована і містить користувачів

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user_info = db.get_user_address_by_name('Sergii')
    assert user_info == ('Maydan Nezalezhnosti 1', 'Kyiv', '3127', 'Ukraine')

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    quantity = db.select_product_qnt_by_id(1)
    assert quantity[0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    quantity = db.select_product_qnt_by_id(4)
    assert quantity[0] == 30
    


