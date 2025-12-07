class materials:
    cities = [
    "Львів", "Київ", "Варшава", "Берлін", "Лондон", 
    "Париж", "Амстердам", "Рим", "Барселона", "Стамбул", 
    "Мадрид", "Франкфурт", "Мюнхен", "Відень", "Цюрих", 
    "Копенгаген", "Лісабон", "Прага", "Афіни", "Дубай"
    ]

    normal_style = """
        QLineEdit {
            background-color: white;
            color: #1e90ff;             
            font-size: 14pt;
            font-weight: bold;
            border: 2px solid #1e90ff;
            border-radius: 8px;
            padding: 6px 12px;
        }
        QLineEdit:focus {
            background-color: #f0f8ff;
        }
        QLineEdit:hover {
            background-color: #f0f8ff;
        }
        """

    error_style = """
            QLineEdit {
                background-color: #fff4f4;      
                border: 2px solid #d32f2f;
                color: #b71c1c;
                font-size: 14pt;
                font-weight: bold;
                border: 2px solid #1e90ff;
                border-radius: 8px;
                padding: 6px 12px;
            }
            QLineEdit:hover {
                background-color: #ffeaea;
            }
            QLineEdit:focus {
                background-color: #fffafa;
                border: 2px solid #ef5350;
            }
        """