import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QComboBox, QSpinBox, QCheckBox, 
                             QPushButton, QGroupBox, QMessageBox)

class DataEntryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Entry Form')
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        # User Information
        user_group = QGroupBox("User Information")
        user_layout = QVBoxLayout()

        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("First Name"))
        self.first_name_edit = QLineEdit()
        name_layout.addWidget(self.first_name_edit)
        name_layout.addWidget(QLabel("Last Name"))
        self.last_name_edit = QLineEdit()
        name_layout.addWidget(self.last_name_edit)
        name_layout.addWidget(QLabel("Title"))
        self.title_combo = QComboBox()
        self.title_combo.addItems(["Mr.", "Mrs.", "Ms.", "Dr."])
        name_layout.addWidget(self.title_combo)
        user_layout.addLayout(name_layout)

        other_layout = QHBoxLayout()
        other_layout.addWidget(QLabel("Age"))
        self.age_spin = QSpinBox()
        self.age_spin.setValue(18)
        other_layout.addWidget(self.age_spin)
        other_layout.addWidget(QLabel("Nationality"))
        self.nationality_edit = QLineEdit()
        other_layout.addWidget(self.nationality_edit)
        user_layout.addLayout(other_layout)

        user_group.setLayout(user_layout)
        layout.addWidget(user_group)

        # Registration Status
        reg_group = QGroupBox("Registration Status")
        reg_layout = QVBoxLayout()
        self.registered_check = QCheckBox("Currently Registered")
        reg_layout.addWidget(self.registered_check)
        
        courses_layout = QHBoxLayout()
        courses_layout.addWidget(QLabel("# Completed Courses"))
        self.courses_spin = QSpinBox()
        courses_layout.addWidget(self.courses_spin)
        reg_layout.addLayout(courses_layout)

        semesters_layout = QHBoxLayout()
        semesters_layout.addWidget(QLabel("# Semesters"))
        self.semesters_spin = QSpinBox()
        semesters_layout.addWidget(self.semesters_spin)
        reg_layout.addLayout(semesters_layout)

        reg_group.setLayout(reg_layout)
        layout.addWidget(reg_group)

        # Terms & Conditions
        terms_group = QGroupBox("Terms & Conditions")
        terms_layout = QVBoxLayout()
        self.terms_check = QCheckBox("I accept the terms and conditions.")
        terms_layout.addWidget(self.terms_check)
        terms_group.setLayout(terms_layout)
        layout.addWidget(terms_group)

        # Submit Button
        submit_button = QPushButton("Enter data")
        submit_button.clicked.connect(self.submit_data)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submit_data(self):
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()
        title = self.title_combo.currentText()
        age = self.age_spin.value()
        nationality = self.nationality_edit.text()
        registered = self.registered_check.isChecked()
        completed_courses = self.courses_spin.value()
        semesters = self.semesters_spin.value()
        accepted_terms = self.terms_check.isChecked()

        if not accepted_terms:
            QMessageBox.warning(self, "Warning", "You must accept the terms and conditions to proceed.")
            return

        # Print data to console (or handle data as needed)
        print(f"Name: {title} {first_name} {last_name}")
        print(f"Age: {age}")
        print(f"Nationality: {nationality}")
        print(f"Registered: {registered}")
        print(f"Completed Courses: {completed_courses}")
        print(f"Semesters: {semesters}")
        print(f"Accepted Terms: {accepted_terms}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataEntryForm()
    ex.show()
    sys.exit(app.exec_())
