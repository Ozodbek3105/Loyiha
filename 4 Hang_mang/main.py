from PySide6.QtWidgets import QApplication
# https://coderslegacy.com/add-image-data-files-in-pyinstaller-exe/

from HANGMANG_GAME.asosiyoyna import AsosiyOyna

app = QApplication()

window = AsosiyOyna(app)
window.show()

app.exec()
