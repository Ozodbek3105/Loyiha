import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QListWidget, QApplication, QLabel, QHBoxLayout, QStatusBar, QToolBar, \
    QMainWindow, QLineEdit


class Glossary_it(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IT Glossary")
        self.vertikal_layout = QHBoxLayout(self)
        self.list_widget = QListWidget(self)
        widget = QWidget(self)
        self.list_widget.itemSelectionChanged.connect(self.clicked)
        self.label = QLabel("")
        self.setFixedSize(700, 500)
        self.label.setFixedWidth(300)

        label_termini = QLabel("Terminlar")
        label_tarifi = QLabel("Tarifi")
        gorinantal_layout = QHBoxLayout()
        gorinantal_layout.addWidget(label_termini)
        gorinantal_layout.addWidget(label_tarifi)
        self.label.setStyleSheet(
            "font: 600 11pt 'Sitka Display Semibold';background-color:rgb(208, 208, 155); padding:10px")

        with open("glossary", "r") as file:
            for i in file.readlines():
                self.i = i.split("$")
                self.list_widget.addItem(f"{self.i[0]}")



        self.search_line = QLineEdit()
        self.search_line.setPlaceholderText("search")
        self.search_line.setFixedWidth(200)


        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))

        self.addToolBar(toolbar)
        button_action = QAction(QIcon("search.png"), "Your button", self)
        button_action.triggered.connect(self.search_click)

        toolbar.addWidget(self.search_line)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

        self.vertikal_layout.addWidget(self.list_widget)
        self.vertikal_layout.addWidget(self.label)
        self.setLayout(self.vertikal_layout)

        widget.setLayout(self.vertikal_layout)
        self.setCentralWidget(widget)

    def clicked(self):
        termin = self.list_widget.currentItem().text()
        with open("glossary", "r") as teore:
            for tegler in teore.readlines():
                if tegler.split("$")[0] in termin:
                    self.label.setText(tegler.split("$")[1])
                    self.label.setWordWrap(True)

    def search_click(self):
        if self.search_line.text() == "":
            with open("glossary", "r") as file:
                self.list_widget.clear()
                for i in file.readlines():
                    self.i = i.split("$")
                    self.list_widget.addItem(f"{self.i[0]}")
        else:
            with open("glossary", "r") as file:
                self.list_widget.clear()
                for i in file.readlines():
                    if self.search_line.text() in i.split('$')[0]:
                        self.list_widget.addItem(f"{i.split('$')[0]}")


app = QApplication(sys.argv)
window = Glossary_it()
window.show()
app.exec()
