import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore
 
import Ui_main
 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main.Ui_Form()
        self.ui.setupUi(self)

    @QtCore.Slot()
    def on_pushButton_clicked(self):
        print("pushButton clicked")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win  = MainWindow()
    win.show()
    sys.exit(app.exec())