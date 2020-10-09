# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/10/9 16:05'

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# 自定义数据
headers = ['国家', '感染病例', '死亡病例']
rows = [('美国', 1034588, 58955),
        ('西班牙', 232128, 23822),
        ('意大利', 201505, 27359)]


# 自定义TableModel,继承自QAbstractTableModel
class TableModel(QAbstractTableModel):

    # 二维数据，行数，列数
    def rowCount(self, parent) -> int:
        return len(rows)

    def columnCount(self, parent) -> int:
        return len(headers)

    # 数据
    def data(self,index:QModelIndex,role:int=...):
        if role!=Qt.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]

    # 表头
    def headerData(self,section:int,orientation:Qt.Orientation,role:int=...):
        if role!=Qt.DisplayRole or orientation!=Qt.Horizontal:
            return QVariant()
        return headers[section]


# 测试程序

app=QApplication([])
model=TableModel()
view=QTableView()
view.setModel(model)
view.show()
app.exec_()