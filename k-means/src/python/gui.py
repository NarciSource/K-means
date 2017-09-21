import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from layout import Ui_MainWindow
from k_means import Kmeans
from cui import CuiMain

class XMainWindow(QMainWindow, Ui_MainWindow, CuiMain):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pixmap = QPixmap()
        self.file_name = str()
        self.option1_km_pp = True
        self.commandLinkButton.clicked.connect(self.commandLinkButton_Event)
        self.openDirectoryButton.clicked.connect(self.openDirectoryButton_Event)
        self.actionOpen.triggered.connect(self.actionOpen_Event)
        self.actionAbout.triggered.connect(self.actionAbout_Event)
        self.actionExit.triggered.connect(self.close)
        self.actionGoto_gitHub.triggered.connect(lambda: webbrowser.open("https://github.com/NarciSource/K-means"))
        self.dial.valueChanged.connect(self.label_4.setNum)
        self.actionOption1.triggered.connect(self.actionOption1_Event)


    ##Event
    def commandLinkButton_Event(self):
        if self.pixmap.isNull():
            msgbox = QMessageBox(self)
            msgbox.information(self,"Warning","No image")
        else:
            self.complete = 0

            #make topcolor box
            for i in range(self.num_of_cluster()):
                item = QListWidgetItem()
                item.setSizeHint(QSize(40,40))
                self.listWidget.addItem(item)

            self.core()

    def openDirectoryButton_Event(self):
        QDesktopServices.openUrl(QUrl(QFileInfo(self.filename()).path(),QUrl.TolerantMode))

    def actionOpen_Event(self):
        self.file_name = QFileDialog.getOpenFileName(self,'Open file','','Images (*.png *.jpg)')[0]
        self.image_Into(self.filename())

    def actionAbout_Event(self):
        msgbox = QMessageBox(self)
        msgbox.information(self,"About","Chung Ang Univ\nName : Jeong Won Cheol\nStudent Code : 20113560")

    def actionOption1_Event(self):
        self.option1_km_pp = not self.option1_km_pp


    def core_result(self, pixels):
        result_image = self.convert_image_from(pixels)
        self.image_Save(result_image)
    
        self.complete =0
        while self.complete < 100:
            self.complete += 0.0001
            self.progressBar.setValue(self.complete)

    ##member function
    def image_Into(self,file_name):
        self.pixmap.load(file_name)
        self.beforeImage.setPixmap(self.pixmap)
        self.beforeImage.setScaledContents(True)


    def image_Load(self):
        return self.pixmap.toImage()

    def image_Show(self, image, centroids):
        for i in range(self.num_of_cluster()):
            item = self.listWidget.item(i)
            item.setBackground(QColor(centroids[i][0],centroids[i][1],centroids[i][2]))
       
        ##draw image
        self.afterImage.setScaledContents(True)
        self.afterImage.setPixmap(QPixmap.fromImage(image))



    def filename(self):
        return self.file_name

    def num_of_cluster(self):
        return self.dial.value()

    def num_of_steps(self):
        if self.verticalSlider.value() == 100:
            return self.verticalSlider.value()
        else :
            return self.verticalSlider.value()/10