from traceback import print_tb
#import python.py
#import python2.py
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import subprocess as s


app = QApplication([])
window = QMainWindow()
window.setFixedSize(400, 160)
window.setWindowTitle("RPPOOP Project")
def D():
   s.run(['python', "C:\\Users\\Anuj\\Desktop\\Python Project\\python2.py"]) 
   
def A():
   s.run(['python', "C:\\Users\\Anuj\\Desktop\\Python Project\\python.py"])     
    
'''
while True:  
    print("\nMAIN MENU")  
    print("1. Dijkstra Algorithm")  
    print("2. A* Shortest Path Algorithm")  
    print("3. Exit")  
    choice = int(input("Enter the Choice:"))  
  
    if choice == 1:
        exec(python.py)  
        print("")      
    elif choice == 2:
        exec(python2.py)
        print("")     
    elif choice == 3:
        print("")

    else: 
        break       
    print("Oops! Incorrect Choice.")  
 ''' 
 

 
button0 = QtWidgets.QPushButton(window) 
button0.setText("Dijkstra Algorithm")
button0.setFont(QFont("New Times Roman",12))
button0.setGeometry(50,80,300,40)
button0.clicked.connect(D) 

button1 = QtWidgets.QPushButton(window) 
button1.setText("A* Shortest Path Algorithm")
button1.setFont(QFont("New Times Roman",12))
button1.setGeometry(50,30,300,40)
button1.clicked.connect(A)


  
window.show()
    
app.exec()    
