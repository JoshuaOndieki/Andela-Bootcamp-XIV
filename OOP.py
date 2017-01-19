""" Banking
class BankAccount(object):  #Parent class
    bank_accounts=0
    credit_score=0
    loan_balance=0
    def __init__(self,owner_name,owner_id,balance,account_type):
        self.owner_name=owner_name
        self.owner_id=owner_id
        self.balance=balance
        self.account_type=account_type
class PremiumBankAccount(BankAccount):  # PremiumBankAccount inherits from parent BankAccount
    def __int__(self,business_loan):
        self.business_loan=business_loan
class StandardBankAccount(BankAccount):  # StandardBankAccount inherits from parent BankAccount
    def __init__(self,small_loan):
        self.small_loan=small_loan