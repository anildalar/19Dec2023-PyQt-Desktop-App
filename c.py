

from PyQt6.QtWidgets import QLabel,QComboBox,QLineEdit,QGridLayout,QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget




app = QApplication([])
#ceo = ClassName()
btn1 = QPushButton('1')
btn2 = QPushButton('2')
btn3 = QPushButton('3')
btn4 = QPushButton('4')
btn5 = QPushButton('5')
btn6 = QPushButton('6')
btn7 = QPushButton('7')
btn8 = QPushButton('8')
btn9 = QPushButton('9')
btn0 = QPushButton('0')

num1 = QLineEdit()
num2 = QLineEdit()

result = QLabel("Hello") # Global variable


#ceo = ClassName()
operator = QComboBox() # +,-,*. /
#ceo.method(aa1)
operator.addItems(["+","-","*","/"])

btnplus = QPushButton('+')
btnequalto = QPushButton('=')

window = QWidget()

layout = QGridLayout() # using QGrideLayout

#ceo.method(actualArgument1,actualArgument2,...)
layout.addWidget(num1,0,0)
layout.addWidget(operator,0,1)
layout.addWidget(num2,0,3)
layout.addWidget(btnequalto,1,0)
layout.addWidget(result,1,1)
window.setLayout(layout)

#widget.signal.connect(slot_function)
def anil():
    print(num1.text())
    print(operator.currentText())
    print(num2.text())
    n1 = float(num1.text())
    op = operator.currentText()
    n2 = float(num2.text())
    
    print(n1)
    if op == '-':
        rst = n1-n2
        
        print(f" {n1} {op} {n2} = {rst}")
        result.setText(str(rst))
    
    
    pass
btnequalto.clicked.connect(anil)
window.show()
app.exec()