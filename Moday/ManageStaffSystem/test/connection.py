

import psycopg2

class Connection:
      def _get_connetion(self):
            try:
                  return psycopg2.connect(
                        database = "Test_Day01_Postgres", user = "user01", password = "0987654", host = "localhost", port = "5432",
                  )
            except Exception as ex:
                  print(f"Connect error: {ex}")