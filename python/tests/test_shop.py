from shop import Shop, User

"""
Added 2 tests in order to test the cases where verified and children OR major 
Same with unverified
"""


def test_happy_path(fsf_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=25,
        address=fsf_address,
        verified=True,
    )

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop(fsf_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=16,
        address=fsf_address,
        verified=True,
    )
    # Verified but not major = cannot order
    assert not Shop.can_order(user)


def test_adults_can_order_from_the_shop(fsf_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=20,
        address=fsf_address,
        verified=True,
    )
    # Verified and major = can order
    assert Shop.can_order(user)


def test_cannot_order_if_not_verified_child(fsf_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=16,
        address=fsf_address,
        verified=False,
    )
    # Not verified and not major = cannot order
    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified_adult(fsf_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=20,
        address=fsf_address,
        verified=False,
    )
    # Not verified = cannot order
    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee(paris_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=25,
        address=paris_address,
        verified=False,
    )

    assert Shop.must_pay_foreign_fee(user)
