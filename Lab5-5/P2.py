""" 
Darin Khamsawat
683040489-2
P2
"""
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QComboBox, 
                             QPushButton, QStackedWidget, QFrame, QScrollArea)
from PySide6.QtCore import Qt, Signal, QMimeData
from PySide6.QtGui import QFont, QDrag

# --- Custom Student Card with Delete and Drag/Drop ---
class StudentCard(QFrame):
    delete_clicked = Signal(int)

    def __init__(self, data, index):
        super().__init__()
        self.data = data
        self.index = index
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.StyledPanel)
        self.setMinimumHeight(120)
        self.setStyleSheet("""
            QFrame { background-color: #fce4ec; border-radius: 5px; border: none; margin: 5px; }
            QLabel { color: #333; }
        """)

        layout = QHBoxLayout(self)
        
        # Drag handle
        handle = QLabel("⋮⋮")
        handle.setFixedWidth(20)
        handle.setStyleSheet("color: #aaa; font-size: 18px;")
        layout.addWidget(handle)

        # Info column
        info_layout = QVBoxLayout()
        name_lbl = QLabel(f"<b>{data['first_name']} {data['last_name']}</b> <font color='#888'>{data['id']}</font>")
        major_lbl = QLabel(f"{data['faculty']} · {data['major']}")
        courses = [data[f'c{i}'] for i in range(1, 4) if data[f'c{i}']]
        courses_lbl = QLabel("\n".join(courses))
        courses_lbl.setStyleSheet("font-size: 10px; color: #555;")
        
        info_layout.addWidget(name_lbl)
        info_layout.addWidget(major_lbl)
        info_layout.addWidget(courses_lbl)
        layout.addLayout(info_layout)
        
        # Delete button
        del_btn = QPushButton("×")
        del_btn.setFixedSize(30, 30)
        del_btn.setStyleSheet("background: transparent; color: #888; font-size: 20px; border: none;")
        del_btn.setCursor(Qt.PointingHandCursor)
        del_btn.clicked.connect(lambda: self.delete_clicked.emit(self.index))
        layout.addWidget(del_btn, alignment=Qt.AlignTop)

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            mime.setText(str(self.index))
            drag.setMimeData(mime)
            drag.exec(Qt.MoveAction)

class RegistrationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Name: Your Name | Student ID: 12345678
        self.setWindowTitle("Student Registration")
        self.setFixedSize(800, 600)
        
        self.students = []
        self.temp_form = {}
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        self.setup_page1_list()
        self.setup_page2_form()
        self.setup_page3_review()
        
    def setup_page1_list(self):
        self.p1 = QWidget()
        layout = QVBoxLayout(self.p1)
        
        header = QHBoxLayout()
        self.count_lbl = QLabel("Students <font color='#888'>0 enrolled</font>")
        self.count_lbl.setFont(QFont("Arial", 14, QFont.Bold))
        add_btn = QPushButton("+ Add Student")
        add_btn.setStyleSheet("background: #3b82f6; color: white; padding: 8px 15px; border-radius: 5px;")
        add_btn.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        
        header.addWidget(self.count_lbl)
        header.addStretch()
        header.addWidget(add_btn)
        layout.addLayout(header)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.list_container = QWidget()
        self.list_layout = QVBoxLayout(self.list_container)
        self.list_layout.setAlignment(Qt.AlignTop)
        self.scroll.setWidget(self.list_container)
        layout.addWidget(self.scroll)
        
        self.stack.addWidget(self.p1)

    def setup_page2_form(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 20, 40, 20)
        
        layout.addWidget(QLabel("<h2>Add Student</h2>"))
        
        # Fields
        self.inputs = {
            'id': QLineEdit(), 'first': QLineEdit(), 'last': QLineEdit(),
            'faculty': QLineEdit(), 'major': QLineEdit()
        }
        self.inputs['id'].setPlaceholderText("e.g. 65010001")
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("PERSONAL INFORMATION"))
        for key, widget in self.inputs.items():
            form_layout.addWidget(QLabel(key.capitalize() + " *"))
            form_layout.addWidget(widget)
            
        self.courses = [QComboBox() for _ in range(3)]
        course_list = ["", "CS101 Intro", "CS102 Data Structures", "CS202 Database", "MATH101 Calculus"]
        for cb in self.courses: 
            cb.addItems(course_list)
            form_layout.addWidget(cb)
            
        layout.addLayout(form_layout)
        
        self.error_lbl = QLabel("")
        self.error_lbl.setStyleSheet("color: red;")
        layout.addWidget(self.error_lbl)
        
        btns = QHBoxLayout()
        cancel_btn = QPushButton("← Cancel")
        cancel_btn.clicked.connect(self.cancel_form)
        review_btn = QPushButton("Review →")
        review_btn.clicked.connect(self.go_to_review)
        btns.addWidget(cancel_btn); btns.addStretch(); btns.addWidget(review_btn)
        layout.addLayout(btns)
        
        self.stack.addWidget(page)

    def setup_page3_review(self):
        self.p3 = QWidget()
        self.p3_layout = QVBoxLayout(self.p3)
        self.stack.addWidget(self.p3)

    def go_to_review(self):
        data = {k: v.text() for k, v in self.inputs.items()}
        data['c1'] = self.courses[0].currentText()
        data['c2'] = self.courses[1].currentText()
        data['c3'] = self.courses[2].currentText()
        
        if not all(data[k] for k in self.inputs) or not data['c1']:
            self.error_lbl.setText("Required: ID, Names, Faculty, Major, at least 1 course")
            return
            
        self.temp_form = data
        self.update_review_page()
        self.stack.setCurrentIndex(2)

    def update_review_page(self):
        # Implementation of summary labels...
        self.stack.setCurrentIndex(2) # Placeholder for UI logic

    def cancel_form(self):
        for i in self.inputs.values(): i.clear()
        self.stack.setCurrentIndex(0)

    # Simplified refresh for Page 1
    def refresh_list(self):
        while self.list_layout.count():
            self.list_layout.takeAt(0).widget().deleteLater()
        for i, s in enumerate(self.students):
            card = StudentCard(s, i)
            card.delete_clicked.connect(self.remove_student)
            self.list_layout.addWidget(card)
        self.count_lbl.setText(f"Students <font color='#888'>{len(self.students)} enrolled</font>")

    def remove_student(self, index):
        self.students.pop(index)
        self.refresh_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationApp()
    window.show()
    sys.exit(app.exec())