from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow2 import Ui_MainWindow
from particula import Particula
from admin import Administrador

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.administra = Administrador()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.AgFinal_pushButton.clicked.connect(self.click_capturar)
        self.ui.AgInicio_pushButton.clicked.connect(self.click_capturar_Inicio)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)
        

    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.administra))

    @Slot()
    def click_capturar(self):
        Ide = self.ui.ID_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.ColorRed_spinBox.value()
        Green = self.ui.ColorGreen_spinBox.value()
        Blue = self.ui.ColorBlue_spinBox.value()
        particula = Particula(Ide, OrigenX, OrigenY, DestinoX, DestinoY, Velocidad, Red, Green, Blue)
        self.administra.agregar_final(particula)

    @Slot()
    def click_capturar_Inicio(self):
        Ide = self.ui.ID_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.ColorRed_spinBox.value()
        Green = self.ui.ColorGreen_spinBox.value()
        Blue = self.ui.ColorBlue_spinBox.value()
        particula = Particula(Ide, OrigenX, OrigenY, DestinoX, DestinoY, Velocidad, Red, Green, Blue)
        self.administra.agregar_inicio(particula)