# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 60, 16))
        self.label_2.setObjectName("label_2")
        self.ID_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ID_Edit.setGeometry(QtCore.QRect(40, 50, 113, 21))
        self.ID_Edit.setObjectName("ID_Edit")
        self.pserach_ushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pserach_ushButton.setGeometry(QtCore.QRect(160, 40, 113, 32))
        self.pserach_ushButton.setObjectName("pserach_ushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 251, 16))
        self.label_3.setObjectName("label_3")
        self.Sort_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Sort_Edit.setGeometry(QtCore.QRect(60, 100, 131, 21))
        self.Sort_Edit.setObjectName("Sort_Edit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 60, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 131, 16))
        self.label_6.setObjectName("label_6")
        self.roast_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.roast_spinBox.setGeometry(QtCore.QRect(150, 130, 48, 24))
        self.roast_spinBox.setObjectName("roast_spinBox")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 160, 87, 20))
        self.checkBox.setObjectName("checkBox")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 81, 16))
        self.label_7.setObjectName("label_7")
        self.description_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description_plainTextEdit.setGeometry(QtCore.QRect(20, 210, 211, 79))
        self.description_plainTextEdit.setObjectName("description_plainTextEdit")
        self.price_pinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.price_pinBox.setGeometry(QtCore.QRect(60, 300, 48, 24))
        self.price_pinBox.setObjectName("price_pinBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 300, 51, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 300, 51, 16))
        self.label_9.setObjectName("label_9")
        self.val = QtWidgets.QSpinBox(self.centralwidget)
        self.val.setGeometry(QtCore.QRect(160, 300, 48, 24))
        self.val.setObjectName("val")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 290, 113, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Капучино"))
        self.label.setText(_translate("MainWindow", "Добавить новый сорт или изменить существующий"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.pserach_ushButton.setText(_translate("MainWindow", "Найти"))
        self.label_3.setText(_translate("MainWindow", "Оставьте пустым для создания нового"))
        self.label_4.setText(_translate("MainWindow", "Сорт"))
        self.label_5.setText(_translate("MainWindow", "Сорт"))
        self.label_6.setText(_translate("MainWindow", "Уровень обжарки"))
        self.checkBox.setText(_translate("MainWindow", "В зернах"))
        self.label_7.setText(_translate("MainWindow", "Описание"))
        self.label_8.setText(_translate("MainWindow", "Цена"))
        self.label_9.setText(_translate("MainWindow", "Вес"))
        self.pushButton.setText(_translate("MainWindow", "Готово"))
