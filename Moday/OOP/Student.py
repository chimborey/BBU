

# ================================= 6. Self =================================

class Student:
    def __init__(self, name):
        # self.name គឺចង់ប្រាប់ថា អថេរ name នេះជារបស់ Object មួយដែលកំពុងបង្កើត
        self.name = name 

    def introduce(self):
        # ប្រើ self.name ដើម្បីទៅទាញយកឈ្មោះរបស់ Object នោះមកបង្ហាញ
        print(f"សួស្តី ខ្ញុំបាទឈ្មោះ {self.name}។")

# បង្កើត Object ចំនួន ២ ផ្សេងគ្នា
student1 = Student("ពិសិដ្ឋ")
student2 = Student("តារា")

# ពេលហៅ student1.introduce() -> self នឹងដើរតួជា student1 (បង្ហាញឈ្មោះ ពិសិដ្ឋ)
student1.introduce()  

# ពេលហៅ student2.introduce() -> self នឹងដើរតួជា student2 (បង្ហាញឈ្មោះ តារា)
student2.introduce()  
