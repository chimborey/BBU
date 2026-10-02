
#  ======================================= 8.Encapsulation =======================================

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 

    # មុខងារជំនួយ (Getter) សម្រាប់ឱ្យខាងក្រៅអាចឆែកមើលលុយបានតាមច្បាប់
    def get_balance(self):
        return self.__balance

account = BankAccount("ពិសិដ្ឋ", 500)
print(account.owner)

# ត្រូវហៅតាមរយៈមុខងារដែលគេអនុញ្ញាតទើបមើលឃើញ
print("ទឹកប្រាក់ក្នុងគណនី:", account.get_balance(), "$") 
