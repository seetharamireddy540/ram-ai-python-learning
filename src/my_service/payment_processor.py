
class PaymentProcessor:
    
    def __init__(self):
        pass
    
    def process_payment(self, amount):
        pass
    

class CreditCardProcessor(PaymentProcessor):

    def __init__(self):
        super().__init__()

    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount} dollars.")