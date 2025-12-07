import pyodbc

class Database:
    def __init__(self, db_name, server="localhost"):
        self.conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={db_name};'
            f'Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()

    # Додавання пасажира до бази даних
    def add_passenger(self, name, surname, email, password, passport, birth_date):
        self.cursor.execute("INSERT INTO Passengers (Name, Surname, Email, Password, Passport, Birth_date) VALUES (?, ?, ?, ?, ?, ?)", (name, surname, email, password, passport, birth_date))
        self.conn.commit()

    # Отримання інформації про пасажираx
    def get_passenger(self, email):
        self.cursor.execute("SELECT * FROM Passengers WHERE Email = ?", (email,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        columns = [column[0] for column in self.cursor.description]
        return dict(zip(columns, row))
    
    # Отримання усіх пасажирів
    def get_all_passengers_raw(self):
        if not self.cursor.connection: return []
        
        query = "SELECT Name, Surname, Email, Passport, id FROM Passengers"
        
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Помилка завантаження пасажирів: {e}")
            return []

    # Видалення пасажира
    def delete_passenger(self, email):
        self.cursor.execute("DELETE FROM Passengers WHERE Email = ?", (email,))
        self.conn.commit()
    
    # Перевірка наявності Gmail
    def check_gmail(self, email):
        self.cursor.execute("SELECT Email FROM Passengers WHERE Email = ?", (email,))
        result = self.cursor.fetchone()
        return result is not None
    
    # Отримання пароля для перевірки входу
    def login(self, email):
        self.cursor.execute("SELECT Password FROM Passengers WHERE Email = ?", (email,))
        result = self.cursor.fetchone()

        if not result:
            return "no_user"

        return result[0]

    # Пошук рейсів
    def find_flights(self, from_city: str, to_city: str, search_date: str = None) -> list:
        if not self.cursor.connection: return []

        base_query = """
        SELECT
            f.flight_id, 
            f.flight_number, 
            orig.city_name AS from_city,
            dest.city_name AS to_city, 
            f.base_price, 
            f.available_seats,
            f.departure_date, 
            f.departure_time,
            f.airplane_id
        FROM
            [dbo].[Flights] f
        JOIN
            [dbo].[Airports] orig ON f.origin_airport_id = orig.airport_id
        JOIN
            [dbo].[Airports] dest ON f.destination_airport_id = dest.airport_id
        WHERE
            TRIM(orig.city_name) = ?
            AND TRIM(dest.city_name) = ?
            AND f.available_seats > 0
        """

        params = [from_city, to_city]

        if search_date:
            base_query += " AND f.departure_date = ?"
            params.append(search_date)

        try:
            self.cursor.execute(base_query, tuple(params))
            raw_flights = self.cursor.fetchall()
            return raw_flights
            
        except Exception as e:
            print(f"Помилка при пошуку рейсів: {e}")
            return []

    # Отримання всіх рейсів (для алгоритму Дейкстри)
    def get_all_flights_raw(self) -> list:
        if not self.cursor.connection: return []
        
        query = """
        SELECT
            f.flight_id, f.flight_number, orig.city_name, dest.city_name, 
            f.base_price, f.available_seats, f.departure_date, f.departure_time,
            f.airplane_id
        FROM [dbo].[Flights] f
        JOIN [dbo].[Airports] orig ON f.origin_airport_id = orig.airport_id
        JOIN [dbo].[Airports] dest ON f.destination_airport_id = dest.airport_id
        WHERE f.available_seats > 0
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Помилка при отриманні усіх рейсів: {e}")
            return []

    # Отримання членів екіпажу літака
    def get_crew_for_airplane(self, airplane_id):
        if not self.cursor.connection: return []
        
        query = """
        SELECT 
            e.name, 
            e.surname, 
            a.role_on_board 
        FROM [dbo].[Emploees] e
        JOIN [dbo].[Airplane_Crew] a ON e.emploee_ID = a.employee_id
        WHERE a.airplane_id = ?
        """
        try:
            cursor = self.cursor.connection.cursor()
            cursor.execute(query, (airplane_id,))
            crew_list = cursor.fetchall()
            return crew_list
        except Exception as e:
            print(f"Помилка отримання екіпажу: {e}")
            return []

    # Покупка квитка
    def add_ticket_purchase(self, user_id, flight_id, ticket_type, price):

        if not self.cursor.connection: 
            print("Немає з'єднання з БД")
            return False
        
        try:
            self.cursor.execute("INSERT INTO dbo.UserTickets (user_id, flight_id, ticket_type, price) VALUES (?, ?, ?, ?)", (user_id, flight_id, ticket_type, price))
            self.cursor.connection.commit()
            
            print(f"Квиток на рейс {flight_id} успішно додано для користувача {user_id}")
            return True
            
        except Exception as e:
            print(f"Помилка при купівлі квитка: {e}")
            self.cursor.connection.rollback()
            return False
    
    # Отримання історії квитків користувача
    def get_user_tickets(self, user_id):
        if not self.cursor.connection: return []

        query = """
        SELECT 
            ut.ticket_id,
            ut.ticket_type,
            ut.price,
            ut.purchase_date,
            f.flight_number,
            orig.city_name AS origin,
            dest.city_name AS destination,
            f.departure_date,
            f.departure_time
        FROM dbo.UserTickets ut
        JOIN dbo.Flights f ON ut.flight_id = f.flight_id
        JOIN dbo.Airports orig ON f.origin_airport_id = orig.airport_id
        JOIN dbo.Airports dest ON f.destination_airport_id = dest.airport_id
        WHERE ut.user_id = ?
        ORDER BY ut.purchase_date DESC
        """
        
        try:
            self.cursor.execute(query, (user_id,))
            tickets = self.cursor.fetchall()
            return tickets
        except Exception as e:
            print(f"Помилка отримання історії квитків: {e}")
            return []
    
    # Зменшення кількості вільних місць на рейсі
    def decrease_seats(self, flight_id):
        if not self.cursor.connection: return False
        
        try:
            check_query = "SELECT available_seats FROM [dbo].[Flights] WHERE flight_id = ?"
            self.cursor.execute(check_query, (flight_id,))
            row = self.cursor.fetchone()
            
            if not row:
                print(f"Рейс {flight_id} не знайдено.")
                return False
                
            available_seats = row[0]
            
            if available_seats <= 0:
                print(f"На рейсі {flight_id} немає вільних місць!")
                return False

            update_query = "UPDATE [dbo].[Flights] SET available_seats = available_seats - 1 WHERE flight_id = ?"
            self.cursor.execute(update_query, (flight_id,))
            
            if self.cursor.rowcount > 0:
                self.cursor.connection.commit()
                print(f"Місце на рейсі {flight_id} успішно заброньовано. Залишилось: {available_seats - 1}")
                return True
            else:
                return False
                
        except Exception as e:
            print(f"Помилка при оновленні місць: {e}")
            self.connection.rollback()
            return False

    # Закриття з'єднання
    def close(self):
        self.cursor.close()
        self.conn.close()



# Збереження сесії користувача
class UserSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.user_data = None
        return cls._instance

    def login(self, user_data):
        self.user_data = user_data

    def logout(self):
        self.user_data = None

    def is_logged_in(self):
        return self.user_data is not None

    def get_user(self):
        return self.user_data
