from connection import Connection
from position import Position

class PositionService(Connection):
      def __init__(self):
            super().__init__()
            
      def get_position_by_id(self, id: int) -> Position:
            con = self._get_connetion()
            cursor = con.cursor()
            
            # Create Obj
            position = Position()
            
            try:
                  query = """
                        select id, name_en, name_kh from "tbl_position where id=%s
                  """
                  value = (id,);
                  cursor.execute(query, value)
                  data = cursor.fetchone()
                  if data is None:
                        position = None;
                  else:
                        position.id = data[0]
                        position.name_en = data[1]
                        position.name_kh = data[2]
            except Exception as ex:
                  print(f"Get postion id: {id} error: {ex}")
            finally:
                  cursor.close()
                  con.close()
            return position