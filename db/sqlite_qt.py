# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/10/9 13:12'

from os.path import exists
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sys

# 判断数据库文件是否存在
if not exists("student.db"):
    print("数据库文件不存在")
    sys.exit()

# qt界面以及数据绑定
app = QApplication([])
# 连接数据库--model
# 1.指定数据库类型
db = QSqlDatabase.addDatabase("QSQLITE")
# 2.指定哪个数据库并打开
db.setDatabaseName('student.db')
db.open()
# 3.创建model data--ui纽带,指定具体表的model
model = QSqlTableModel(None, db)
model.setTable('student')
# 3.1 设置修改策略，基于字段的修改
model.setEditStrategy(QSqlTableModel.OnFieldChange)
model.select()
# 3.2 设置表格头部
model.setHeaderData(0, Qt.Horizontal, '名字')
model.setHeaderData(1, Qt.Horizontal, '电话')
model.setHeaderData(2, Qt.Horizontal, '地址')
# 4.ui部分,让ui组件绑定model
view = QTableView()
view.setModel(model)

# 4.1 添加 & 删除按钮
dialog = QDialog()
dialog.setWindowTitle('sqlite操作')
# 垂直布局
layout = QVBoxLayout()
layout.addWidget(view)


def add_row():
    print(model.rowCount())
    num = model.insertRows(model.rowCount(), 1)
    print(num)


btn_add = QPushButton('添加')
btn_add.clicked.connect(add_row)
layout.addWidget(btn_add)
btn_delete = QPushButton('删除')
# 删除当前选中行
# lambda表达式本质是匿名函数
# 匿名函数，很少调用或者只有一次调用调用，完成简单函数功能的函数定义
btn_delete.clicked.connect(lambda:model.removeRow(view.currentIndex().row()))
layout.addWidget(btn_delete)
dialog.setLayout(layout)
# 5.显示数据
dialog.show()
app.exec_()
