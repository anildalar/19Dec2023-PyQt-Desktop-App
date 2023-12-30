#import moduleName
import sys # sys is a builtin module
import uuid # uuid is a builtin python module
import requests # requests is a 3rd party module
import requests1 # requests1 is userDefined module
import sqlite3 # sql


from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout,QGridLayout, QPushButton,QLabel, QWidget, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon # PyQt6 is a 3rd party module,
conn = sqlite3.connect('anil.db')
cursor = conn.cursor()

# Create a table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        sno TEXT NOT NULL
    )
""")
conn.commit() # Execute/Perform the SQL query



#2. Function callingg
#print(anilLaptopHardwareId())

#1. Function defination is one time process
def anil(msg): # msg is a formal arguement
    co = QMessageBox()
    co.setText(msg)
    co.exec()
    pass

def sendData():
    print("Inside sendData function")
    data = {
                "firstname": fname_input.text(),
                "lastname": lname_input.text(),
                "email": email_input.text(),
                "serial_number": snumber_input.text()
            }
    cursor.execute(
                    "INSERT INTO users (first_name,last_name,email,sno) VALUES (?, ?, ?, ?)",
                    (data["firstname"], data["lastname"], data["email"], data["serial_number"])
                  )
    conn.commit()
    QMessageBox.information(None, "Success", "Data saved successfully")
    pass


# 1 Function defination
def anilLaptopHardwareId():
   #ceo         = module.ClassName(keyWordArgument=Value)
    hardware_id = uuid.UUID(int=uuid.getnode()).hex[-12:]
    # Every function return something
    return hardware_id
    pass



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



#widget.signal.connect(slot_function)
button1.clicked.connect(sendData)




window.show()

#window.showFullScreen()
# Start the event loop.
app.exec()
