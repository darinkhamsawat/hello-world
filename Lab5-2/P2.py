""" 
Darin Khamsawat
683040489-2
P2
"""
import sys
import math
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QLineEdit, QPushButton
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(360, 520)

        self.expression = ""
        self.create_ui()

    def create_ui(self):
        main_layout = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(90)
        self.display.setFont(QFont("Segoe UI", 28))

        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #f3f3f3;
                border: none;
                padding: 15px;
                color: black;
            }
        """)

        main_layout.addWidget(self.display)

        grid = QGridLayout()
        grid.setSpacing(8)

        buttons = [
            ["%", "CE", "C", "<-"],
            ["1/x", "x^2", "sqrt", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="],
        ]

        for row, row_values in enumerate(buttons):
            for col, text in enumerate(row_values):
                button = QPushButton(text)
                button.setFixedSize(75, 65)
                button.setFont(QFont("Segoe UI", 14))

               
                if text.isdigit() or text == ".":
                 
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #ffffff;
                            color: black;
                            border: 1px solid #d6d6d6;
                            border-radius: 8px;
                        }
                        QPushButton:hover {
                            background-color: #eaeaea;
                        }
                    """)
                elif text == "=":
                   
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #0078D7;
                            color: white;
                            border: none;
                            border-radius: 8px;
                        }
                        QPushButton:hover {
                            background-color: #005A9E;
                        }
                    """)
                else:
                   
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #f0f0f0;
                            color: black;
                            border: 1px solid #d6d6d6;
                            border-radius: 8px;
                        }
                        QPushButton:hover {
                            background-color: #e0e0e0;
                        }
                    """)

                button.clicked.connect(self.button_clicked)
                grid.addWidget(button, row, col)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == "C":
            self.expression = ""
            self.display.setText("")

        elif text == "CE":
            self.expression = ""
            self.display.setText("")

        elif text == "<-":
            self.expression = self.expression[:-1]
            self.display.setText(self.expression)

        elif text == "=":
            try:
                result = str(eval(self.expression))
                self.display.setText(result)
                self.expression = result
            except:
                self.display.setText("Error")
                self.expression = ""

        elif text == "1/x":
            try:
                value = float(self.display.text())
                result = str(1 / value)
                self.display.setText(result)
                self.expression = result
            except:
                self.display.setText("Error")
                self.expression = ""

        elif text == "x^2":
            try:
                value = float(self.display.text())
                result = str(value ** 2)
                self.display.setText(result)
                self.expression = result
            except:
                self.display.setText("Error")
                self.expression = ""

        elif text == "sqrt":
            try:
                value = float(self.display.text())
                result = str(math.sqrt(value))
                self.display.setText(result)
                self.expression = result
            except:
                self.display.setText("Error")
                self.expression = ""

        elif text == "+/-":
            try:
                value = float(self.display.text())
                result = str(-value)
                self.display.setText(result)
                self.expression = result
            except:
                self.display.setText("Error")
                self.expression = ""

        else:
            self.expression += text
            self.display.setText(self.expression)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())