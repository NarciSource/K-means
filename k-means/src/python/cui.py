
from k_means import Kmeans
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QColor
from PyQt5.QtCore import QFileInfo

class CuiMain():
    def __init__(self,argv):
        self.argv = argv

    def run(self):
        self.core()

    def core(self):
        ##load image        
        image = self.image_Load()
        self.width = image.width()
        self.height = image.height()

        ##print information        
        print("width(",self.width,") x height(",self.height,") x cluster(",self.num_of_cluster(),") x steps(",self.num_of_steps(),") = "
                ,self.width*self.height*self.num_of_cluster()*self.num_of_steps())

        ##convert to pixel from image
        pixels = {}
        for x in range(self.width):
            for y in range(self.height):
                pixels[(x,y)]=QColor(image.pixel(x,y)).getRgb()

        ##k-means process
        kmeans = Kmeans(pixels,self.num_of_cluster(),self.num_of_steps(),self)
        kmeans.start()


    def core_intermediate(self, pixels, centroids):
        result_image = self.convert_image_from(pixels)
        self.image_Show(result_image, centroids)

    def core_result(self, pixels):
        result_image = self.convert_image_from(pixels)
        self.image_Save(result_image)
    


    ##member function
    def convert_image_from(self, pixels):
        ##new image
        result_image = QImage(self.width, self.height, QImage.Format_RGB32)     

        ##convert to image from pixel
        for x in range(self.width):
            for y in range(self.height):
                result_image.setPixel(x,y,QColor(pixels[(x,y)][0],pixels[(x,y)][1],pixels[(x,y)][2],pixels[(x,y)][3]).rgb())

        return result_image

    
    def image_Load(self):
        return QImage(self.filename())

    def image_Show(self, image, centroids):
        pass

    def image_Save(self, result_image):
        result_image.save(str(self.num_of_cluster()) +'-means' + '_' + QFileInfo(self.filename()).fileName())

    def filename(self):
        return str(self.argv[1])

    def num_of_cluster(self):
        return int(self.argv[2])

    def num_of_steps(self):
        return int(self.argv[3])
