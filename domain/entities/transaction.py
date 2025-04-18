from datetime import datetime
from uuid import uuid4

class Transaction:
    def __init__(self, account_id: str, transaction_type: str, amount: float):
        self.transaction_id = str(uuid4())  
        self.account_id = account_id 
        self.transaction_type = transaction_type  
        self.amount = amount
        self.timestamp = datetime.datetime.now()  

