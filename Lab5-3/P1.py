""" 
Darin Khamsawat
683040489-2
P1
"""
import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox,
    QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

from PySide6.QtCore import QLocale



class StudentGradeApp(QWidget):
    def __init__(self):
        super().__init__()



        self.setWindowTitle("Student Grade Calculator")
        self.resize(950, 550)

        self.students = {}
        self.load_students()

        self.setup_ui()
        self.apply_styles()


    def load_students(self):
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_path, "students.txt")

            if not os.path.exists(file_path):
                raise FileNotFoundError("students.txt not found")

            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(",")

                    if len(parts) >= 2:
                        student_id = parts[0].strip()
                        name = parts[1].strip()
                        self.students[student_id] = name

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            sys.exit()

    def setup_ui(self):
        main_layout = QVBoxLayout()

       
        top_layout = QHBoxLayout()

        self.combo_id = QComboBox()
        self.combo_id.addItems(sorted(self.students.keys()))
        self.combo_id.currentTextChanged.connect(self.show_name)

        self.label_name = QLabel("")
        self.label_name.setMinimumHeight(30)

        top_layout.addWidget(QLabel("Student ID:"))
        top_layout.addWidget(self.combo_id)
        top_layout.addWidget(QLabel("Student Name:"))
        top_layout.addWidget(self.label_name)

        
        score_layout = QHBoxLayout()

        self.spin_math = QSpinBox()
        self.spin_math.setLocale(QLocale(QLocale.Language.English, QLocale.Country.UnitedStates))
        self.spin_science = QSpinBox()
        self.spin_science.setLocale(QLocale(QLocale.Language.English, QLocale.Country.UnitedStates))
        self.spin_english = QSpinBox()
        self.spin_english.setLocale(QLocale(QLocale.Language.English, QLocale.Country.UnitedStates))

        for spin in [self.spin_math, self.spin_science, self.spin_english]:
            spin.setRange(0, 100)

        score_layout.addWidget(QLabel("Math:"))
        score_layout.addWidget(self.spin_math)
        score_layout.addWidget(QLabel("Science:"))
        score_layout.addWidget(self.spin_science)
        score_layout.addWidget(QLabel("English:"))
        score_layout.addWidget(self.spin_english)

        
        button_layout = QHBoxLayout()

        self.btn_add = QPushButton("Add Student")
        self.btn_reset = QPushButton("Reset Input")
        self.btn_clear = QPushButton("Clear All")

        self.btn_add.clicked.connect(self.add_student)
        self.btn_reset.clicked.connect(self.reset_input)
        self.btn_clear.clicked.connect(self.clear_table)
        self.btn_add.setFixedHeight(30)
        self.btn_reset.setFixedHeight(30)
        self.btn_clear.setFixedHeight(30)

        button_layout.addWidget(self.btn_add)
        button_layout.addWidget(self.btn_reset)
        button_layout.addWidget(self.btn_clear)

       
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Student ID", "Name",
            "Math", "Science", "English",
            "Total", "Average", "Grade"
        ])

        main_layout.addLayout(top_layout)
        main_layout.addLayout(score_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)
        self.show_name(self.combo_id.currentText())

    # -----------------------------
    def show_name(self, student_id):
        self.label_name.setText(self.students.get(student_id, ""))

    # -----------------------------
    def calculate_grade(self, avg):
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    # -----------------------------
    def add_student(self):
        student_id = self.combo_id.currentText()
        name = self.students[student_id]

        math = self.spin_math.value()
        science = self.spin_science.value()
        english = self.spin_english.value()

        total = math + science + english
        avg = total / 3
        grade = self.calculate_grade(avg)

        row = self.table.rowCount()
        self.table.insertRow(row)

        data = [
            student_id, name,
            str(math), str(science), str(english),
            str(total), f"{avg:.2f}", grade
        ]

        for col, value in enumerate(data):
            item = QTableWidgetItem(value)
            item.setTextAlignment(Qt.AlignCenter)

            if col in [2, 3, 4]:
                if int(value) < 50:
                    item.setBackground(QColor("#F66B78"))

            if col == 6:
                if float(value) < 50:
                    item.setBackground(QColor("#F66B78"))
           
            if col == 7:
                if grade == "A":
                    item.setBackground(QColor("#90EE93"))
                elif grade == "B":
                    item.setBackground(QColor("#9ACAF1"))
                elif grade == "C":
                    item.setBackground(QColor("#F5EDA7"))
                elif grade == "D":
                    item.setBackground(QColor("#F3AE45"))
                else:
                    item.setBackground(QColor("#F66B78"))

            self.table.setItem(row, col, item)

        self.table.sortItems(0)

    
    def reset_input(self):
        self.spin_math.setValue(0)
        self.spin_science.setValue(0)
        self.spin_english.setValue(0)

    def clear_table(self):
        self.table.setRowCount(0)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                font-size: 14px;
                color: black;
                background-color: #EAF6FF;            
                           
            }

            QLabel {
                font-weight: 500;
            }

            QComboBox, QSpinBox {
                padding: 6px;
                border: 1px solid #bbb;
                border-radius: 6px;
                background-color: #F6B1D7;
            }

            QPushButton {
                background-color: #EF69B3;
                color: black;
                padding: 8px;
                border-radius: 8px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #2563EB;
            }

            QTableWidget {
                background-color: white;
                gridline-color: #EAA3D6;
            }

            QHeaderView::section {
                background-color: #EAA3D6;
                padding: 6px;
                font-weight: bold;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentGradeApp()
    window.show()
    sys.exit(app.exec())