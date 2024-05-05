from PySide6.QtCore import Signal, QObject


class MyObject(QObject):
    t1 = Signal()

o = MyObject()
