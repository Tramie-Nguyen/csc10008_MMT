from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog


class HomePage_w(QMainWindow):
    def __init__(self):
        super(HomePage_w, self).__init__()
        uic.loadUi("templates/home_page.ui", self)
        self.chooseFileButton.clicked.connect(self.click_handler)

    def click_handler(self):
        dialog = QFileDialog()
        dialog.setNameFilter("All files (*.png, *.txt)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_success = dialog.exec()

        if dialog_success == 1:
            selected_file = dialog.selectedFiles()
            print(selected_file)
        else:
            print("User canceled opening the file dialog")
