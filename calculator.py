import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()  
window.showMaximized()  # Show the window in a maximized state
window.setWindowTitle('QHBoxLayout')

iconCO = QIcon('./icon.png')
window.setWindowIcon(iconCO)

""" menubar = window.menuBar()
calculator_menu = menubar.addMenu('Calculator')
standar_menu = calculator_menu.addMenu("Standard")
standar_submen_menu = standar_menu.addMenu("Standard Ka Submenu")
standar_submen_submenu_menu = standar_submen_menu.addMenu("Standard Ke Submenu Ka Submen")

calculator_menu = menubar.addMenu('Converter')
calculator_menu = menubar.addMenu('Settings') """

# co = ClassName()
# co.method()
button1 = QPushButton('Widget 1')
button2 = QPushButton('Widget 2')
button3 = QPushButton('Widget 3')
button4 = QPushButton('Widget 4')

layout = QHBoxLayout()

layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)

window.setLayout(layout)

window.show()

#window.showFullScreen()
# Start the event loop.
app.exec()
