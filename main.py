import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets

from main_auto import *
import add

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.view.loadFinished.connect(self.onLoadFinished)
        self.pushButton.clicked.connect(self.add)
    
    def add(self):
        dialog = add.Add()
        dialog.show()
        dialog.exec_()

    def onLoadFinished(self):
        with open('map.js', 'r') as f:
            frame = self.view.page().mainFrame()
            frame.evaluateJavaScript(f.read())

    @QtCore.pyqtSlot(float, float)
    def onMapMove(self, lat, lng):
        self.label.setText('Lng: {:.5f}, Lat: {:.5f}'.format(lng, lat))

    def panMap(self, lng, lat):
        frame = self.view.page().mainFrame()
        frame.evaluateJavaScript(
            'map.panTo(L.latLng({}, {}));'.format(lat, lng))

app = QtWidgets.QApplication(sys.argv)
myWindow = Main(None)
myWindow.show()
app.exec_()