import sys
from gui import XMainWindow
from cui import CuiMain
from PyQt5.QtWidgets import QApplication


# main
if len(sys.argv) is 1:
    #gui
    app = QApplication(sys.argv)
    dlg = XMainWindow()
    dlg.show()
    app.exec_()
else :
    #cui
    app = CuiMain(sys.argv)
    app.run()

