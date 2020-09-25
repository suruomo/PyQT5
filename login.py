# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(413, 283)
        LoginDialog.setMinimumSize(QtCore.QSize(413, 283))
        LoginDialog.setMaximumSize(QtCore.QSize(413, 283))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/图片/电脑壁纸/2d266df8b74822cd239c2a634b688025.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginDialog.setWindowIcon(icon)
        LoginDialog.setStyleSheet("background-color: rgb(0, 172, 126);")
        self.label = QtWidgets.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(100, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.userEdit = QtWidgets.QLineEdit(LoginDialog)
        self.userEdit.setGeometry(QtCore.QRect(180, 70, 113, 21))
        self.userEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userEdit.setObjectName("userEdit")
        self.pwdEdit = QtWidgets.QLineEdit(LoginDialog)
        self.pwdEdit.setGeometry(QtCore.QRect(180, 120, 113, 21))
        self.pwdEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pwdEdit.setObjectName("pwdEdit")
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.loginButton = QtWidgets.QPushButton(LoginDialog)
        self.loginButton.setGeometry(QtCore.QRect(110, 170, 61, 31))
        self.loginButton.setStyleSheet("color: rgb(85, 170, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.loginButton.setObjectName("loginButton")
        self.registButton = QtWidgets.QPushButton(LoginDialog)
        self.registButton.setGeometry(QtCore.QRect(220, 170, 61, 31))
        self.registButton.setStyleSheet("color: rgb(85, 170, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.registButton.setObjectName("registButton")

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "登录"))
        self.label.setText(_translate("LoginDialog", "用户名："))
        self.label_2.setText(_translate("LoginDialog", "密码:"))
        self.loginButton.setText(_translate("LoginDialog", "登录"))
        self.registButton.setText(_translate("LoginDialog", "注册"))
