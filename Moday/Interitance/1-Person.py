# ============= 6. Interitance ===========

# ------------- Create SuperClass ---------
class Person: 
      def __init__(self, id, name, dob, gender):
            self.__id = id;
            self.__name = name;
            self.__dob = dob;
            self.___gender = gender;
      
      # property
      @property
      def id(self): return self.__id;
      def name(self): return self.__name;
      def gender(self): return self.___gender;
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
      def marjor(self): return self.__marjor;
      def faculty(self): return self.__faculty;
      def python(self): return self.__python;
      def database(self): return self.__database;
      def dsa(self): return self.__dsa;
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
      def dsa(self, value: float): self.__dsa = value;
      @network.setter
      def network(self, value: str): self.__network = value;
