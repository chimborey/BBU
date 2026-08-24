# ============= 6. Interitance ===========

# ------------- Create SuperClass ---------
class Person: 
      def __init__(self, id, name, dob, gender):
            self.__id = id;
            self.__name = name;
            self.___gender = gender;
            self.__dob = dob;
      
      # property
      @property
      def id(self): return self.__id;
      @property
      def name(self): return self.__name;
      @property
      def gender(self): return self.___gender;
      @property
      def dob(self): return self.__dob;
      
      # setter
      @id.setter
      def id(self, value: int): self.__id = value;
      @name.setter
      def name(self, value: str): self.__name = value;
      @gender.setter
      def gender(self, value: str): self.___gender = value;  
      @dob.setter
      def dob(self, value: str): self.__dob = value; 
       
# ------------- Create ChildClass ---------
class Studen(Person):
      def __init__(self, id, name, dob, gender, marjor, degree, faculty, python, database, dsa, network):
            super().__init__(id, name, dob, gender)
            self.__degree = degree
            self.__marjor = marjor;
            self.__faculty = faculty;
            self.__python = python;
            self.__database = database;
            self.__dsa = dsa;
            self.__network = network;
      @property
      def degree(self): return self.__degree;
      @property
      def marjor(self): return self.__marjor;
      @property
      def faculty(self): return self.__faculty;
      @property
      def python(self): return self.__python;
      @property
      def database(self): return self.__database;
      @property
      def dsa(self): return self.__dsa;
      @property
      def network(self): return self.__network;
      
      @degree.setter
      def degree(self, value: str): self.__degree = value;
      @marjor.setter
      def marjor(self, value: str): self.__marjor = value;
      @faculty.setter
      
      def faculty(self, value: str): self.__faculty = value;
      @python.setter
      def python(self, value: float):
            if value < 0 or value > 100:
                  raise ValueError("Invalid value.")
            else:
                  self.__python = value;
      @database.setter
      def database(self, value: float): self.__database = value;
      @dsa.setter
      def dsa(self, value: float):
            if value > 0 and value < 100:
                  raise ValueError("Invalid value.")
            else:
                  self.__dsa = value;
      @network.setter
      def network(self, value: str): self.__network = value;
      # ------------- Show_Student ---------
      def show_Student(self):
            print(f"ID: {self.id}")
            print(f"Name: {self.name}")
            print(f"Gender: {self.gender}")
            print(f"Dob: {self.dob}")
            print(f"Degree: {self.degree}")
            print(f"Marjor: {self.marjor}")
            print(f"Faculty: {self.faculty}")
            print(f"Python: {self.python}")
            print(f"Database: {self.database}")
            print(f"Dsa: {self.dsa}")
            print(f"Network: {self.network}")
      

if __name__ == "__main__":
      object = Studen(
            1, "Nita", "Female", "01-01-2000", "Bachelor", "Leader", "", 90.0, 70.50, 50.50, 90
      )
      object.show_Student()
            
