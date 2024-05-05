import os
import sys
from random import choice

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, Qt, QPixmap, QKeyEvent, QFont
from PySide6.QtWidgets import QGridLayout, QLabel, QWidget, \
    QMessageBox, QApplication, QVBoxLayout

from klaviatura import Klaviatura


def resource_path(relative_path):
    """ .py va .exe ikkala holatda ishlaydigan qilish """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)


class AsosiyOyna(QWidget):

    def __init__(self, app: QApplication):

        self.app = app
        super().__init__()
        self.xatolar = 0
        self.foydalanuvchi_harflar = []
        self.mevalar = ['banan', 'anor', 'gilos', 'olma', 'ananas', ]
        self.texnika = ['moshina', 'traktor', 'velosiped']
        self.sabzavot = ['sabzi', 'bodring', 'pomidor', 'piyoz', 'kartoshka']
        self.setFixedSize(QSize(580, 494))
        self.setWindowIcon(QIcon(resource_path("../../Loyiha/4 Hang_mang/images/hangman.ico")))
        self.setWindowTitle("HANGMAN")
        self.setObjectName("asosiy")

        self.grid = QGridLayout()
        self.label_savol = QLabel("Mevalar!!!")
        self.label_savol.setFixedSize(350, 30)
        self.label_savol.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label_savol.setFont(QFont("Arial black", 14))
        self.label_savol.setStyleSheet("color:white;")
        # Hamma qlabel widgetlarni orqa foni qizil bo'lsin
        # Bu vaqtinchalik, keyin o'chirib tashlaymiz
        self.rasm_lbl = QLabel(self)  # rasm uchun
        self.rasm_lbl.setScaledContents(True)
        self.rasm_lbl.setFixedSize(QSize(200, 300))
        self.ver_layout = QVBoxLayout()
        self.soz_lbl = QLabel(self)  # soz uchun

        self.soz_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.soz_lbl.setObjectName("yozuv")
        self.stilni_yangila()
        self.ver_layout.addWidget(self.label_savol)
        self.ver_layout.addWidget(self.soz_lbl)
        self.grid.addWidget(self.rasm_lbl, 0, 0)
        self.grid.addLayout(self.ver_layout, 0, 1)

        # oynaga gridLayout ni o'rnatish
        self.setLayout(self.grid)
        self.tasodifiy_soz_tanla()
        self.rasmni_korsat()
        self.klaviaturani_joyla()

    def stilni_yangila(self):
        self.setStyleSheet(open(resource_path("../../Loyiha/4 Hang_mang/images/style.css")).read())

    def tasodifiy_soz_tanla(self):
        self.nimaga_oid = choice([self.mevalar, self.texnika, self.sabzavot])
        if self.nimaga_oid == self.mevalar:
            self.label_savol.setText("Mevalarga oid")
            self.tasodifiy_soz = choice(self.mevalar)
        elif self.nimaga_oid == self.texnika:
            self.label_savol.setText("Texnikaga oid")
            self.tasodifiy_soz = choice(self.texnika)
        else:
            self.label_savol.setText("Sabzavotga oid")
            self.tasodifiy_soz = choice(self.sabzavot)
        self.sozni_korsat()

    def rasmni_korsat(self):
        pixmap = QPixmap(resource_path(f'../../Loyiha/4 Hang_mang/images/stage{self.xatolar + 1}.png' ))
        self.rasm_lbl.setPixmap(pixmap)

    def klaviaturani_joyla(self):
        self.klaviatura = Klaviatura()
        self.grid.addLayout(self.klaviatura, 1, 0, 1, 2)
        self.klaviatura.bosildi.connect(self.klaviatura_bosildi)

    def qayt_ishga_tushir(self):
        self.xatolar = 0
        self.foydalanuvchi_harflar.clear()
        self.rasmni_korsat()
        self.tasodifiy_soz_tanla()
        self.klaviatura.boshlangich_holatga_otkaz()
        self.stilni_yangila()

    def keyPressEvent(self, event: QKeyEvent) -> None:

        self.klaviatura_bosildi(event.text())

    def klaviatura_bosildi(self, text: str):

        self.foydalanuvchi_harflar.append(text)

        if text not in self.tasodifiy_soz:
            self.xatolar += 1
            self.klaviatura.xatoga_ozgartir(text)
            self.rasmni_korsat()
            self.sozni_korsat()
            self.stilni_yangila()
            if self.xatolar == 5:
                self.habar_ber("Yutqazdingiz. Yana o'ynaysizmi?")
        else:
            self.klaviatura.togriga_ozgartir(text)
            self.sozni_korsat()
            self.stilni_yangila()
            if "+" not in self.soz_lbl.text():
                self.habar_ber("Yutdingiz. Yana o'ynaysizmi?")

    def habar_ber(self, habar):
        javob = QMessageBox.question(self, "Savol", habar)

        if javob == QMessageBox.Yes:
            self.qayt_ishga_tushir()
        else:
            self.app.quit()

    def sozni_korsat(self):

        soz = ""
        for harf in self.tasodifiy_soz:
            if harf in self.foydalanuvchi_harflar:
                soz += harf
            else:
                soz += '+'
        self.soz_lbl.setText(soz)
