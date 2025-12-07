import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QCompleter, QDialog, QMessageBox, 
                               QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
                               QSpinBox, QMenu, QWidgetAction, QFormLayout, QListWidgetItem, QFrame)
from PySide6.QtCore import Qt, QSize, Signal, QPoint
from PySide6.QtGui import QIcon
import ctypes
import os

from gui.main_window import Ui_MainWindow
from gui.sign_in_window import Ui_SignIn as Ui_LoginWindow
from gui.register_window import Ui_Registration as Ui_RegWindow
from gui.flight_pick import Ui_FlightPick

from program_files.text_materials import materials
from program_files.db import Database, UserSession

try:
    from program_files.core_backend import BookingSystem
    print("C++ Backend успішно завантажено.")
except ImportError as e:
    print(f"Помилка імпорту C++: {e}")

db = Database(db_name="AeroNova")
booking_system = BookingSystem()

if sys.platform == 'win32':
    myappid = 'aeronova.desktop.1.0' 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class LoginWindow(QDialog, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
        self.sign_in_btn.clicked.connect(self.login_user)

        self.normal_style = materials.normal_style
        self.error_style = materials.error_style

        self.email_sign_in.textChanged.connect(lambda: self.reset_field_style(self.email_sign_in))
        self.password_sign_in.textChanged.connect(lambda: self.reset_field_style(self.password_sign_in))

    def reset_field_style(self, field):
        field.setStyleSheet(self.normal_style)

    def login_user(self):
        email = self.email_sign_in.text().strip()
        password = self.password_sign_in.text().strip()

        has_error = False
        if not email:
            self.email_sign_in.setStyleSheet(self.error_style)
            has_error = True
        
        if not password:
            self.password_sign_in.setStyleSheet(self.error_style)
            has_error = True
        
        if has_error:
            return

        # Використання C++ для перевірки логіна
        status = booking_system.login_logic(password, db.login(email))

        if status == "success":
            UserSession().login(user_data=db.get_passenger(email))
            window.show_user_info()
            self.close()

        elif db.login(email) == "no_user":
            self.email_sign_in.setStyleSheet(self.error_style)
        else:
            self.password_sign_in.setStyleSheet(self.error_style)

class RegWindow(QDialog, Ui_RegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_account_btn.clicked.connect(self.register_user)
        self.normal_style = materials.normal_style
        self.error_style = materials.error_style

        self.name_reg.textChanged.connect(lambda: self.reset_field_style(self.name_reg))
        self.surname.textChanged.connect(lambda: self.reset_field_style(self.surname))
        self.email_reg.textChanged.connect(lambda: self.reset_field_style(self.email_reg))
        self.password_reg.textChanged.connect(lambda: self.reset_field_style(self.password_reg))
        self.passport.textChanged.connect(lambda: self.reset_field_style(self.passport))


    def reset_field_style(self, field):
        field.setStyleSheet(self.normal_style)

    def register_user(self):
        name = self.name_reg.text().strip()
        surname = self.surname.text().strip()
        email = self.email_reg.text().strip()
        password = self.password_reg.text().strip()
        passport = self.passport.text().strip()
        
        # Використання C++ для хешування пароля
        hash_password = booking_system.hash_password_cpp(password)
        
        birth_date = self.birth_date.date().toString("yyyy-MM-dd")

        has_error = False
        if not name: self.name_reg.setStyleSheet(self.error_style); has_error = True
        if not surname: self.surname.setStyleSheet(self.error_style); has_error = True
        if not email: self.email_reg.setStyleSheet(self.error_style); has_error = True
        if not password: self.password_reg.setStyleSheet(self.error_style); has_error = True
        if not passport: self.passport.setStyleSheet(self.error_style); has_error = True

        if has_error: return

        if db.check_gmail(email):
            self.email_reg.setStyleSheet(self.error_style)
            return

        db.add_passenger(name, surname, email, hash_password, passport, birth_date)
        p = db.get_passenger(email)
        if passport:
            booking_system.add_passenger_to_hash(name, surname, email, passport, p['id'])

        self.close()

class FlightItemWidget(QWidget):
    def __init__(self, flight_data, parent=None):
        super().__init__(parent)
        
        if len(flight_data) >= 9:
            f_id = flight_data[0]
            f_num = flight_data[1]
            orig = flight_data[2]
            dest = flight_data[3]
            price = flight_data[4]
            seats = flight_data[5]
            date = flight_data[6]
            time = flight_data[7]
            
            self.airplane_id = flight_data[10]
        else:
            f_id, f_num, orig, dest, price, seats, date, time = flight_data[:8]
            self.airplane_id = flight_data[9]

        self.icon_label = QLabel("✈️")
        self.icon_label.setStyleSheet("font-size: 30px; margin-right: 10px;")
        
        time_str = time.strftime('%H:%M') if hasattr(time, 'strftime') else str(time)[:5]
        date_str = str(date)[:10]

        self.route_label = QLabel(f"{orig} → {dest}")
        self.route_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #1565c0;")
        
        self.time_label = QLabel(f"{date_str} о {time_str} (Рейс: {f_num})")
        self.time_label.setStyleSheet("color: #555;")

        self.price_label = QLabel(f"💰 {price} UAH")
        self.price_label.setStyleSheet("font-weight: bold; color: #1565c0; font-size: 18px;")

        seats_label = QLabel(f"Вільних місць: {seats}")
        seats_label.setStyleSheet("color: #a04000;")
        
        crew_button = QPushButton("👨‍✈️ Екіпаж")
        crew_button.setFixedWidth(100)
        crew_button.setStyleSheet("QPushButton { background-color: #17a2b8; color: white; border-radius: 5px; font-weight: bold; } QPushButton:hover { background-color: #138496; }")
        crew_button.clicked.connect(self.show_crew)

        buy_button = QPushButton("Купити")
        buy_button.setFixedWidth(100)
        buy_button.setProperty("flight_id", f_id)
        buy_button.setStyleSheet("QPushButton { background-color: #28a745; color: white; border-radius: 5px; font-weight: bold; } QPushButton:hover { background-color: #218838; }")
        buy_button.clicked.connect(self.buy_flight)
        
        left = QVBoxLayout()
        left.addWidget(self.route_label)
        left.addWidget(self.time_label)
        left.addStretch()
        
        right = QVBoxLayout()
        right.addWidget(self.price_label)
        right.addWidget(seats_label)
        right.addWidget(crew_button)
        right.addWidget(buy_button)
        right.addStretch() 
        right.setAlignment(Qt.AlignRight) 
        
        main = QHBoxLayout()
        main.addWidget(self.icon_label, alignment=Qt.AlignTop)
        main.addLayout(left)
        main.addStretch() 
        main.addLayout(right)
        
        self.setLayout(main)
        self.default_style()

    def default_style(self):
        self.setStyleSheet("QWidget { background-color: white; color: #1e90ff; font-size: 14px; font-weight: bold; border: 2px solid #1e90ff; border-radius: 8px; padding: 6px 12px; }")

    def set_transfer_style(self, step_num):
        self.icon_label.setText(f"🔄 {step_num}")
        self.setStyleSheet("QWidget { background-color: #e3f2fd; color: #1565c0; border: 2px dashed #90caf9; border-radius: 8px; padding: 6px 12px; }")
        self.price_label.setStyleSheet("color: #1565c0; font-size: 18px; font-weight: bold;")
        self.route_label.setStyleSheet("color: #1565c0; font-size: 16px; font-weight: bold;")

    def show_crew(self):
        if not self.airplane_id:
            QMessageBox.warning(self, "Інфо", "Інформація про літак відсутня.")
            return

        crew_data = db.get_crew_for_airplane(self.airplane_id)
        
        if not crew_data:
            QMessageBox.information(self, "Екіпаж", "Екіпаж ще не призначено на цей рейс.")
            return

        names = [row[0] for row in crew_data]
        surnames = [row[1] for row in crew_data]
        roles = [row[2] for row in crew_data]

        duties_list = booking_system.get_crew_duties(names, surnames, roles)
        
        msg = "\n".join(duties_list)
        QMessageBox.information(self, f"Екіпаж (Літак ID: {self.airplane_id})", msg)

    def buy_flight(self):
        f_id = self.sender().property("flight_id")
        session = UserSession()
        
        if session.is_logged_in():
            if db.decrease_seats(f_id):
                user = session.get_user()
                
                reply = QMessageBox.question(self, "Клас обслуговування", "Бажаєте бізнес-клас (+50% до вартості)?", QMessageBox.Yes | QMessageBox.No)
                
                ticket_type = 1 if reply == QMessageBox.Yes else 0
                
                try:
                    base_price = float(self.price_label.text().split()[1])
                except:
                    base_price = 1000.0

                final_price = booking_system.calculate_ticket_price(base_price, ticket_type)
                
                ticket_name = "Bussines" if ticket_type == 1 else "Economy"
                
                db.add_ticket_purchase(user['id'], f_id, ticket_type, final_price)

                QMessageBox.information(self, "Успішно", 
                    f"Квиток ({ticket_name}) заброньовано!\n"
                    f"Пасажир: {user['Name']} {user['Surname']}\n"
                    f"До сплати: {final_price} UAH")
                window.show_user_info()
            else:
                QMessageBox.warning(self, "Помилка", "На жаль, місць більше немає.")
        else:
            QMessageBox.warning(self, "Увага", "Будь ласка, увійдіть у свій акаунт.")
            self.second_window = LoginWindow()
            self.second_window.exec()



class FlightPickDialog(QDialog, Ui_FlightPick):
    def __init__(self, from_city, to_city, flight_date):
        super().__init__()
        self.setupUi(self)
        self.from_city = from_city
        self.to_city = to_city
        self.flight_date = flight_date
        self.raw_sql_data = [] 


        btn_style = """
            QPushButton { 
                background-color: #e3f2fd; color: #1565c0; 
                border: 1px solid #1565c0; border-radius: 4px; padding: 6px; font-weight: bold; 
            } 
            QPushButton:hover { background-color: #bbdefb; }
            QPushButton:pressed { background-color: #90caf9; }
            QPushButton:disabled { background-color: #f0f0f0; color: #a0a0a0; border: 1px solid #d0d0d0; }
        """
        
        if hasattr(self, 'time_sort_btn'):
            self.time_sort_btn.setStyleSheet(btn_style)
            self.time_sort_btn.clicked.connect(self.apply_quicksort) 
            
        if hasattr(self, 'price_sort_btn'):
            self.price_sort_btn.setStyleSheet(btn_style)
            self.price_sort_btn.clicked.connect(self.apply_greedy)

        self.initial_search()

    def initial_search(self):
        results = db.find_flights(self.from_city, self.to_city, self.flight_date)
        if not results:
            results = db.find_flights(self.from_city, self.to_city, search_date=None)
        
        if results:
            self.raw_sql_data = results
            self.setWindowTitle(f"Рейси {self.from_city} → {self.to_city}")
            self.apply_quicksort() 
        else:
            self.try_find_transfer_route()

    def load_to_cpp_backend(self):
        if not self.raw_sql_data: return False
        
        booking_system.clear_flights()
        for row in self.raw_sql_data:
            f_time = str(row[7])
            booking_system.add_flight_from_python(
                int(row[0]), str(row[1]), str(row[2]), str(row[3]), 
                float(row[4]), int(row[5]), f_time
            )
        return True

    def apply_quicksort(self):
        if self.load_to_cpp_backend():
            sorted_flights = booking_system.get_all_flights_sorted()
            self.update_flight_list(sorted_flights)

    def apply_greedy(self):
        if self.load_to_cpp_backend():
            cheapest = booking_system.get_cheapest_flights(3)
            self.update_flight_list(cheapest)

    def try_find_transfer_route(self):
        print(f"Прямих немає. Запускаю Дейкстру...")
        
        all_flights = db.get_all_flights_raw()
        if not all_flights:
            QMessageBox.warning(self, "Пошук", "База рейсів порожня або немає з'єднання.")
            return

        booking_system.clear_flights()
        for row in all_flights:
            booking_system.add_flight_from_python(
                int(row[0]), str(row[1]), str(row[2]), str(row[3]), 
                float(row[4]), int(row[5]), str(row[7])
            )

        # Шукаємо маршрут
        route = booking_system.find_optimal_route(self.from_city, self.to_city, False)

        if route:
            total_price = sum(f.price for f in route)
            msg = (f"<span style='color:black; font-size:14px'>Прямих рейсів немає.<br>"
                   f"Знайдено маршрут з <b>{len(route)-1} пересадками</b>!<br>"
                   f"Загальна вартість: <b>{total_price} UAH</b></span>")
            
            QMessageBox.information(self, "Розумний пошук", msg)
            self.setWindowTitle(f"Маршрут з пересадками: {self.from_city} → {self.to_city}")
            
            if hasattr(self, 'time_sort_btn'): self.time_sort_btn.setEnabled(False)
            if hasattr(self, 'price_sort_btn'): self.price_sort_btn.setEnabled(False)
            
            self.update_flight_list(route)
        else:
            QMessageBox.warning(self, "Пошук", "На жаль, маршруту між цими містами не існує.")
            self.close()

    def update_flight_list(self, flights_list):
        list_widget = getattr(self, 'flightsListWidget', None)
        if not list_widget: return
        list_widget.clear()

        if not flights_list: return

        flight_date_str = self.flight_date if self.flight_date else "Дата у квитку"

        airplane_map = {}
        if self.raw_sql_data:
            for row in self.raw_sql_data:
                if len(row) >= 9: airplane_map[row[0]] = row[8]

        for i, flight_obj in enumerate(flights_list):
            
            a_id = airplane_map.get(flight_obj.id, None)
            
            flight_tuple = (
                flight_obj.id, 
                flight_obj.flight_number,
                flight_obj.origin, 
                flight_obj.destination, 
                flight_obj.price, 
                flight_obj.available_seats,
                flight_date_str, 
                flight_obj.time, 
                "00:00", 
                flight_obj.arrival_time,
                a_id
            )

            flight_widget = FlightItemWidget(flight_tuple)
            
            if len(flights_list) > 1 and flights_list[0].origin != flights_list[-1].destination:
                flight_widget.set_transfer_style(i + 1)

            list_item = QListWidgetItem()
            list_item.setSizeHint(flight_widget.sizeHint())
            
            list_widget.addItem(list_item)
            list_widget.setItemWidget(list_item, flight_widget)
            list_item.setData(Qt.UserRole, flight_obj.id)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        completer = QCompleter(materials.cities, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.from_edit.setCompleter(completer)
        self.to_edit.setCompleter(completer)
        self.to_edit.returnPressed.connect(self.search_flights)
        self.search_btn.clicked.connect(self.search_flights)
        
        self.sign_in_btn.clicked.connect(self.open_second_window)
        self.register_btn.clicked.connect(self.open_register_window)

        self.second_window = LoginWindow()
        self.register_window = RegWindow()

        self.show_user_info()
        self.init_hash_table()

    def init_hash_table(self):
        print("Завантаження пасажирів у хеш-таблицю C++...")
        passengers = db.get_all_passengers_raw()
        if passengers:
            for p in passengers:
                name = p[0] if p[0] else ""
                surname = p[1] if p[1] else ""
                email = p[2] if p[2] else ""
                passport = p[3] if p[3] else ""
                p_id = p[4] if p[4] else 0
                
                if passport:
                    booking_system.add_passenger_to_hash(name, surname, email, passport, p_id)
            print(f"Успішно захешовано {len(passengers)} пасажирів.")
        else:
            print("Список пасажирів порожній.")

    def search_flights(self):
        from_city = self.from_edit.text()
        to_city = self.to_edit.text()
        flight_data = self.date1.date().toString("yyyy-MM-dd")
        
        self.pick_flights = FlightPickDialog(from_city, to_city, flight_data)
        self.pick_flights.show()
        
        print(f"Шукаю рейси з {from_city} до {to_city}")

    def show_user_info(self):
        session = UserSession()
        if session.is_logged_in():
            user_session_data = session.get_user()
            passport_key = user_session_data['Passport']
            
            cpp_passenger = booking_system.find_passenger_by_passport(passport_key)
            
            if cpp_passenger.full_name != "Not Found":
                print(f"Дані користувача знайдено через C++ Hash Table: {cpp_passenger.full_name}")
                display_name = cpp_passenger.full_name
                display_email = cpp_passenger.email
                display_passport = cpp_passenger.passport
                user_id = cpp_passenger.ticket_id
            else:
                print("Користувача не знайдено в хеші (використовую сесію).")
                display_name = f"{user_session_data['Name']} {user_session_data['Surname']}"
                display_email = user_session_data['Email']
                display_passport = user_session_data['Passport']
                user_id = user_session_data['id']

            tickets = db.get_user_tickets(user_id)
            
            info = (
                f"👤 Профіль користувача:\n"
                f"🆔 ID: {user_id}\n"
                f"📛 Ім'я: {display_name}\n"
                f"📧 Email: {display_email}\n"
                f"🪪 Паспорт: {display_passport}\n"
                f"{'=' * 25}\n"
            )
            
            if tickets:
                info += f"🎫 ВАШІ КВИТКИ ({len(tickets)}):\n\n"
                for t in tickets:
                    dep_date = str(t[7]); dep_time = str(t[8])[:5]; buy_date = str(t[3])[:16]
                    info += f"✈️ Рейс {t[4]}: {t[5]} ➝ {t[6]}\n"
                    info += f"   📅 Виліт: {dep_date} о {dep_time}\n"
                    info += f"   💺 Клас: {t[1]} | 💰 Ціна: {t[2]} UAH\n"
                    info += f"   🛒 Куплено: {buy_date}\n{'-' * 30}\n"
            else:
                info += "\n📭 Історія покупок порожня."

            self.user_name.setText(f"✋ Привіт, {display_name}!")
            self.user_info_label.setText(info)
            self.sign_in_btn.hide(); self.register_btn.hide()
        else:
            self.sign_in_btn.show(); self.register_btn.show()


    def open_second_window(self):
        self.second_window.exec()

    def open_register_window(self):
        self.register_window.exec()

def start_gui():
    global window
    app = QApplication(sys.argv)
    if os.path.exists("pics/plane.ico"):
        app.setWindowIcon(QIcon("pics/plane.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())