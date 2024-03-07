
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 714)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(450, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.widget.setStatusTip("")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_widget = QtWidgets.QWidget(self.widget)
        self.text_widget.setObjectName("text_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.text_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.text = QtWidgets.QTextEdit(self.text_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.text.setFont(font)
        self.text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.text_widget)
        self.btn_widget = QtWidgets.QWidget(self.widget)
        self.btn_widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btn_widget.setAccessibleName("")
        self.btn_widget.setObjectName("btn_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.btn_widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.save = QtWidgets.QPushButton(self.btn_widget)
        self.save.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.save.setFont(font)
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.save.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-radius:6px;\n"
"    border:7px;\n"
"\n"
"    \n"
"    \n"
"    background-color: rgb(149, 183, 255);\n"
"    \n"
"    border-color: rgb(0, 200, 255);\n"
"}")
        self.save.setObjectName("save")
        self.horizontalLayout_2.addWidget(self.save)
        self.ext = QtWidgets.QPushButton(self.btn_widget)
        self.ext.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ext.setFont(font)
        self.ext.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ext.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-radius:6px;\n"
"    border:7px;\n"
"\n"
"    \n"
"        \n"
"    background-color: rgb(255, 151, 119);\n"
"    border-color: rgb(0, 200, 255);\n"
"}")
        self.ext.setObjectName("ext")
        self.horizontalLayout_2.addWidget(self.ext)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.btn_widget)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "editor (beta) - Made in Russia"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.ext.setText(_translate("MainWindow", "Exit"))
