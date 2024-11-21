from shop import Shop, User

"""
Added 2 tests in order to test the cases where verified and children OR major 
Same with unverified
"""

def create_default_user(address, name="bob", email="bob@gmail.com", age=16, verified=True):
    return User(
        name=name,
        email=email,
        age=age,
        address=address,
        verified=verified
    )

def test_happy_path(fsf_address):
    user = create_default_user(address=fsf_address, age=25)
    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop(fsf_address):
    user = create_default_user(address=fsf_address)
    assert not Shop.can_order(user)


def test_adults_can_order_from_the_shop(fsf_address):
    user = create_default_user(address=fsf_address, age=20)
    assert Shop.can_order(user)


def test_cannot_order_if_not_verified_child(fsf_address):
    user = create_default_user(address=fsf_address, verified=False)
    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified_adult(fsf_address):
    user = create_default_user(address=fsf_address, age=20, verified=False)
    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee(paris_address):
    user = create_default_user(address=paris_address, age=25, verified=False)
    assert Shop.must_pay_foreign_fee(user)
