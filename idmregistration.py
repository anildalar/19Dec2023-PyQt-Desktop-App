import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout,QGridLayout, QPushButton,QLabel, QWidget, QLineEdit
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()  
window.showMaximized()  # Show the window in a maximized state
window.setWindowTitle('QVBoxLayout')

iconCO = QIcon('./icon.png')
window.setWindowIcon(iconCO)

# co = ClassName()
# co.method()
button1 = QPushButton('OK')
button2 = QPushButton('How to License')
button3 = QPushButton('Cancel')

fname = QLabel("First Name")
lname = QLabel("Last Name")
email = QLabel("Email")
snumber = QLabel("Serial number")

fname_input = QLineEdit()
lname_input = QLineEdit()
email_input = QLineEdit()
snumber_input = QLineEdit()

layout = QGridLayout()

#layout.addWidget(fname,y,x)
layout.addWidget(fname,0,0)
layout.addWidget(fname_input,0,1)
layout.addWidget(lname,1,0)
layout.addWidget(lname_input,1,1)
layout.addWidget(email,2,0)
layout.addWidget(email_input,2,1)
layout.addWidget(snumber,3,0) 
layout.addWidget(snumber_input,3,1) 

window.setLayout(layout)

window.show()

#window.showFullScreen()
# Start the event loop.
app.exec()
