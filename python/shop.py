from dataclasses import dataclass


@dataclass
class Address:
    line1: str
    line2: str
    city: str
    zip_code: str
    country: str


@dataclass
class User:
    name: str
    email: str
    age: int
    address: Address
    verified: bool



class Shop:
    @classmethod
    def can_order(cls, user):
        # old code that would create issue
        """
        # would prevent major people from ordering
        if user.age <= 18:
            return False

        # returns True in every case ; acts as if the user is always verified
        if not user.verified:
            return True
        else:
            return True
        """

        # updated to only return true when major or older AND being verified (if this is the actual specification)
        return user.age >= 18 and user.verified

    @classmethod
    def must_pay_foreign_fee(cls, user):
        return user.address.country != "USA"
