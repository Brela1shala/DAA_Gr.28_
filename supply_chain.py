import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, 
                             QTextEdit, QMessageBox)
from PyQt6.QtCore import Qt
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value

class SupplyChainGUI(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Supply Chain Optimization")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

         # Button to generate tables
        generate_button = QPushButton("Generate Tables")
        generate_button.clicked.connect(self.generate_tables)
        main_layout.addWidget(generate_button)

        # Optimize button
        optimize_button = QPushButton("Optimize")
        optimize_button.clicked.connect(self.optimize)
        main_layout.addWidget(optimize_button)
         