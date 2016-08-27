from PyQt4.QtCore import *
from PyQt4.QtGui  import *


class ImageLoad(QWidget):
    def __init__(self, numImg):
        QWidget.__init__(self)

        image = QLabel()
        hi = QPushButton("Configurations")
        layout = QVBoxLayout()

        #Necessario alterar o path para que funcione...
        if(numImg == 0):
            pixmap = QPixmap('C:/Users/Prado/Desktop/FottoramaPY/resources/images/planet.jpg')
        elif(numImg == 1):
            pixmap = QPixmap('C:/Users/Prado/Desktop/FottoramaPY/resources/images/cat.png')
        elif(numImg == 2):
            pixmap = QPixmap('C:/Users/Prado/Desktop/FottoramaPY/resources/images/building.jpg')

        image.setAlignment(Qt.AlignCenter)
        image.setPixmap(pixmap)

        layout.addWidget(image)
        layout.addWidget(hi)

        self.resize(500,500)
        self.setFixedSize(500,500)
        self.setWindowTitle("Show, Image!")
        self.setLayout(layout)

        hi.clicked.connect(lambda: self.close())
        
        
class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        #layoutVertical = QGridLayout()
        imgLabel       = QLabel("Select Image:", self)
        comboBox       = QComboBox(self)

        imgLabel.move(50, 205)
        
        comboBox.addItems(["planet.jpg", "cat.png", "building.jpg"]);
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
        
        but.clicked.connect(lambda: self.sayHello(comboBox.currentIndex()))
        but.move(50,250)
        
        self.resize(500, 500)
        self.setFixedSize(500,500)
        self.setWindowTitle("Show, Image!")

    def sayHello(self, numero):
        format(numero)
        self.window = ImageLoad(numero)
        self.window.show()
                
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main = Main()
    main.show()
    sys.exit(app.exec_())
