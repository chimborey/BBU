class Position:
      def __init__(self):
            self.__id = 0;
            self.__name_en = "";
            self.__name_kh = "";
            
      @property
      def id(self): return self.__id;
      @id.setter
      def id(self, value: int): self.__id = value;
      
      
      @property
      def name_en(self): return self.__name_en;
      @name_en.setter
      def name_en(self, value: str): self.__name_en;
      
      @property
      def name_kh(self): return self.__name_kh;
      @name_kh.setter
      def name_kh(self, value: str): self.__name_kh;