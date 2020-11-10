# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/10/29 13:57'

import vtk
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from finite.pick import MyInteractor

main_ui, _ = loadUiType('main.ui')  # 引入ui资源


class MainApp(QMainWindow, main_ui):  # 主操作界面

    # 定义构造方法
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pick_actor = vtk.vtkActor()
        self.init_vtk_view()
        self.handle_events()

    # 绑定事件
    def handle_events(self):
        self.import_geometry_action.triggered.connect(self.show_geometry)
        self.point_pick.triggered.connect(self.pick_point)

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
        self.style = vtk.vtkInteractorStyleTrackballCamera()  # 交互器样式的一种，该样式下，用户是通过控制相机对物体作旋转、放大、缩小等操作
        # self.style = MyInteractor(self)
        self.style.SetDefaultRenderer(self.renderer)
        self.iren.SetInteractorStyle(self.style)
        # 拾取器
        cellPicker = vtk.vtkCellPicker()
        self.iren.SetPicker(cellPicker)
        # 4.添加坐标轴(加self,血的教训）
        axesActor = vtk.vtkAxesActor()
        self.axes_widget = vtk.vtkOrientationMarkerWidget()
        self.axes_widget.SetOrientationMarker(axesActor)
        self.axes_widget.SetInteractor(self.iren)
        self.axes_widget.EnabledOn()
        self.axes_widget.InteractiveOff()  # 坐标系是否可移动
        # 5.添加Actor
        self.original_actor = vtk.vtkActor()

    # 加载几何模型
    def show_geometry(self):
        # 使用QSettings记录上次打开路径
        qSettings = QSettings()
        lastPath = qSettings.value("LastFilePath")
        # 文件选择器
        filename, _ = QFileDialog.getOpenFileName(
            self, '打开文件 - vtk文件', lastPath, '(*.vtk)')
        # 如果刚才已经打开过模型，则删除上一个
        if self.original_actor:
            self.renderer.RemoveActor(self.original_actor)
            # 如果上一次选点，则取消上一次选点标记
            if self.pick_actor:
                self.renderer.RemoveActor(self.pick_actor)

        if filename:
            # 1.数据源：读取stl文件
            self.original_model = vtk.vtkPolyDataReader()
            self.original_model.SetFileName(filename)
            self.original_model.Update()
            self.output_point()
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
            self.iren.Start()
            self.OutputBrowser.append('成功导入模型！')

    def output_point(self):
        polydata = self.original_model.GetOutput()
        string = "Number of Cells:" + str(polydata.GetNumberOfCells())
        self.OutputBrowser.append(string)
        string = "Number of Points:" + str(polydata.GetNumberOfPoints())
        self.OutputBrowser.append(string)

    def pick_point(self):
        self.style.AddObserver("RightButtonPressEvent", self.RightButtonPressEvent)

    # 右键拾取点
    def RightButtonPressEvent(self, obj, event):
        # 选择当前像素
        clickPos = self.render_window.GetInteractor().GetEventPosition()
        self.OutputBrowser.append("Picking pixel: " + str(clickPos))

        picker = self.render_window.GetInteractor().GetPicker()
        picker.Pick(clickPos[0], clickPos[1], 0, self.renderer)

        # 选取到模型上一点
        if (picker.GetCellId() != -1):
            self.OutputBrowser.append("Pick position is: " + str(picker.GetPickPosition()))
            self.OutputBrowser.append("Cell id is:" + str(picker.GetCellId()))
            self.OutputBrowser.append("Point id is:" + str(picker.GetPointId()))
            point_position = self.original_model.GetOutput().GetPoint(picker.GetPointId())
            # 如果上一次选点，则取消上一次选点标记
            if self.pick_actor:
                self.renderer.RemoveActor(self.pick_actor)

            # 创建点标识
            sphereSource = vtk.vtkSphereSource()
            sphereSource.SetCenter(point_position)
            sphereSource.SetRadius(0.2)
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(sphereSource.GetOutputPort())
            self.pick_actor.SetMapper(mapper)
            self.pick_actor.GetProperty().SetColor(1.0, 0.0, 0.0)
            self.renderer.AddActor(self.pick_actor)

        # Forward events
        self.style.OnRightButtonDown()
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
