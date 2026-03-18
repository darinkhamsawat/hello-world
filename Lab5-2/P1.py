""" 
Darin Khamsawat
683040489-2
P1
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QComboBox, QFormLayout, QGridLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: BMI Calculator")
        self.setFixedSize(380, 460)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(14)

        # Title Bar
        title = QLabel("Adult and Child BMI Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setStyleSheet("""
            background-color: #8B0000;
            color: white;
        """)
    
        title.setFixedHeight(25)
        main_layout.addWidget(title)

        # Form 
        form_layout = QFormLayout()

        self.age_combo = QComboBox()
        self.age_combo.addItems([
            "Adults 20+",
            "Children and Teenagers (5-19)"
        ])

        self.weight_input = QLineEdit()
        self.weight_unit = QComboBox()
        self.weight_unit.addItems(["kilograms", "pounds"])

        weight_layout = QHBoxLayout()
        weight_layout.addWidget(self.weight_input)
        weight_layout.addWidget(self.weight_unit)

        self.height_input = QLineEdit()
        self.height_unit = QComboBox()
        self.height_unit.addItems(["centimeters", "inches"])

        height_layout = QHBoxLayout()
        height_layout.addWidget(self.height_input)
        height_layout.addWidget(self.height_unit)

        form_layout.addRow("BMI age group:", self.age_combo)
        form_layout.addRow("Weight:", weight_layout)
        form_layout.addRow("Height:", height_layout)
    

        main_layout.addLayout(form_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        self.clear_btn = QPushButton("clear")
        self.submit_btn = QPushButton("Submit Registration")

        btn_layout.addWidget(self.clear_btn)
        btn_layout.addWidget(self.submit_btn)
        main_layout.addLayout(btn_layout)

        # Result Section 
        result_container = QWidget()
        result_container.setStyleSheet("background-color: #FAF0E6;")
        result_layout = QVBoxLayout()
        result_layout.setAlignment(Qt.AlignCenter)
        result_container.setFixedSize(360, 230)
       

        result_title = QLabel("Your BMI")
        result_title.setAlignment(Qt.AlignCenter)
        result_title.setStyleSheet("color: #000000;")

        self.bmi_label = QLabel("0.00")
        self.bmi_label.setAlignment(Qt.AlignCenter)
        self.bmi_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.bmi_label.setStyleSheet("color: #1E40AF;")

        self.condition_label = QLabel("")
        self.condition_label.setAlignment(Qt.AlignCenter)

        self.child_info = QLabel("")
        self.child_info.setAlignment(Qt.AlignCenter)
        self.child_info.setOpenExternalLinks(True)

        result_layout.addWidget(result_title)
        result_layout.addWidget(self.bmi_label)
        result_layout.addWidget(self.condition_label)
        result_layout.addWidget(self.child_info)

        # BMI Summary Table 
        self.table_widget = QWidget()
        table_layout = QGridLayout()
        

        header1 = QLabel("BMI")
        header1.setFont(QFont("Arial", 9, QFont.Bold))
        header2 = QLabel("Condition")
        header2.setFont(QFont("Arial", 9, QFont.Bold))

        table_layout.addWidget(header1, 0, 0)
        table_layout.addWidget(header2, 0, 1)

        table_layout.addWidget(QLabel("< 18.5"), 1, 0)
        table_layout.addWidget(QLabel("Thin"), 1, 1)

        table_layout.addWidget(QLabel("18.5 - 25.0"), 2, 0)
        table_layout.addWidget(QLabel("Normal"), 2, 1)

        table_layout.addWidget(QLabel("25.1 - 30.0"), 3, 0)
        table_layout.addWidget(QLabel("Overweight"), 3, 1)

        table_layout.addWidget(QLabel("> 30.0"), 4, 0)
        table_layout.addWidget(QLabel("Obese"), 4, 1)

        self.table_widget.setLayout(table_layout)
        self.table_widget.hide()  
        self.table_widget.setStyleSheet("color: #000000;")
        result_layout.addWidget(self.table_widget)

        result_container.setLayout(result_layout)
        
        main_layout.addWidget(result_container)

        self.setLayout(main_layout)

        # Connections 
        self.submit_btn.clicked.connect(self.calculate_bmi)
        self.clear_btn.clicked.connect(self.clear_fields)

    # Calculate BMI 
    def calculate_bmi(self):
     try:
        weight = float(self.weight_input.text())
        height = float(self.height_input.text())

        
        if weight <= 0 or height <= 0:
            self.bmi_label.setText("Error")
            self.condition_label.setText("Weight and Height must be > 0")
            self.child_info.setText("")
            self.table_widget.hide()
            return

        
        if self.weight_unit.currentText() == "kilograms":
            height_m = height / 100
            bmi = weight / (height_m ** 2)
        else:
            bmi = (weight / (height ** 2)) * 703

        self.bmi_label.setText(f"{bmi:.2f}")

        
        if self.age_combo.currentText() == "Adults 20+":
            self.child_info.setText("")
            self.table_widget.show()

            if bmi < 18.5:
                condition = "Thin"
            elif bmi <= 25:
                condition = "Normal"
            elif bmi <= 30:
                condition = "Overweight"
            else:
                condition = "Obese"

            self.condition_label.setText(condition)
            self.condition_label.setStyleSheet("color: #000000;")

        
        else:
            self.condition_label.setText("")
            self.table_widget.hide()
            self.child_info.setText(
                "For child's BMI interpretation, please click:<br>"
                "<a href='https://www.nhs.uk/'>BMI graph for BOYS</a> | "
                "<a href='https://www.nhs.uk/'>BMI graph for GIRLS</a>"
            )
            self.child_info.setStyleSheet("color: #000000;")

     except:
        self.bmi_label.setText("Error")
        self.condition_label.setText("Please enter valid numbers")
        self.child_info.setText("")
        self.table_widget.hide()
           

    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.bmi_label.setText("0.00")
        self.condition_label.setText("")
        self.child_info.setText("")
        self.table_widget.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())