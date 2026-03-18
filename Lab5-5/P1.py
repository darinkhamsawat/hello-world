""" 
Darin Khamsawat
683040489-2
P1
"""
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QDateEdit, 
                             QSpinBox, QPushButton, QStackedWidget, QFrame, 
                             QMessageBox, QGridLayout, QSpacerItem, QSizePolicy)
from PySide6.QtCore import Qt, QDate, Signal, Slot
from PySide6.QtGui import QFont

class RoomCard(QFrame):
   
    roomSelected = Signal(str, float)

    def __init__(self, name, price, description, emoji):
        super().__init__()
        self.room_name = name
        self.price = price
        self.is_selected = False
        
        self.setObjectName("roomCard")
        self.setFixedWidth(210)
        self.setMinimumHeight(260)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(8)

        # UI Elements
        self.icon_label = QLabel(emoji)
        self.icon_label.setFont(QFont("Segoe UI Emoji", 35))
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel(name)
        self.name_label.setFont(QFont("Arial", 11, QFont.Bold))
        self.name_label.setAlignment(Qt.AlignCenter)

        self.price_label = QLabel(f"${price} / night")
        self.price_label.setFont(QFont("Arial", 10))
        self.price_label.setAlignment(Qt.AlignCenter)

        self.desc_label = QLabel(description)
        self.desc_label.setWordWrap(True)
        self.desc_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setStyleSheet("color: #777; font-size: 11px;")

        self.select_btn = QPushButton("Select Room")
        self.select_btn.setCursor(Qt.PointingHandCursor)
        self.select_btn.clicked.connect(self.emit_selection)
        
        # Add to layout
        layout.addWidget(self.icon_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.price_label)
        layout.addWidget(self.desc_label)
        layout.addStretch()
        layout.addWidget(self.select_btn)

        self.update_appearance()

    def emit_selection(self):
        self.roomSelected.emit(self.room_name, self.price)

    def set_highlight(self, selected):
        self.is_selected = selected
        self.update_appearance()

    def update_appearance(self):
        if self.is_selected:
            self.setStyleSheet("""
                #roomCard { 
                    background-color: #e8f5e9; 
                    border: 3px solid #4caf50; 
                    border-radius: 15px; 
                }
            """)
            self.select_btn.setText("✓ Selected")
            self.select_btn.setStyleSheet("background-color: #4caf50; color: white; font-weight: bold; border-radius: 5px; padding: 5px;")
        else:
            self.setStyleSheet("""
                #roomCard { 
                    background-color: white; 
                    border: 1px solid #ddd; 
                    border-radius: 15px; 
                }
            """)
            self.select_btn.setText("Select Room")
            self.select_btn.setStyleSheet("background-color: #5c6bc0; color: white; border-radius: 5px; padding: 5px;")

# ---------------------------------------------------------
# MAIN APPLICATION WINDOW
# ---------------------------------------------------------
class CozyStayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CozyStay — Hotel Booking System")
        self.resize(1000, 750)
        self.setStyleSheet("background-color: #f4f6f9;")

        # Data storage
        self.booking_data = {}
        self.selected_room_name = None

        # Main Stacked Widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Create Pages
        self.setup_page1() # Booking Page
        self.setup_page2() # Review Page

    # --- PAGE 1: BOOKING ---
    def setup_page1(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 20, 40, 20)

        # Header
        header = QLabel("🏨 Book Your Stay at CozyStay")
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #1a237e;")
        layout.addWidget(header)
        layout.addWidget(QLabel("Fill in your details and choose your room"))
        layout.addSpacing(20)

        # Guest Info Section
        info_group = QFrame()
        info_group.setStyleSheet("background-color: white; border-radius: 10px; border: 1px solid #eee;")
        info_layout = QGridLayout(info_group)
        info_layout.setContentsMargins(20, 20, 20, 20)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("e.g. John Smith")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("e.g. 081-234-5678")

        # Dates as requested
        self.checkin_input = QDateEdit(QDate.currentDate())
        self.checkin_input.setDisplayFormat("dd/MM/yyyy")
        self.checkin_input.setCalendarPopup(True)

        self.checkout_input = QDateEdit(QDate.currentDate().addDays(1))
        self.checkout_input.setDisplayFormat("dd/MM/yyyy")
        self.checkout_input.setCalendarPopup(True)

        # Spinbox as requested
        self.guest_spin = QSpinBox()
        self.guest_spin.setRange(1, 10)
        self.guest_spin.setSuffix(" guest(s)")

        info_layout.addWidget(QLabel("Full Name :"), 0, 0)
        info_layout.addWidget(self.name_input, 0, 1)
        info_layout.addWidget(QLabel("Phone Number :"), 1, 0)
        info_layout.addWidget(self.phone_input, 1, 1)
        info_layout.addWidget(QLabel("Check-in Date :"), 2, 0)
        info_layout.addWidget(self.checkin_input, 2, 1)
        info_layout.addWidget(QLabel("Check-out Date :"), 3, 0)
        info_layout.addWidget(self.checkout_input, 3, 1)
        info_layout.addWidget(QLabel("Guests :"), 4, 0)
        info_layout.addWidget(self.guest_spin, 4, 1)

        layout.addWidget(QLabel("📂 Guest Information"))
        layout.addWidget(info_group)
        layout.addSpacing(20)

        # Room Selection
        layout.addWidget(QLabel("🛋️ Select a Room"))
        rooms_layout = QHBoxLayout()
        self.room_cards = [
            RoomCard("Standard Room", 50, "Single bed, Free Wi-Fi", "🛏️"),
            RoomCard("Deluxe Room", 120, "Double bed, Ocean view, Wi-Fi", "🌊"),
            RoomCard("Suite Room", 250, "Living room, Jacuzzi, Premium view", "👑"),
            RoomCard("Family Room", 160, "2 Bedrooms, Perfect for families", "👨‍👩‍👧‍👦")
        ]

        for card in self.room_cards:
            card.roomSelected.connect(self.on_room_clicked)
            rooms_layout.addWidget(card)
        
        layout.addLayout(rooms_layout)
        layout.addStretch()

        # Bottom Buttons
        btn_layout = QHBoxLayout()
        clear_btn = QPushButton("🗑️ Clear Info")
        clear_btn.clicked.connect(self.clear_fields)
        
        next_btn = QPushButton("Next →")
        next_btn.setFixedSize(120, 40)
        next_btn.setStyleSheet("background-color: #5c6bc0; color: white; font-weight: bold; border-radius: 8px;")
        next_btn.clicked.connect(self.go_to_review)

        btn_layout.addWidget(clear_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(next_btn)
        layout.addLayout(btn_layout)

        self.stack.addWidget(page)

    # --- PAGE 2: REVIEW ---
    def setup_page2(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 40, 40, 40)

        header = QLabel("📋 Booking Summary")
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #1a237e;")
        layout.addWidget(header)
        layout.addWidget(QLabel("Please review your details before confirming"))
        
        self.summary_card = QLabel()
        self.summary_card.setStyleSheet("background-color: white; border-radius: 15px; padding: 30px; font-size: 14px; border: 1px solid #ddd;")
        layout.addSpacing(20)
        layout.addWidget(self.summary_card)

        self.total_display = QLabel("Total Amount: $0")
        self.total_display.setAlignment(Qt.AlignRight)
        self.total_display.setStyleSheet("font-size: 22px; font-weight: bold; color: #3f51b5; padding-top: 20px;")
        layout.addWidget(self.total_display)
        
        layout.addStretch()

        btn_layout = QHBoxLayout()
        back_btn = QPushButton("← Back")
        back_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        confirm_btn = QPushButton("✓ Confirm Booking")
        confirm_btn.setFixedSize(180, 45)
        confirm_btn.setStyleSheet("background-color: #4caf50; color: white; font-weight: bold; border-radius: 8px;")
        confirm_btn.clicked.connect(self.confirm_booking)

        btn_layout.addWidget(back_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(confirm_btn)
        layout.addLayout(btn_layout)

        self.stack.addWidget(page)

 # --- LOGIC ---

    def on_room_clicked(self, name, price):
        self.selected_room_name = name
        self.selected_room_price = price
        for card in self.room_cards:
            card.set_highlight(card.room_name == name)

    def clear_fields(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.checkin_input.setDate(QDate.currentDate())
        self.checkout_input.setDate(QDate.currentDate().addDays(1))
        self.guest_spin.setValue(1)
        self.selected_room_name = None
        for card in self.room_cards:
            card.set_highlight(False)

    def go_to_review(self):
        # Validation
        if not self.name_input.text() or not self.selected_room_name:
            QMessageBox.warning(self, "Missing Info", "Please enter your name and select a room.")
            return
        
        if self.checkin_input.date() >= self.checkout_input.date():
            QMessageBox.warning(self, "Invalid Dates", "Check-out date must be after check-in date.")
            return

        # Calculate Nights and Total
        nights = self.checkin_input.date().daysTo(self.checkout_input.date())
        total = nights * self.selected_room_price

        # Update Review Page
        summary_text = f"""
        <b>Room:</b> &nbsp;&nbsp;&nbsp;&nbsp; {self.selected_room_name}<br><br>
        <b>Price / Night:</b> &nbsp;&nbsp;&nbsp;&nbsp; ${self.selected_room_price}<br><br>
        <b>Guest Name:</b> &nbsp;&nbsp;&nbsp;&nbsp; {self.name_input.text()}<br><br>
        <b>Phone:</b> &nbsp;&nbsp;&nbsp;&nbsp; {self.phone_input.text()}<br><br>
        <b>Check-in:</b> &nbsp;&nbsp;&nbsp;&nbsp; {self.checkin_input.date().toString('dd/MM/yyyy')}<br><br>
        <b>Check-out:</b> &nbsp;&nbsp;&nbsp;&nbsp; {self.checkout_input.date().toString('dd/MM/yyyy')}<br><br>
        <b>Nights:</b> &nbsp;&nbsp;&nbsp;&nbsp; {nights} night(s)<br><br>
        <b>Guests:</b> &nbsp;&nbsp;&nbsp;&nbsp; {self.guest_spin.value()} guest(s)
        """
        self.summary_card.setText(summary_text)
        self.total_display.setText(f"💳 Total Amount: ${total}")
        
        self.stack.setCurrentIndex(1)

    def confirm_booking(self):
        name = self.name_input.text()
        msg = QMessageBox(self)
        msg.setWindowTitle("Booking Confirmed")
        msg.setText(f"✅ <b>Booking Successful!</b><br><br>Dear {name},<br>Your {self.selected_room_name} is ready to welcome you! 🎉")
        msg.exec()
        
        # Go back to start and clear
        self.clear_fields()
        self.stack.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CozyStayApp()
    window.show()
    sys.exit(app.exec())   
        
 