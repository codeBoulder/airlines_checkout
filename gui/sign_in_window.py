# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_in_window.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_SignIn(object):
    def setupUi(self, SignIn):
        if not SignIn.objectName():
            SignIn.setObjectName(u"SignIn")
        SignIn.resize(601, 469)
        SignIn.setStyleSheet(u"background-color: #e6f2ff;   /* \u043d\u0456\u0436\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u0438\u0439 */")
        self.frame_2 = QFrame(SignIn)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(120, 120, 361, 201))
        self.frame_2.setStyleSheet(u"background-color: white;      /* \u0431\u0456\u043b\u0438\u0439 \u0444\u043e\u043d */\n"
"\n"
"    border-radius: 15px; ")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 10, 31, 31))
        self.label_6.setStyleSheet(u"background: white;")
        self.label_6.setPixmap(QPixmap(u"../../../Downloads/avatar_11598848.png"))
        self.label_6.setScaledContents(True)
        self.sign_in_label2 = QLabel(self.frame_2)
        self.sign_in_label2.setObjectName(u"sign_in_label2")
        self.sign_in_label2.setGeometry(QRect(100, 10, 191, 26))
        self.sign_in_label2.setStyleSheet(u"QLabel {\n"
"    color: #1565c0;          /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0456\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 16pt;         /* \u0440\u043e\u0437\u043c\u0456\u0440 \u0448\u0440\u0438\u0444\u0442\u0443 */\n"
"    font-weight: bold;       /* \u0436\u0438\u0440\u043d\u0438\u0439 */\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u043e\u0440\u0438\u0439 \u0444\u043e\u043d */\n"
"}")
        self.email_sign_in = QLineEdit(self.frame_2)
        self.email_sign_in.setObjectName(u"email_sign_in")
        self.email_sign_in.setGeometry(QRect(10, 50, 340, 41))
        self.email_sign_in.setMinimumSize(QSize(150, 0))
        self.email_sign_in.setMaximumSize(QSize(340, 16777215))
        self.email_sign_in.setStyleSheet(u"QLineEdit {\n"
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
        self.password_sign_in = QLineEdit(self.frame_2)
        self.password_sign_in.setObjectName(u"password_sign_in")
        self.password_sign_in.setGeometry(QRect(10, 100, 340, 41))
        self.password_sign_in.setMinimumSize(QSize(150, 0))
        self.password_sign_in.setMaximumSize(QSize(340, 16777215))
        self.password_sign_in.setStyleSheet(u"QLineEdit {\n"
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
        self.password_sign_in.setEchoMode(QLineEdit.EchoMode.Password)
        self.sign_in_btn = QPushButton(self.frame_2)
        self.sign_in_btn.setObjectName(u"sign_in_btn")
        self.sign_in_btn.setGeometry(QRect(130, 150, 111, 41))
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
        self.cloud1 = QLabel(SignIn)
        self.cloud1.setObjectName(u"cloud1")
        self.cloud1.setGeometry(QRect(20, 20, 201, 161))
        self.cloud1.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud1.setScaledContents(True)
        self.cloud2 = QLabel(SignIn)
        self.cloud2.setObjectName(u"cloud2")
        self.cloud2.setGeometry(QRect(370, 10, 201, 161))
        self.cloud2.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud2.setScaledContents(True)
        self.cloud3 = QLabel(SignIn)
        self.cloud3.setObjectName(u"cloud3")
        self.cloud3.setGeometry(QRect(260, 250, 201, 161))
        self.cloud3.setPixmap(QPixmap(u"../../../Downloads/cloud-computing.png"))
        self.cloud3.setScaledContents(True)
        self.cloud3.raise_()
        self.cloud2.raise_()
        self.cloud1.raise_()
        self.frame_2.raise_()

        self.retranslateUi(SignIn)

        QMetaObject.connectSlotsByName(SignIn)
    # setupUi

    def retranslateUi(self, SignIn):
        SignIn.setWindowTitle(QCoreApplication.translate("SignIn", u"Sign In", None))
        self.label_6.setText("")
        self.sign_in_label2.setText(QCoreApplication.translate("SignIn", u"\u0423\u0432\u0456\u0439\u0434\u0456\u0442\u044c \u0432 \u0430\u043a\u0430\u0443\u043d\u0442", None))
        self.email_sign_in.setText("")
        self.email_sign_in.setPlaceholderText(QCoreApplication.translate("SignIn", u"Email", None))
        self.password_sign_in.setText("")
        self.password_sign_in.setPlaceholderText(QCoreApplication.translate("SignIn", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.sign_in_btn.setText(QCoreApplication.translate("SignIn", u"\u0423\u0432\u0456\u0439\u0442\u0438", None))
        self.cloud1.setText("")
        self.cloud2.setText("")
        self.cloud3.setText("")
    # retranslateUi

