#import moduleName
import sys # sys is a builtin module
import requests # requests is a 3rd party module
import requests1 # requests1 is userDefined module
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout,QGridLayout, QPushButton,QLabel, QWidget, QLineEdit
from PyQt6.QtGui import QIcon # PyQt6 is a 3rd party module

#co = ClassName(actualArgument will go inside constructor)
app = QApplication(sys.argv)

window = QWidget()  
#window.showMaximized()  # Show the window in a maximized state
window.setWindowTitle('QVBoxLayout')

iconCO = QIcon('./icon.png')
window.setWindowIcon(iconCO)

# co = ClassName()
# co.method()
button1 = QPushButton('Save')
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
layout.addWidget(button1,4,0) 

window.setLayout(layout)


def sendData():
    print("Inside sendData function")
    payload = {
        "data": {
            "firstname": fname_input.text(),
            "lastname": lname_input.text(),
            "email": email_input.text(),
            "sno": snumber_input.text()
        }
    }

    api_url = 'http://localhost:1337/api/registrations'
    #module.member
    #response1 = requests1.post('url1',json='payload') # actualarg1,actualarg2
    #print(response1)
    response = requests.post(api_url, json=payload)
    
    pass


#widget.signal.connect(slot_function)
button1.clicked.connect(sendData)



window.show()

#window.showFullScreen()
# Start the event loop.
app.exec()
