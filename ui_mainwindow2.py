from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(516, 502)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.DestinoX_spinBox = QSpinBox(self.groupBox)
        self.DestinoX_spinBox.setObjectName(u"DestinoX_spinBox")
        self.DestinoX_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.DestinoX_spinBox, 3, 2, 1, 1)

        self.ID_spinBox = QSpinBox(self.groupBox)
        self.ID_spinBox.setObjectName(u"ID_spinBox")
        self.ID_spinBox.setMaximum(99)

        self.gridLayout_2.addWidget(self.ID_spinBox, 0, 2, 1, 1)

        self.DestinoY_spinBox = QSpinBox(self.groupBox)
        self.DestinoY_spinBox.setObjectName(u"DestinoY_spinBox")
        self.DestinoY_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.DestinoY_spinBox, 4, 2, 1, 1)

        self.AgInicio_pushButton = QPushButton(self.groupBox)
        self.AgInicio_pushButton.setObjectName(u"AgInicio_pushButton")

        self.gridLayout_2.addWidget(self.AgInicio_pushButton, 7, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 2)

        self.AgFinal_pushButton = QPushButton(self.groupBox)
        self.AgFinal_pushButton.setObjectName(u"AgFinal_pushButton")

        self.gridLayout_2.addWidget(self.AgFinal_pushButton, 7, 1, 1, 1)

        self.OrigenX_label = QLabel(self.groupBox)
        self.OrigenX_label.setObjectName(u"OrigenX_label")

        self.gridLayout_2.addWidget(self.OrigenX_label, 1, 0, 1, 2)

        self.OrigenY_label = QLabel(self.groupBox)
        self.OrigenY_label.setObjectName(u"OrigenY_label")

        self.gridLayout_2.addWidget(self.OrigenY_label, 2, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 2)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")

        self.gridLayout_2.addWidget(self.Velocidad_spinBox, 5, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.ColorRed_spinBox = QSpinBox(self.groupBox_2)
        self.ColorRed_spinBox.setObjectName(u"ColorRed_spinBox")
        self.ColorRed_spinBox.setMaximum(255)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ColorRed_spinBox)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.ColorGreen_spinBox = QSpinBox(self.groupBox_2)
        self.ColorGreen_spinBox.setObjectName(u"ColorGreen_spinBox")
        self.ColorGreen_spinBox.setMaximum(255)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ColorGreen_spinBox)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.ColorBlue_spinBox = QSpinBox(self.groupBox_2)
        self.ColorBlue_spinBox.setObjectName(u"ColorBlue_spinBox")
        self.ColorBlue_spinBox.setMaximum(255)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ColorBlue_spinBox)


        self.gridLayout_2.addWidget(self.groupBox_2, 6, 0, 1, 2)

        self.OrigenY_spinBox = QSpinBox(self.groupBox)
        self.OrigenY_spinBox.setObjectName(u"OrigenY_spinBox")
        self.OrigenY_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.OrigenY_spinBox, 2, 2, 1, 1)

        self.OrigenX_spinBox = QSpinBox(self.groupBox)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")
        self.OrigenX_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.OrigenX_spinBox, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 2)

        self.ID_label = QLabel(self.groupBox)
        self.ID_label.setObjectName(u"ID_label")

        self.gridLayout_2.addWidget(self.ID_label, 0, 0, 1, 1)

        self.Mostrar_pushButton = QPushButton(self.groupBox)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.gridLayout_2.addWidget(self.Mostrar_pushButton, 7, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 516, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.AgInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.AgFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.OrigenX_label.setText(QCoreApplication.translate("MainWindow", u"Origen en X: ", None))
        self.OrigenY_label.setText(QCoreApplication.translate("MainWindow", u"Origen en Y: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Color (RGB)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.ID_label.setText(QCoreApplication.translate("MainWindow", u"ID: ", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
    # retranslateUi


