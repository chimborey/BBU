# 3-bank_accpunt_system
account_list  = []
# input_integer
def input_integer(label: str):
      while True:
            try:
                  return int(input(label))
            except ValueError:
                  print("Must input number. please input again.")
# int_float
def input_float(label: str):
      while True:
            try:
                  return float(input(label))
            except ValueError:
                  print("Must input number. please input again.")
# find__by__id 
def find__by__id(id: int):
      for acc in account_list:
            if acc['id'] == id:
                  return acc;
# find_by_acc_num
def find_by_acc_num(acc_num: str):
      for acc  in account_list:
            if str(acc['acc_num'].str().strip() == acc_num.strip()):
                  return acc;
            return None;
# create__new__account
def create__new__account():
      id = input_integer("Please input account id: ")
      if find__by__id(id) is not None:
            print(f"Sorry, account id: {id} arleady exist.")
            return;
      acc_num = input("Please input account number:")
      acc_name = input("Please input account name:")
      acc_type = input("Please input account type(saving/current)")
      ssn = input("please input ssn")
      balance = input_float("Please input balance")
      accunt = {
            "id": id,
            "acc_num": acc_num,
            "acc_name": acc_name,
            "acc_type": acc_type,
            "ssn": ssn,
            "balance": balance
      }
      account_list.append(accunt)
      print("Registred new account successfuly.")
# show_all_account
def show_all_account():
      print("=========================All Account================================")
      if len(account_list) == 0:
            print("No Account registered.")
      else:
            print("id\tAccount Name\tAccount Number\tType\tSSN\tBalance")
            for acc in account_list:
                  print(f"{acc['id']}\t"f"{acc['acc_name']}\t"f"{acc['acc_num']}\t"f"{acc['acc_type']}\t"f"{acc['ssn']}\t"f"{acc['balance']}\t")
#__name__ 
if __name__ == "__main__":
     while True:
           print("==============================Menu=====================================")
           print("1.Create new account")
           print("2.Update account by ID")
           print("3.Delete account by ID")
           print("4.Desposit")
           print("5.Withdraw")
           print("6.Show all account")
           print("7.Exist")
           menu = input_integer("Please choose menu {1-7:")
           if menu ==1:
                 print("====Create new account from=====");
                 create__new__account();
           elif menu == 6:
                 show_all_account();
           elif menu == 7:
                 print("System Exited.")
                 break
           else:
                 print("invalid menu.Please choose [1-7] again.");
           