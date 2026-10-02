# ================================= 7. __init__ =================================

class Car:
    # បង្កើត constructor __init__ ដើម្បីទទួលតម្លៃពេលបង្កើត Object
    def __init__(self, model, year):
        self.model = model
        self.year = year
        # វានឹងរត់កូដខាងក្រោមនេះអូតូភ្លាមៗ
        print(f"ឡានម៉ាក {self.model} ត្រូវបានបង្កើតឡើងជោគជ័យ!") 

    def show_info(self):
        print(f"ព័ត៌មាន៖ ឡាននេះម៉ាក {self.model} ផលិតឆ្នាំ {self.year}")

# គ្រាន់តែវាយជួរខាងក្រោមនេះដើម្បីបង្កើត Object នោះ __init__ នឹងរត់ភ្លាមៗ
# ដោយមិនបាច់វាយ car1.__init__(...) ឡើយ
car1 = Car("Toyota", 2024) 

# បន្ទាប់មកយើងអាចហៅ Method ផ្សេងទៀតមកប្រើធម្មតា
car1.show_info()
