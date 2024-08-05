import psycopg2

class DatabaseManager:
    """
    Prisijungimąs ir operacijos su PostgreSQL duomenų baze.
    """

    def __init__(self, dbname, user, password, host, port):
        """
        Inicializuoja DatabaseManager su prisijungimo parametrais.

        Args:
            dbname (str): Duomenų bazės pavadinimas.
            user (str): Duomenų bazės vartotojo vardas.
            password (str): Duomenų bazės vartotojo slaptažodis.
            host (str): Duomenų bazės serverio hostname.
            port (int): Duomenų bazės serverio prievado numeris.
        Return: None
        """

        self.__dbname = dbname
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = psycopg2.connect(
                dbname=self.__dbname,
                user=self.__user,
                password=self.__password,
                host=self.__host,
                port=self.__port
            )
            self.__cursor = self.__connection.cursor()
        except psycopg2.OperationalError as e:
            raise ConnectionError(f"Nepavyko prisijungti prie duomenų bazės: {e}")

    def fetch_all(self, query):
        self.__ensure_connection()
        try:
            self.__cursor.execute(query)
            return self.__cursor.fetchall()
        except Exception as e:
            raise RuntimeError(f"Užklausos vykdymas nepavyko: {e}")

    def execute_query(self, query, params=None):
        self.__ensure_connection()
        try:
            self.__cursor.execute(query, params)
            self.__connection.commit()
        except Exception as e:
            self.__connection.rollback()
            raise RuntimeError(f"Užklausos vykdymas nepavyko: {e}")

    def close(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connection:
            self.__connection.close()

    def __ensure_connection(self):
        if not self.__connection or not self.__cursor:
            raise ConnectionError("Nesate prisijungę prie duomenų bazės.")

    def get_cursor_description(self):
        """Gaukite kursorio aprašymą, kad gautumėte stulpelių pavadinimus"""
        if self.__cursor:
            return self.__cursor.description
        else:
            raise ConnectionError("Nesate prisijungę prie duomenų bazės arba kursoris neegzistuoja.")
