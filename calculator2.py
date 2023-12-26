#import area
import sys
#from topmodule.submodule import elim1,elim2,elim3,...
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit


#1. Class Defination
class CalculatorApp(QWidget):
    def __init__(self): #CIO
        super().__init__()

        self.setWindowTitle('Abhishek Calculator') # Set the window title

        self.setup_ui()

        self.current_expression = ''

    def setup_ui(self):# snake_case
        layout = QGridLayout() # using QGrideLayout

        display = QLineEdit(self)
        layout.addWidget(display, 0, 0, 1, 4)

        buttons = [ '7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', '.', '=', '+']

        row, col = 1, 0 # these are all  local varible
        for button in buttons: # for singular in plural:
            button = self.create_button(button)
            button.clicked.connect(self.handle_button_click)
            layout.addWidget(button, row, col)
            #layout.addWidget(button, y, x)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.setLayout(layout)

    def create_button(self, text): #this function returning a co
        
        # every function return somethign
        return QPushButton(text, self)

    def handle_button_click(self):
        clicked_button = self.sender()
        button_text = clicked_button.text()

        if button_text == '=': # if statement
            try:
                result = eval(self.current_expression)
                self.current_expression = str(result)
            except Exception as e:
                self.current_expression = 'Error'
        else: # else statement
            self.current_expression += button_text

        self.findChild(QLineEdit, '').setText(self.current_expression)


app = QApplication(sys.argv)
#ceo = ClassName()
calc_app = CalculatorApp()
calc_app.show()


sys.exit(app.exec())
