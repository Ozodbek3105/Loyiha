from PySide6.QtCore import Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton


class Klaviatura(QVBoxLayout):
    bosildi = Signal(str)

    def __init__(self):
        super().__init__()

        gorizontal_1 = QHBoxLayout()
        gorizontal_2 = QHBoxLayout()
        gorizontal_3 = QHBoxLayout()
        self.addLayout(gorizontal_1)
        self.addLayout(gorizontal_2)
        self.addLayout(gorizontal_3)

        self.tugmalar = {}

        for harflar, joy in {"qwertyuiop": gorizontal_1, "asdfghjkl": gorizontal_2, "zxcvbnm": gorizontal_3}.items():
            for harf in harflar:
                self.tugmalar[harf] = QPushButton(harf)
                self.tugmalar[harf].setObjectName("klaviatura")
                joy.addWidget(self.tugmalar[harf])
                # self.tugmalar[harf].setFixedSize(QSize(50, 50))
                joy.setAlignment(Qt.AlignmentFlag.AlignCenter)
                # joy.setSpacing(10)
                self.tugmalar[harf].clicked.connect(self.bosilganda(self.tugmalar[harf]))

    def boshlangich_holatga_otkaz(self):
        for harf, button in self.tugmalar.items():
            button.setObjectName("klaviatura")
            button.setDisabled(False)

    def bosilganda(self, button: QPushButton):

        def harfni_yubor(val):
            # Signal yuborish 👇
            self.bosildi.emit(button.text())

        return harfni_yubor

    def xatoga_ozgartir(self, text):
        self.tugmalar[text].setObjectName("xato")
        self.tugmalar[text].setDisabled(True)

    def togriga_ozgartir(self, text):
        self.tugmalar[text].setObjectName("togri")
        self.tugmalar[text].setDisabled(True)
