# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.tabWidget.setMaximumSize(QtCore.QSize(500, 500))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_eartitle = QtWidgets.QLabel(self.tab)
        self.label_eartitle.setGeometry(QtCore.QRect(150, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_eartitle.setFont(font)
        self.label_eartitle.setObjectName("label_eartitle")
        self.radioButton_alien = QtWidgets.QRadioButton(self.tab)
        self.radioButton_alien.setGeometry(QtCore.QRect(320, 90, 95, 20))
        self.radioButton_alien.setObjectName("radioButton_alien")
        self.label_output = QtWidgets.QLabel(self.tab)
        self.label_output.setGeometry(QtCore.QRect(30, 300, 431, 101))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_output.setFont(font)
        self.label_output.setText("")
        self.label_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output.setObjectName("label_output")
        self.lineEdit_amount = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_amount.setGeometry(QtCore.QRect(150, 150, 251, 31))
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.label_amount = QtWidgets.QLabel(self.tab)
        self.label_amount.setGeometry(QtCore.QRect(40, 150, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_amount.setFont(font)
        self.label_amount.setObjectName("label_amount")
        self.pushButton_submit = QtWidgets.QPushButton(self.tab)
        self.pushButton_submit.setGeometry(QtCore.QRect(80, 230, 131, 41))
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.pushButton_clear = QtWidgets.QPushButton(self.tab)
        self.pushButton_clear.setGeometry(QtCore.QRect(250, 230, 131, 41))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.radioButton_cat = QtWidgets.QRadioButton(self.tab)
        self.radioButton_cat.setGeometry(QtCore.QRect(180, 90, 95, 20))
        self.radioButton_cat.setChecked(True)
        self.radioButton_cat.setObjectName("radioButton_cat")
        self.label_species = QtWidgets.QLabel(self.tab)
        self.label_species.setGeometry(QtCore.QRect(30, 90, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_species.setFont(font)
        self.label_species.setObjectName("label_species")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_exptitle = QtWidgets.QLabel(self.tab_2)
        self.label_exptitle.setGeometry(QtCore.QRect(130, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_exptitle.setFont(font)
        self.label_exptitle.setObjectName("label_exptitle")
        self.label_base = QtWidgets.QLabel(self.tab_2)
        self.label_base.setGeometry(QtCore.QRect(40, 90, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_base.setFont(font)
        self.label_base.setObjectName("label_base")
        self.label_power = QtWidgets.QLabel(self.tab_2)
        self.label_power.setGeometry(QtCore.QRect(40, 160, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_power.setFont(font)
        self.label_power.setObjectName("label_power")
        self.lineEdit_base = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_base.setGeometry(QtCore.QRect(150, 90, 251, 31))
        self.lineEdit_base.setObjectName("lineEdit_base")
        self.lineEdit_power = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_power.setGeometry(QtCore.QRect(150, 150, 251, 31))
        self.lineEdit_power.setObjectName("lineEdit_power")
        self.pushButton_submit_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_submit_2.setGeometry(QtCore.QRect(80, 230, 131, 41))
        self.pushButton_submit_2.setObjectName("pushButton_submit_2")
        self.pushButton_clear_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_clear_2.setGeometry(QtCore.QRect(260, 230, 131, 41))
        self.pushButton_clear_2.setObjectName("pushButton_clear_2")
        self.label_output_2 = QtWidgets.QLabel(self.tab_2)
        self.label_output_2.setGeometry(QtCore.QRect(30, 300, 421, 101))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_output_2.setFont(font)
        self.label_output_2.setText("")
        self.label_output_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output_2.setObjectName("label_output_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label_eartitle.setText(_translate("MainWindow", "EAR CALCULATOR"))
        self.radioButton_alien.setText(_translate("MainWindow", "Alien"))
        self.label_amount.setText(_translate("MainWindow", "Amount:"))
        self.pushButton_submit.setText(_translate("MainWindow", "SUBMIT"))
        self.pushButton_clear.setText(_translate("MainWindow", "CLEAR"))
        self.radioButton_cat.setText(_translate("MainWindow", "Cat"))
        self.label_species.setText(_translate("MainWindow", "Species:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ear Calculator"))
        self.label_exptitle.setText(_translate("MainWindow", "EXPONENT CALCULATOR"))
        self.label_base.setText(_translate("MainWindow", "Base:"))
        self.label_power.setText(_translate("MainWindow", "Power:"))
        self.pushButton_submit_2.setText(_translate("MainWindow", "SUBMIT"))
        self.pushButton_clear_2.setText(_translate("MainWindow", "CLEAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Exponenent Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())