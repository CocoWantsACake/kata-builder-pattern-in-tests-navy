from shop import Shop, User
from conftest import fsf_address, paris_address

"""
Added 2 tests in order to test the cases where verified and children OR major 
Same with unverified
"""

def create_user(address=fsf_address, name="bob", email="bob@gmail.com", age=20, verified=True):
    return User(
        name=name,
        email=email,
        age=age,
        address=address,
        verified=verified
    )

def test_happy_path():
    user = create_user()
    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop():
    user = create_user(age=16)
    assert not Shop.can_order(user)


def test_adults_can_order_from_the_shop():
    user = create_user()
    assert Shop.can_order(user)


def test_cannot_order_if_not_verified_child():
    user = create_user(age=16, verified=False)
    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified_adult():
    user = create_user(verified=False)
    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee():
    user = create_user(address=paris_address)
    assert Shop.must_pay_foreign_fee(user)
