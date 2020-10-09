# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/10/9 15:12'

# 显示当前用户磁盘路径树形图
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel
# 获取路径信息
home_dir=expanduser("~")

# 0.构建QT程序
app=QApplication([])

'''
TreeView
'''
# 1.创建树形view
# view=QTreeView()
# 2.创建model，默认为全磁盘目录结构
# 不同的数据需要不同的model，不同的view需要不同的model
# model=QDirModel()
# 3.model连接data
# 4.连接model和view
# view.setModel(model)
# 设置根目录
# view.setRootIndex(model.index(home_dir))
# 5.显示界面
# view.show()

'''
ListView
'''
# view=QListView()
# model=QStringListModel(['zhangsan','lisi','bob'])
# view.setModel(model)
# view.show()



app.exec_()




