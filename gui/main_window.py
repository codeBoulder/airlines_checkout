# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 844)
        MainWindow.setStyleSheet(u"background-color: #e6f2ff;   /* \u043d\u0456\u0436\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u0438\u0439 */\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 70, 951, 141))
        self.frame.setStyleSheet(u"background-color: white;      /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"\n"
"    border-radius: 15px; ")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.search_btn = QPushButton(self.frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(850, 40, 79, 71))
        self.search_btn.setStyleSheet(u"QPushButton#search_btn {\n"
"    background-color: white;     /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #1e90ff;              /* \u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14px;             /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;           /* \u0436\u0438\u0440\u043d\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;          /* \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0456 \u043a\u0443\u0442\u0438 */\n"
"    padding: 6px 12px;           /* \u0432\u043d\u0443\u0442\u0440\u0456\u0448\u043d\u0456 \u0432\u0456\u0434\u0441\u0442\u0443\u043f\u0438 */\n"
"}\n"
"\n"
"QPushButton#search_btn:hover {\n"
"    background-color: #f0f8ff;   /* \u043b\u0435\u0433\u043a\u0438\u0439 \u0433\u043e\u043b\u0443\u0431\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435"
                        "\u0434\u0435\u043d\u043d\u0456 */\n"
"}\n"
"\n"
"QPushButton#search_btn:pressed {\n"
"    background-color: #1e90ff;   /* \u0444\u043e\u043d \u0441\u0442\u0430\u0454 \u0441\u0438\u043d\u0456\u043c */\n"
"    color: white;                /* \u0442\u0435\u043a\u0441\u0442 \u0441\u0442\u0430\u0454 \u0431\u0456\u043b\u0438\u0439 */\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../Downloads/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QSize(35, 35))
        self.date1 = QDateEdit(self.frame)
        self.date1.setObjectName(u"date1")
        self.date1.setGeometry(QRect(450, 80, 141, 41))
        self.date1.setStyleSheet(u"QDateEdit {\n"
"    background-color: white;\n"
"    color: #1e90ff;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1e90ff;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"/* \u041d\u0430\u0432\u0435\u0434\u0435\u043d\u043d\u044f */\n"
"QDateEdit:hover {\n"
"    background-color: #f0f8ff;\n"
"}\n"
"\n"
"/* \u0424\u043e\u043a\u0443\u0441 */\n"
"QDateEdit:focus {\n"
"    border: 2px solid #104e8b;\n"
"    background-color: #e6f2ff;\n"
"}\n"
"\n"
"/* \u041f\u0440\u0438\u0431\u0438\u0440\u0430\u0454\u043c\u043e \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0438\u0439 drop-down */\n"
"QDateEdit::drop-down {\n"
"    border: none;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QDateEdit::up-button, \n"
"QDateEdit::down-button {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: none;\n"
"}")
        self.date1_label = QLabel(self.frame)
        self.date1_label.setObjectName(u"date1_label")
        self.date1_label.setGeometry(QRect(460, 50, 74, 28))
        self.date1_label.setStyleSheet(u"QLabel {\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;       /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"}")
        self.date2 = QDateEdit(self.frame)
        self.date2.setObjectName(u"date2")
        self.date2.setGeometry(QRect(600, 80, 141, 41))
        self.date2.setStyleSheet(u"QDateEdit {\n"
"    background-color: white;\n"
"    color: #1e90ff;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1e90ff;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"/* \u041d\u0430\u0432\u0435\u0434\u0435\u043d\u043d\u044f */\n"
"QDateEdit:hover {\n"
"    background-color: #f0f8ff;\n"
"}\n"
"\n"
"/* \u0424\u043e\u043a\u0443\u0441 */\n"
"QDateEdit:focus {\n"
"    border: 2px solid #104e8b;\n"
"    background-color: #e6f2ff;\n"
"}\n"
"\n"
"/* \u041f\u0440\u0438\u0431\u0438\u0440\u0430\u0454\u043c\u043e \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0438\u0439 drop-down */\n"
"QDateEdit::drop-down {\n"
"    border: none;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QDateEdit::up-button, \n"
"QDateEdit::down-button {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: none;\n"
"}")
        self.date2_label = QLabel(self.frame)
        self.date2_label.setObjectName(u"date2_label")
        self.date2_label.setGeometry(QRect(610, 50, 121, 28))
        self.date2_label.setStyleSheet(u"QLabel {\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;       /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"}")
        self.from_edit = QLineEdit(self.frame)
        self.from_edit.setObjectName(u"from_edit")
        self.from_edit.setGeometry(QRect(10, 80, 200, 41))
        self.from_edit.setMinimumSize(QSize(150, 0))
        self.from_edit.setMaximumSize(QSize(200, 16777215))
        self.from_edit.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;     /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #1e90ff;              /* \u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QLineEdit:focus {\n"
"    background-color: #f0f8ff;   /* \u043b\u0435\u0433\u043a\u0438\u0439 \u0433\u043e\u043b\u0443\u0431\u0438\u0439 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0456 */\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: #f0f8ff;   /* \u043b\u0435\u0433\u043a\u0438\u0439 \u0433\u043e\u043b\u0443\u0431\u0438\u0439 */\n"
"}\n"
"")
        self.to_edit = QLineEdit(self.frame)
        self.to_edit.setObjectName(u"to_edit")
        self.to_edit.setGeometry(QRect(220, 80, 201, 41))
        self.to_edit.setMinimumSize(QSize(150, 0))
        self.to_edit.setMaximumSize(QSize(250, 16777215))
        self.to_edit.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;     /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #1e90ff;              /* \u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QLineEdit:focus {\n"
"    background-color: #f0f8ff;   /* \u043b\u0435\u0433\u043a\u0438\u0439 \u0433\u043e\u043b\u0443\u0431\u0438\u0439 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0456 */\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: #f0f8ff;   /* \u043b\u0435\u0433\u043a\u0438\u0439 \u0433\u043e\u043b\u0443\u0431\u0438\u0439 */\n"
"}\n"
"")
        self.date1_label_2 = QLabel(self.frame)
        self.date1_label_2.setObjectName(u"date1_label_2")
        self.date1_label_2.setGeometry(QRect(70, 30, 74, 28))
        self.date1_label_2.setStyleSheet(u"QLabel {\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 18pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;       /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 31, 31))
        self.label_2.setPixmap(QPixmap(u"../pics/icons8-airplane-64.png"))
        self.label_2.setScaledContents(True)
        self.company_name = QLabel(self.centralwidget)
        self.company_name.setObjectName(u"company_name")
        self.company_name.setGeometry(QRect(20, 20, 161, 41))
        self.company_name.setStyleSheet(u"QLabel#company_name {\n"
"    color: #1565c0;              /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 */\n"
"    font-size: 24pt;             /* \u0432\u0435\u043b\u0438\u043a\u0438\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-weight: bold;           /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"    qproperty-alignment: 'AlignCenter'; /* \u043f\u043e \u0446\u0435\u043d\u0442\u0440\u0443 */\n"
"}")
        self.icon = QLabel(self.centralwidget)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(180, 20, 41, 41))
        self.icon.setPixmap(QPixmap(u"../../../Downloads/plane.png"))
        self.icon.setScaledContents(True)
        self.cloud1 = QLabel(self.centralwidget)
        self.cloud1.setObjectName(u"cloud1")
        self.cloud1.setGeometry(QRect(-10, -40, 201, 161))
        self.cloud1.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud1.setScaledContents(True)
        self.cloud3 = QLabel(self.centralwidget)
        self.cloud3.setObjectName(u"cloud3")
        self.cloud3.setGeometry(QRect(520, -30, 201, 161))
        self.cloud3.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud3.setScaledContents(True)
        self.cloud2 = QLabel(self.centralwidget)
        self.cloud2.setObjectName(u"cloud2")
        self.cloud2.setGeometry(QRect(210, 110, 201, 161))
        self.cloud2.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud2.setScaledContents(True)
        self.cloud4 = QLabel(self.centralwidget)
        self.cloud4.setObjectName(u"cloud4")
        self.cloud4.setGeometry(QRect(850, 100, 201, 161))
        self.cloud4.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud4.setScaledContents(True)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 230, 421, 571))
        self.frame_2.setStyleSheet(u"background-color: white;      /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"\n"
"    border-radius: 15px; ")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.sign_in_btn = QPushButton(self.frame_2)
        self.sign_in_btn.setObjectName(u"sign_in_btn")
        self.sign_in_btn.setGeometry(QRect(40, 60, 111, 41))
        self.sign_in_btn.setStyleSheet(u"QPushButton#sign_in_btn {\n"
"    background-color: #1e90ff;   /* \u0441\u0438\u043d\u0456\u0439 \u0444\u043e\u043d */\n"
"    color: white;                /* \u0431\u0456\u043b\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;          /* \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0456 \u043a\u0443\u0442\u0438 */\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton#sign_in_btn:hover {\n"
"    background-color: #f0f8ff;   /* \u0441\u0432\u0456\u0442\u043b\u043e-\u0433\u043e\u043b\u0443\u0431\u0438\u0439 \u0444\u043e\u043d */\n"
"	color: #1e90ff;\n"
"    border: 2px solid #5dade2;\n"
"}\n"
"\n"
"QPushButton#sign_in_btn:pressed {\n"
"    background-color: white;     /* \u0444\u043e\u043d \u0431\u0456\u043b\u0438\u0439 */\n"
"    color: #1e90ff;              /* \u0442\u0435\u043a\u0441\u0442 \u0441\u0438\u043d\u0456\u0439 */\n"
"    "
                        "border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"}")
        self.register_btn = QPushButton(self.frame_2)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(160, 60, 191, 41))
        self.register_btn.setStyleSheet(u"QPushButton#register_btn {\n"
"    background-color: #1e90ff;   /* \u0441\u0438\u043d\u0456\u0439 \u0444\u043e\u043d */\n"
"    color: white;                /* \u0431\u0456\u043b\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;          /* \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0456 \u043a\u0443\u0442\u0438 */\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton#register_btn:hover {\n"
"    background-color: #f0f8ff;   /* \u0441\u0432\u0456\u0442\u043b\u043e-\u0433\u043e\u043b\u0443\u0431\u0438\u0439 \u0444\u043e\u043d */\n"
"	color: #1e90ff;\n"
"    border: 2px solid #5dade2;\n"
"}\n"
"\n"
"QPushButton#register_btn:pressed {\n"
"    background-color: white;     /* \u0444\u043e\u043d \u0431\u0456\u043b\u0438\u0439 */\n"
"    color: #1e90ff;              /* \u0442\u0435\u043a\u0441\u0442 \u0441\u0438\u043d\u0456\u0439 */\n"
" "
                        "   border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"}")
        self.profile_label = QLabel(self.frame_2)
        self.profile_label.setObjectName(u"profile_label")
        self.profile_label.setGeometry(QRect(60, 20, 131, 26))
        self.profile_label.setStyleSheet(u"QLabel {\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;       /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"}")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 31, 31))
        self.label_6.setStyleSheet(u"background: white;")
        self.label_6.setPixmap(QPixmap(u"../../../Downloads/avatar_11598848.png"))
        self.label_6.setScaledContents(True)
        self.user_name = QLabel(self.frame_2)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setGeometry(QRect(20, 50, 381, 51))
        self.user_name.setStyleSheet(u"QLabel {\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 16pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;       /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"}")
        self.user_name.setWordWrap(True)
        self.user_info_label = QTextEdit(self.frame_2)
        self.user_info_label.setObjectName(u"user_info_label")
        self.user_info_label.setGeometry(QRect(20, 120, 381, 431))
        self.user_info_label.setStyleSheet(u"\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"")
        self.user_info_label.setReadOnly(True)
        self.user_name.raise_()
        self.sign_in_btn.raise_()
        self.register_btn.raise_()
        self.profile_label.raise_()
        self.label_6.raise_()
        self.user_info_label.raise_()
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(580, 240, 401, 541))
        self.stackedWidget.setStyleSheet(u"background: white;\n"
"border-radius: 15px; ")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 521))
        self.label.setPixmap(QPixmap(u"../../../Downloads/main_pic_1.png"))
        self.label.setScaledContents(True)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.cloud2_2 = QLabel(self.centralwidget)
        self.cloud2_2.setObjectName(u"cloud2_2")
        self.cloud2_2.setGeometry(QRect(440, 350, 201, 161))
        self.cloud2_2.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud2_2.setScaledContents(True)
        self.cloud2_3 = QLabel(self.centralwidget)
        self.cloud2_3.setObjectName(u"cloud2_3")
        self.cloud2_3.setGeometry(QRect(670, 660, 201, 161))
        self.cloud2_3.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud2_3.setScaledContents(True)
        self.cloud2_4 = QLabel(self.centralwidget)
        self.cloud2_4.setObjectName(u"cloud2_4")
        self.cloud2_4.setGeometry(QRect(40, 510, 201, 161))
        self.cloud2_4.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud2_4.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.cloud2_4.raise_()
        self.cloud2_3.raise_()
        self.cloud2_2.raise_()
        self.cloud4.raise_()
        self.cloud2.raise_()
        self.cloud3.raise_()
        self.cloud1.raise_()
        self.frame.raise_()
        self.company_name.raise_()
        self.icon.raise_()
        self.frame_2.raise_()
        self.stackedWidget.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ariline_checkout", None))
        self.search_btn.setText("")
        self.date1_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043b\u0456\u0442", None))
        self.date2_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0435\u043d\u043d\u044f", None))
        self.from_edit.setText("")
        self.from_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u043d\u043a\u0442 \u0432\u0456\u0434\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044f", None))
        self.to_edit.setText("")
        self.to_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u043d\u043a\u0442 \u043f\u0440\u0438\u0431\u0443\u0442\u0442\u044f", None))
        self.date1_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0439\u0441\u0438", None))
        self.label_2.setText("")
        self.company_name.setText(QCoreApplication.translate("MainWindow", u"AeroNova", None))
        self.icon.setText("")
        self.cloud1.setText("")
        self.cloud3.setText("")
        self.cloud2.setText("")
        self.cloud4.setText("")
        self.sign_in_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0456\u0439\u0442\u0438", None))
        self.register_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0432\u0430\u0442\u0438\u0441\u044f", None))
        self.profile_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448 \u043f\u0440\u043e\u0444\u0456\u043b\u044c", None))
        self.label_6.setText("")
        self.user_name.setText("")
        self.label.setText("")
        self.cloud2_2.setText("")
        self.cloud2_3.setText("")
        self.cloud2_4.setText("")
    # retranslateUi

