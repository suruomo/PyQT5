# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/10/29 13:57'

import vtk
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

# 引入ui资源

main_ui, _ = loadUiType('main.ui')


# 主操作界面
class MainApp(QMainWindow, main_ui):

    # 定义构造方法
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.init_vtk_view()
        self.handle_events()

    # 绑定事件
    def handle_events(self):
        self.import_geometry_action.triggered.connect(self.show_geometry)

    # 初始化vtk视图区域
    def init_vtk_view(self):
        # 在之前创建的view_widget上添加vtk控件
        self.vtk_vertical_layout = QVBoxLayout(self.view_widget)
        self.vtk_widget = QVTKRenderWindowInteractor(self.view_widget)
        self.vtk_vertical_layout.addWidget(self.vtk_widget)
        # 1.创建RenderWindow窗口
        self.render_window = self.vtk_widget.GetRenderWindow()
        # 2.创建render
        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(1.0, 1.0, 1.0)  # 设置页面底部颜色值
        self.renderer.SetBackground2(0.1, 0.2, 0.4)  # 设置页面顶部颜色值
        self.renderer.SetGradientBackground(1)  # 开启渐变色背景设置
        self.render_window.AddRenderer(self.renderer)
        self.render_window.Render()
        # 3.设置交互方式
        self.iren = self.render_window.GetInteractor()  # 获取交互器
        style = vtk.vtkInteractorStyleTrackballCamera()  # 交互器样式的一种，该样式下，用户是通过控制相机对物体作旋转、放大、缩小等操作
        self.iren.SetInteractorStyle(style)
        # 4.添加坐标轴(加self,血的教训）
        axesActor = vtk.vtkAxesActor()
        self.axes_widget = vtk.vtkOrientationMarkerWidget()
        self.axes_widget.SetOrientationMarker(axesActor)
        self.axes_widget.SetInteractor(self.iren)
        self.axes_widget.EnabledOn()
        self.axes_widget.InteractiveOff() # 坐标系是否可移动
        # 5.添加Actor
        self.original_actor = vtk.vtkActor()

    def show_geometry(self):
        # 使用QSettings记录上次打开路径
        qSettings=QSettings()
        lastPath=qSettings.value("LastFilePath")
        # 文件选择器
        filename, _ = QFileDialog.getOpenFileName(
            self, '打开文件 - stl文件', lastPath, '(*.stl)')
        # 如果刚才已经打开过模型，则删除上一个
        if self.original_actor:
             self.renderer.RemoveActor(self.original_actor)
        if filename:
            # 1.数据源：读取stl文件
            self.original_model = vtk.vtkSTLReader()
            self.original_model.SetFileName(filename)
            self.original_model.Update()
            # 2.创建mapper，建图
            self.original_mapper = vtk.vtkPolyDataMapper()
            self.original_mapper.SetInputConnection(self.original_model.GetOutputPort())
            # 3.设置执行单元：演员
            self.original_actor.SetMapper(self.original_mapper)
            self.original_actor.GetProperty().SetColor(0.5, 0.5, 0.5)
            # 4.渲染renderer
            self.renderer.AddActor(self.original_actor)
            self.renderer.ResetCamera()
            # 交互器初始化，否则需要点一下才能显示模型
            self.iren.Initialize()
            self.statusBar().showMessage('成功导入模型！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
