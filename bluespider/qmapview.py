
from PyQt4 import Qt, QtCore, QtGui

class QMapPixmap(QtGui.QGraphicsObject):
    clicked = QtCore.pyqtSignal(QtGui.QGraphicsSceneMouseEvent)

    def __init__(self, pixmap):
        super(QMapPixmap, self).__init__()
        self.pixmap = pixmap

    def boundingRect(self):
        return QtCore.QRectF(self.pixmap.rect())

    def mousePressEvent(self, event):
        self.clicked.emit(event)

    def paint(self, painter, option, widget):
        painter.drawPixmap(QtCore.QPoint(0, 0), self.pixmap)



