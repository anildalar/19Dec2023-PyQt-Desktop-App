import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()  
window.showMaximized()  # Show the window in a maximized state
window.setWindowTitle('QVBoxLayout')

iconCO = QIcon('./icon.png')
window.setWindowIcon(iconCO)

# co = ClassName()
# co.method()
button1 = QPushButton('Widget 1')
button2 = QPushButton('Widget 2')
button3 = QPushButton('Widget 3')
button4 = QPushButton('Widget 4')

layout = QVBoxLayout()

layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)

window.setLayout(layout)

window.show()

#window.showFullScreen()
# Start the event loop.
app.exec()
