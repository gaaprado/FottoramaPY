from PyQt4.QtCore import *
from PyQt4.QtGui  import *
import json

class Main(QWidget):
    def __init__(self, nome, json):
        QWidget.__init__(self)

        image     = QLabel()
        butConfig = QPushButton("Configurations")
        layout    = QVBoxLayout()

        image.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(image)
        layout.addWidget(butConfig)

        for index in range(len(json)):
            if nome == json[index]['nome']:
                pixmap = QPixmap(json[index]['diretorio'])
                image.setPixmap(pixmap)
                
        # Comandos que modelam o qwidget
        self.resize(500,500)
        self.setFixedSize(500,500)
        self.setWindowTitle("Show, Image!")
        self.setLayout(layout)
        
        butConfig.clicked.connect(lambda: self.selectImage())
        
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

        #Hardcode com tupla's e json's.
        tp1  = ('planet.jpg',
                  os.path.realpath("")
                  +'\\resources\\images\\planet.jpg')
        tp2 = ('cat.png',
                  os.path.realpath("")
                  +'\\resources\\images\\cat.png')
        tp3 = ('building.jpg',
                  os.path.realpath("")
                  +'\\resources\\images\\building.jpg')
        first =  {
               'nome': ''+tp1[0], 
               'diretorio': ''+tp1[1]
            }
        second =  {
               'nome': ''+tp2[0], 
               'diretorio': ''+tp2[1]
            }
        third =  {
               'nome': ''+tp3[0], 
               'diretorio': ''+tp3[1]
            }

        array = [first, second, third]
        
        #Botão dropdown
        comboBox.addItems([first['nome'], second['nome'], third['nome']])
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

        but.clicked.connect(lambda: self.selectImage(comboBox.currentText(), array))
        
        but.move(50,250)
        
        self.resize(500, 500)
        self.setFixedSize(500,500)
        self.setWindowTitle("Show, Image!")

    def selectImage(self, nome, JsonArray):
        self.window = Main(nome, JsonArray)
        self.window.show()
        self.close()


if __name__ == "__main__":
    import sys
    import os
    app = QApplication(sys.argv)

    main = Main("", "")
    main.show()
    sys.exit(app.exec_())
