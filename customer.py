class Customer:

    def __init__(self, name, phone, email, customer_id=None):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email