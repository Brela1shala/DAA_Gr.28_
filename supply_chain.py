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