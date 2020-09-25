# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/9/20 17:04'
import sys

from PyQt5.QtWidgets import *
from login import Ui_LoginDialog

if __name__ == '__main__':

    app=QApplication(sys.argv)
    main=QDialog()
    login_dialog=Ui_LoginDialog()
    login_dialog.setupUi(main)
    main.show()
    sys.exit(app.exec_())

