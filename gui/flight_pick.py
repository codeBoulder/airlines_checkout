# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flight_pick.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_FlightPick(object):
    def setupUi(self, FlightPick):
        if not FlightPick.objectName():
            FlightPick.setObjectName(u"FlightPick")
        FlightPick.resize(781, 763)
        FlightPick.setStyleSheet(u"background-color: #e6f2ff;   /* \u043d\u0456\u0436\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u0438\u0439 */\n"
"")
        self.frame_2 = QFrame(FlightPick)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 771, 741))
        self.frame_2.setStyleSheet(u"background-color: white;      /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"\n"
"    border-radius: 15px; ")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.flightsListWidget = QListWidget(self.frame_2)
        self.flightsListWidget.setObjectName(u"flightsListWidget")
        self.flightsListWidget.setGeometry(QRect(30, 50, 721, 671))
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 10, 81, 21))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;       /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"}")
        self.price_sort_btn = QPushButton(self.frame_2)
        self.price_sort_btn.setObjectName(u"price_sort_btn")
        self.price_sort_btn.setGeometry(QRect(640, 10, 111, 41))
        self.price_sort_btn.setStyleSheet(u"QPushButton#price_sort_btn {\n"
"    background-color: #1e90ff;   /* \u0441\u0438\u043d\u0456\u0439 \u0444\u043e\u043d */\n"
"    color: white;                /* \u0431\u0456\u043b\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;          /* \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0456 \u043a\u0443\u0442\u0438 */\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton#price_sort_btn:hover {\n"
"    background-color: #f0f8ff;   /* \u0441\u0432\u0456\u0442\u043b\u043e-\u0433\u043e\u043b\u0443\u0431\u0438\u0439 \u0444\u043e\u043d */\n"
"	color: #1e90ff;\n"
"    border: 2px solid #5dade2;\n"
"}\n"
"\n"
"QPushButton#price_sort_btn:pressed {\n"
"    background-color: white;     /* \u0444\u043e\u043d \u0431\u0456\u043b\u0438\u0439 */\n"
"    color: #1e90ff;              /* \u0442\u0435\u043a\u0441\u0442 \u0441\u0438\u043d\u0456\u0439 */"
                        "\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"}")
        self.sign_in_btn_2 = QPushButton(self.frame_2)
        self.sign_in_btn_2.setObjectName(u"sign_in_btn_2")
        self.sign_in_btn_2.setGeometry(QRect(490, 20, 111, 41))
        self.sign_in_btn_2.setStyleSheet(u"QPushButton#sign_in_btn {\n"
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
        self.time_sort_btn = QPushButton(self.frame_2)
        self.time_sort_btn.setObjectName(u"time_sort_btn")
        self.time_sort_btn.setGeometry(QRect(510, 10, 111, 41))
        self.time_sort_btn.setStyleSheet(u"QPushButton#time_sort_btn {\n"
"    background-color: #1e90ff;   /* \u0441\u0438\u043d\u0456\u0439 \u0444\u043e\u043d */\n"
"    color: white;                /* \u0431\u0456\u043b\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;          /* \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0456 \u043a\u0443\u0442\u0438 */\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton#time_sort_btn:hover {\n"
"    background-color: #f0f8ff;   /* \u0441\u0432\u0456\u0442\u043b\u043e-\u0433\u043e\u043b\u0443\u0431\u0438\u0439 \u0444\u043e\u043d */\n"
"	color: #1e90ff;\n"
"    border: 2px solid #5dade2;\n"
"}\n"
"\n"
"QPushButton#time_sort_btn:pressed {\n"
"    background-color: white;     /* \u0444\u043e\u043d \u0431\u0456\u043b\u0438\u0439 */\n"
"    color: #1e90ff;              /* \u0442\u0435\u043a\u0441\u0442 \u0441\u0438\u043d\u0456\u0439 */\n"
""
                        "    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"}")

        self.retranslateUi(FlightPick)

        QMetaObject.connectSlotsByName(FlightPick)
    # setupUi

    def retranslateUi(self, FlightPick):
        FlightPick.setWindowTitle(QCoreApplication.translate("FlightPick", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("FlightPick", u"\u0420\u0435\u0439\u0441\u0438", None))
        self.price_sort_btn.setText(QCoreApplication.translate("FlightPick", u"\u0417\u0430 \u0446\u0456\u043d\u043e\u044e", None))
        self.sign_in_btn_2.setText(QCoreApplication.translate("FlightPick", u"\u0417\u0430 \u0446\u0456\u043d\u043e\u044e", None))
        self.time_sort_btn.setText(QCoreApplication.translate("FlightPick", u"\u0417\u0430 \u0447\u0430\u0441\u043e\u043c", None))
    # retranslateUi

