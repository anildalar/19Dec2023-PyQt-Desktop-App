import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)

window = QMainWindow()  
window.showMaximized()  # Show the window in a maximized state
window.setWindowTitle('OKLABS Cacluator')

iconCO = QIcon('./icon.png')
window.setWindowIcon(iconCO)

menubar = window.menuBar()
calculator_menu = menubar.addMenu('Calculator')
standar_menu = calculator_menu.addMenu("Standard")
standar_submen_menu = standar_menu.addMenu("Standard Ka Submenu")
standar_submen_submenu_menu = standar_submen_menu.addMenu("Standard Ke Submenu Ka Submen")

calculator_menu = menubar.addMenu('Converter')
calculator_menu = menubar.addMenu('Settings')
#window.showFullScreen()
# Start the event loop.
app.exec()
