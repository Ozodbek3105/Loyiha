from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton

from calc import Ui_MainWindow


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_1.clicked.connect(self.btn_clicked)
        self.btn_2.clicked.connect(self.btn_clicked)
        self.btn_3.clicked.connect(self.btn_clicked)
        self.btn_4.clicked.connect(self.btn_clicked)
        self.btn_5.clicked.connect(self.btn_clicked)
        self.btn_6.clicked.connect(self.btn_clicked)
        self.btn_7.clicked.connect(self.btn_clicked)
        self.btn_8.clicked.connect(self.btn_clicked)
        self.btn_9.clicked.connect(self.btn_clicked)
        self.btn_c.clicked.connect(self.btn_clicked)
        self.btn_0.clicked.connect(self.btn_clicked)
        self.btn_ayir.clicked.connect(self.btn_clicked)
        self.btn_qosh.clicked.connect(self.btn_clicked)
        self.btn_nuqta.clicked.connect(self.btn_clicked)
        self.btn_bolish.clicked.connect(self.btn_clicked)
        self.btn_kopaytr.clicked.connect(self.btn_clicked)
        self.btn_eval.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        button: QPushButton = self.sender()
        text = self.label_1.text()
        self.label_1.setText(text + button.text())
        # if text[-1] in ["+","-","/","*"]:
        #     self.label_1.setText(text)
        if text == "0":
            self.label_1.setText(button.text())
        if text in ["ZeroDivisionError","SyntaxError"]:
            self.label_1.setText(button.text())
        if button.text() == "C":
            self.label_1.setText("0")
        if button.text() == "=":
            try:
                natija = eval(text)
                self.label_1.setText(str(natija))
                self.label_2.setText(str(natija))
            except ZeroDivisionError:
                self.label_1.setText("ZeroDivisionError")
            except SyntaxError:
                self.label_1.setText("SyntaxError")

