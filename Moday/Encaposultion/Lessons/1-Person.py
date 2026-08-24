




class Person:
      def __init__(self):
            self.__id = 0
            self.__name = ""
            
      # Getter
      @property
      def id(self):
            return self.__id
      def name(self):
            return self.__name
      # Setter
      @id.setter
      def id(self, value: int):
            self.__id = value;
            
      @name.setter
      def name(self, value: str):
            self.__name = value
      