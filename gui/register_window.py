# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Registration(object):
    def setupUi(self, Registration):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(641, 631)
        Registration.setStyleSheet(u"background-color: #e6f2ff;")
        self.frame = QFrame(Registration)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 80, 561, 391))
        self.frame.setStyleSheet(u"background: white;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.profile_label = QLabel(self.frame)
        self.profile_label.setObjectName(u"profile_label")
        self.profile_label.setGeometry(QRect(60, 10, 221, 41))
        self.profile_label.setStyleSheet(u"QLabel {\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 20pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;       /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"}")
        self.reg_icon = QLabel(self.frame)
        self.reg_icon.setObjectName(u"reg_icon")
        self.reg_icon.setGeometry(QRect(10, 10, 41, 41))
        self.reg_icon.setPixmap(QPixmap(u"../../../Downloads/file_4512928.png"))
        self.reg_icon.setScaledContents(True)
        self.name_reg = QLineEdit(self.frame)
        self.name_reg.setObjectName(u"name_reg")
        self.name_reg.setGeometry(QRect(10, 60, 261, 41))
        self.name_reg.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;     /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #1e90ff;              /* \u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
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
        self.surname = QLineEdit(self.frame)
        self.surname.setObjectName(u"surname")
        self.surname.setGeometry(QRect(280, 60, 271, 41))
        self.surname.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;     /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #1e90ff;              /* \u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
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
        self.email_reg = QLineEdit(self.frame)
        self.email_reg.setObjectName(u"email_reg")
        self.email_reg.setGeometry(QRect(10, 110, 261, 41))
        self.email_reg.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;     /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #1e90ff;              /* \u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
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
        self.password_reg = QLineEdit(self.frame)
        self.password_reg.setObjectName(u"password_reg")
        self.password_reg.setGeometry(QRect(280, 110, 271, 41))
        self.password_reg.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;     /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #1e90ff;              /* \u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
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
        self.password_reg.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.birth_date = QDateEdit(self.frame)
        self.birth_date.setObjectName(u"birth_date")
        self.birth_date.setGeometry(QRect(10, 260, 151, 41))
        self.birth_date.setStyleSheet(u"QDateEdit {\n"
"    background-color: white;\n"
"    color: #1e90ff;\n"
"    font-size: 14pt;\n"
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
        self.profile_label_2 = QLabel(self.frame)
        self.profile_label_2.setObjectName(u"profile_label_2")
        self.profile_label_2.setGeometry(QRect(10, 220, 191, 26))
        self.profile_label_2.setStyleSheet(u"QLabel {\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 16pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;       /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"}")
        self.create_account_btn = QPushButton(self.frame)
        self.create_account_btn.setObjectName(u"create_account_btn")
        self.create_account_btn.setGeometry(QRect(180, 330, 191, 41))
        self.create_account_btn.setStyleSheet(u"QPushButton#create_account_btn {\n"
"    background-color: #1e90ff;   /* \u0441\u0438\u043d\u0456\u0439 \u0444\u043e\u043d */\n"
"    color: white;                /* \u0431\u0456\u043b\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;          /* \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0456 \u043a\u0443\u0442\u0438 */\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton#create_account_btn:hover {\n"
"    background-color: #f0f8ff;   /* \u0441\u0432\u0456\u0442\u043b\u043e-\u0433\u043e\u043b\u0443\u0431\u0438\u0439 \u0444\u043e\u043d */\n"
"	color: #1e90ff;\n"
"    border: 2px solid #5dade2;\n"
"}\n"
"\n"
"QPushButton#create_account_btn:pressed {\n"
"    background-color: white;     /* \u0444\u043e\u043d \u0431\u0456\u043b\u0438\u0439 */\n"
"    color: #1e90ff;              /* \u0442\u0435\u043a\u0441\u0442 \u0441\u0438\u043d\u0456"
                        "\u0439 */\n"
"    border: 2px solid #1e90ff;   /* \u0441\u0438\u043d\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"}")
        self.passport = QLineEdit(self.frame)
        self.passport.setObjectName(u"passport")
        self.passport.setGeometry(QRect(10, 160, 261, 41))
        self.passport.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;     /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #1e90ff;              /* \u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 14pt;\n"
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
        self.cloud2 = QLabel(Registration)
        self.cloud2.setObjectName(u"cloud2")
        self.cloud2.setGeometry(QRect(0, 20, 201, 161))
        self.cloud2.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud2.setScaledContents(True)
        self.cloud1 = QLabel(Registration)
        self.cloud1.setObjectName(u"cloud1")
        self.cloud1.setGeometry(QRect(400, 330, 201, 161))
        self.cloud1.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud1.setScaledContents(True)
        self.cloud1.raise_()
        self.cloud2.raise_()
        self.frame.raise_()

        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Register", None))
        self.profile_label.setText(QCoreApplication.translate("Registration", u"\u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0432\u0430\u0442\u0438\u0441\u044c", None))
        self.reg_icon.setText("")
        self.name_reg.setPlaceholderText(QCoreApplication.translate("Registration", u"\u0406\u043c'\u044f", None))
        self.surname.setPlaceholderText(QCoreApplication.translate("Registration", u"\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435", None))
        self.email_reg.setPlaceholderText(QCoreApplication.translate("Registration", u"Email", None))
        self.password_reg.setPlaceholderText(QCoreApplication.translate("Registration", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.profile_label_2.setText(QCoreApplication.translate("Registration", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f", None))
        self.create_account_btn.setText(QCoreApplication.translate("Registration", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u0430\u043a\u0430\u0443\u043d\u0442", None))
        self.passport.setPlaceholderText(QCoreApplication.translate("Registration", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.cloud2.setText("")
        self.cloud1.setText("")
    # retranslateUi

