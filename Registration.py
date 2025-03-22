import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
import os

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Account Registration')
        self.setGeometry(0, 0, 400, 300)

        self.set_background()

        self.set_icon()

        title_label = QLabel('Registration Form', self)
        title_label.move(150, 10)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: white;")

        labels = ['First Name:', 'Last Name:', 'Username:', 'Password:',
                  'Email Address:', 'Contact Number:']
        self.line_edits = []
        y_pos = 50

        for label_text in labels:
            label = QLabel(label_text, self)
            label.move(50, y_pos)
            label.setStyleSheet("color: white;")
            line_edit = QLineEdit(self)
            line_edit.move(150, y_pos)
            self.line_edits.append(line_edit)
            y_pos += 30

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.move(100, y_pos + 20)
        self.clear_button = QPushButton('Clear', self)
        self.clear_button.move(250, y_pos + 20)

        self.submit_button.clicked.connect(self.submit_data)
        self.clear_button.clicked.connect(self.clear_fields)

        self.center_window()

        self.show()

    def center_window(self):
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        size = QApplication.desktop().screenGeometry(screen)
        self.move(int((float(size.width()) - self.width()) / 2),
                  int((float(size.height()) - self.height()) / 2))

    def set_icon(self):
        icon_path = 'instagram_ig_logo_icon_181500.ico'
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found at: {icon_path}")

    def submit_data(self):
        data = {}
        for i, line_edit in enumerate(self.line_edits):
            data[i] = line_edit.text()

        if not all(data.values()):
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")
            return

        message = "\n".join([f"{i}: {value}" for i, value in data.items()])
        QMessageBox.information(self, "Submitted Data", message)

    def clear_fields(self):
        for line_edit in self.line_edits:
            line_edit.clear()

    def set_background(self):
        background_path = 'instagram-minimal-logo-3d-rendering_41204-3583.jpg'
        if os.path.exists(background_path):
            pixmap = QPixmap(background_path)
            palette = QPalette()
            palette.setBrush(QPalette.Background, QBrush(pixmap))
            self.setPalette(palette)
        else:
            print(f"Background image not found at: {background_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationForm()
    sys.exit(app.exec_())