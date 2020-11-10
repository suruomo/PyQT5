# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/11/9 18:10'


import vtk


class MyInteractor(vtk.vtkInteractorStyleTrackballCamera):  # 交互拾取器

    def __init__(self, mainApp):
        self.AddObserver("RightButtonPressEvent", self.RightButtonPressEvent)
        self.mainApp=mainApp
        self.actor = vtk.vtkActor()

    # 右键拾取点
    def RightButtonPressEvent(self, obj, event):
        # MainApp对象
        clickPos = self.mainApp.render_window.GetInteractor().GetEventPosition()
        self.mainApp.OutputBrowser.append("Picking pixel: "+str(clickPos))

        # 选择当前像素
        picker = self.mainApp.render_window.GetInteractor().GetPicker()
        picker.Pick(clickPos[0], clickPos[1], 0, self.mainApp.renderer)

        # If CellId = -1, nothing was picked
        if (picker.GetCellId() != -1):
            self.mainApp.OutputBrowser.append("Pick position is: "+str(picker.GetPickPosition()))
            self.mainApp.OutputBrowser.append("Cell id is:"+str(picker.GetCellId()))
            self.mainApp.OutputBrowser.append("Point id is:"+str(picker.GetPointId()))
            point_position = self.mainApp.original_model.GetOutput().GetPoint(picker.GetPointId())
            # 如果上一次选点，则取消上一次选点标记
            if self.actor:
                self.mainApp.renderer.RemoveActor(self.actor)

            # Create a sphere
            sphereSource = vtk.vtkSphereSource()
            sphereSource.SetCenter(point_position)
            sphereSource.SetRadius(0.2)

            # Create a mapper and actor
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(sphereSource.GetOutputPort())

            self.actor.SetMapper(mapper)
            self.actor.GetProperty().SetColor(1.0, 0.0, 0.0)
            self.mainApp.renderer.AddActor(self.actor)


        # Forward events
        self.OnRightButtonDown()
        return
