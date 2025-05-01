from faker import Faker

fake = Faker()

class TestdataGenerator:

    @staticmethod
    def get_first_name():
        return fake.first_name()

    @staticmethod
    def get_last_name():
        return fake.last_name()

    @staticmethod
    def get_email():
        return fake.email(domain='testmail.com')

    @staticmethod
    def get_telephone():
        return fake.phone_number()

    @staticmethod
    def get_password():
        return fake.password(length=5,special_chars=True,digits=True,lower_case=True)