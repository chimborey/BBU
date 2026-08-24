print("=================================================== Create Student ========================================\n\t")
#  ============================ Create Class, Then(Enrolled to Input, and Output) ============================================
class Stu:
      
      # ----------------------------------- Input -----------------------------------
      def __init__(self):
            self.id = 1
            self.name = "Sokha"
            self.gender = "Male"
            self.phone = "123-1203-029"
            pass
      
      # ----------------------------------- Output -----------------------------------
      def showFields(self):
            print(f"ID: {self.id}");
            print(f"Name: {self.name}");
            print(f"Gender: {self.gender}");
            print(f"Phone: {self.phone}");

if __name__ == "__main__":
      # student
      objectStu = Stu()
      objectStu.showFields()
         
print("=================================================== Create Teacher ========================================\n\t")
#  ============================ Create Class, Then(Enrolled to Input, and Output) ============================================
class Teacher:
      
      # ----------------------------------- Input -----------------------------------
      def __init__(self):
            self.id = 1
            self.name = "Sokha"
            self.name_en = "Sokha"
            self.name_Kh = "សុខា"
            self.gender = "Male"
            self.dob = "teacher"
            pass
      
      # ----------------------------------- Output -----------------------------------
      def showFieldsForTeacher(self):
            print(f"ID: {self.id}");
            print(f"Name: {self.name}");
            print(f"nameEn: {self.name_en}");
            print(f"nameKh: {self.name_Kh}");
            print(f"Gender: {self.gender}");
            print(f"Dob: {self.dob}");
            
# ================================ Called To Class(Stu) ============================================
if __name__ == "__main__":
      # teacher
      objectTeacher = Teacher()
      objectTeacher.showFieldsForTeacher()
      