# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(442, 665)
        MainWindow.setStyleSheet(u"background-color: rgb(180, 178, 170);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_c = QPushButton(self.centralwidget)
        self.btn_c.setObjectName(u"btn_c")
        font = QFont()
        font.setPointSize(20)
        self.btn_c.setFont(font)
        self.btn_c.setStyleSheet(u"background-color: rgb(241, 159, 88);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 30px;")

        self.gridLayout.addWidget(self.btn_c, 7, 1, 1, 2)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 30px;")

        self.gridLayout.addWidget(self.btn_0, 6, 1, 1, 2)

        self.btn_bolish = QPushButton(self.centralwidget)
        self.btn_bolish.setObjectName(u"btn_bolish")
        self.btn_bolish.setFont(font)
        self.btn_bolish.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_bolish, 6, 4, 1, 1)

        self.btn_nuqta = QPushButton(self.centralwidget)
        self.btn_nuqta.setObjectName(u"btn_nuqta")
        self.btn_nuqta.setFont(font)
        self.btn_nuqta.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_nuqta, 6, 3, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_4, 3, 1, 1, 1)

        self.btn_kopaytr = QPushButton(self.centralwidget)
        self.btn_kopaytr.setObjectName(u"btn_kopaytr")
        self.btn_kopaytr.setFont(font)
        self.btn_kopaytr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_kopaytr, 5, 4, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_3, 5, 1, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_1, 5, 3, 1, 1)

        self.btn_eval = QPushButton(self.centralwidget)
        self.btn_eval.setObjectName(u"btn_eval")
        self.btn_eval.setFont(font)
        self.btn_eval.setStyleSheet(u"background-color: rgb(241, 159, 88);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 30px;")

        self.gridLayout.addWidget(self.btn_eval, 7, 3, 1, 2)

        self.btn_qosh = QPushButton(self.centralwidget)
        self.btn_qosh.setObjectName(u"btn_qosh")
        self.btn_qosh.setFont(font)
        self.btn_qosh.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_qosh, 0, 4, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_5, 3, 2, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_7, 0, 1, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_6, 3, 3, 1, 1)

        self.btn_ayir = QPushButton(self.centralwidget)
        self.btn_ayir.setObjectName(u"btn_ayir")
        self.btn_ayir.setFont(font)
        self.btn_ayir.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_ayir, 3, 4, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_8, 0, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_9, 0, 3, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 15px;")

        self.gridLayout.addWidget(self.btn_2, 5, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: black;\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 10px;")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        font1 = QFont()
        font1.setPointSize(25)
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"background-color: rgb(57, 57, 57);\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 5px;\n"
"")
        self.label_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_1, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_bolish.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_nuqta.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_kopaytr.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_eval.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_qosh.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_ayir.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

