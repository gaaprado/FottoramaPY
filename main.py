from PyQt4.QtCore import *
from PyQt4.QtGui  import *


class Main(QWidget):
    def __init__(self, nameImg):
        QWidget.__init__(self)

        image = QLabel()
        butConfig = QPushButton("Configurations")
        layout = QVBoxLayout()   

        if nameImg == "":
            path = os.path.realpath("")+"/resources/images/planet.jpg"
            pixmap = QPixmap(path)
            image.setPixmap(pixmap)
            
        elif nameImg != "":
            
            try:
                con    = lite.connect('fottorama.db')
                cur    = con.execute("SELECT diretorio FROM images WHERE nome LIKE '{name}'".\
                                     format(name = nameImg))
                data   = cur.fetchone()
                path   = os.path.realpath("")
                pixmap = QPixmap(path+data[0])
                
                image.setPixmap(pixmap)
                con.close()
                
            except ValueError:
                print("Error sql")

        butConfig.clicked.connect(lambda: self.selectImage())        

        image.setAlignment(Qt.AlignCenter)    
                    
        layout.addWidget(image)
        layout.addWidget(butConfig)

        self.resize(500,500)
        self.setFixedSize(500,500)
        self.setWindowTitle("Show, Image!")
        self.setLayout(layout)

    def selectImage(self):
        self.close()
        self.window = ImageSelect()
        self.window.show()
            
class ImageSelect(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        imgLabel       = QLabel("Select Image:", self)
        comboBox       = QComboBox(self)
        
        imgLabel.move(50, 205)

        try:

            connection = lite.connect('fottorama.db')
            cur        = connection.execute('SELECT nome, diretorio FROM images')
            rows       = cur.fetchall()
            
            comboBox.addItems([rows[0][0], rows[1][0], rows[2][0]])

        except ValueError:
            print("Error: SQL")

        comboBox.setMinimumWidth(200)
        comboBox.setMinimumHeight(25)
        comboBox.setMaximumWidth(200)
        comboBox.setMaximumHeight(25)
        comboBox.move(150, 200)

        but = QPushButton("Save", self)
        but.setMinimumWidth(400)
        but.setMinimumHeight(20)
        but.setMaximumWidth(400)
        but.setMaximumHeight(20)
        
        but.clicked.connect(lambda: self.sayHello(comboBox.currentText()))
        but.move(50,250)
        
        self.resize(500, 500)
        self.setFixedSize(500,500)
        self.setWindowTitle("Show, Image!")

    def sayHello(self, nome):
        format(nome)
        self.window = Main(nome)
        self.window.show()
        self.close()
                
if __name__ == "__main__":
    import sys
    import sqlite3 as lite
    import os

    app = QApplication(sys.argv)
    
    main = Main("")
    main.show()
    sys.exit(app.exec_())
