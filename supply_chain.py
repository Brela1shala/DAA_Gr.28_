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
         
        # Results display
        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        main_layout.addWidget(self.results_display)

        def get_table_data(self, table):
        rows = table.rowCount()
        cols = table.columnCount()
        data = []
        for i in range(rows):
            row_data = []
            for j in range(cols):
                item = table.item(i, j)
                row_data.append(int(item.text()) if item else 0)
            data.append(row_data)
        return data
 
 def create_input_field(self, label_text, layout):
        label = QLabel(label_text)
        input_field = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(input_field)
        return input_field

    def create_table(self, title):
        table = QTableWidget()
        table.setHorizontalHeaderLabels([title])
        return table

    def generate_tables(self):
        try:
            num_factories = int(self.factory_input.text())
            num_warehouses = int(self.warehouse_input.text())
            num_stores = int(self.store_input.text())

            self.setup_table(self.factory_capacities_table, num_factories, 1)
            self.setup_table(self.store_demands_table, num_stores, 1)
            self.setup_table(self.factory_to_warehouse_cost_table, num_factories, num_warehouses)
            self.setup_table(self.warehouse_to_store_cost_table, num_warehouses, num_stores)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers for factories, warehouses, and stores.")

    def setup_table(self, table, rows, cols):
        table.setRowCount(rows)
        table.setColumnCount(cols)
        for i in range(rows):
            for j in range(cols):
                table.setItem(i, j, QTableWidgetItem("0"))def setup_table(self, table, rows, cols):
        table.setRowCount(rows)
        table.setColumnCount(cols)
        for i in range(rows):
            for j in range(cols):
                table.setItem(i, j, QTableWidgetItem("0"))

# Input fields for number of factories, warehouses, and stores
        input_layout = QHBoxLayout()
        self.factory_input = self.create_input_field("Number of Factories:", input_layout)
        self.warehouse_input = self.create_input_field("Number of Warehouses:", input_layout)
        self.store_input = self.create_input_field("Number of Stores:", input_layout)
        main_layout.addLayout(input_layout)
def optimize(self):
        try:
            num_factories = int(self.factory_input.text())
            num_warehouses = int(self.warehouse_input.text())
            num_stores = int(self.store_input.text())

            factory_capacities = self.get_table_data(self.factory_capacities_table)
            warehouse_to_store_demand = self.get_table_data(self.store_demands_table)
            factory_to_warehouse_cost = self.get_table_data(self.factory_to_warehouse_cost_table)
            warehouse_to_store_cost = self.get_table_data(self.warehouse_to_store_cost_table)

            # Ensure factory_capacities and warehouse_to_store_demand are 1D lists
            if isinstance(factory_capacities[0], list):
                factory_capacities = [row[0] for row in factory_capacities]
            if isinstance(warehouse_to_store_demand[0], list):
                warehouse_to_store_demand = [row[0] for row in warehouse_to_store_demand]

# Tables for input data
        self.factory_capacities_table = self.create_table("Factory Capacities")
        self.store_demands_table = self.create_table("Store Demands")
        self.factory_to_warehouse_cost_table = self.create_table("Factory to Warehouse Cost")
        self.warehouse_to_store_cost_table = self.create_table("Warehouse to Store Cost")

        main_layout.addWidget(self.factory_capacities_table)
        main_layout.addWidget(self.store_demands_table)
        main_layout.addWidget(self.factory_to_warehouse_cost_table)
        main_layout.addWidget(self.warehouse_to_store_cost_table)
