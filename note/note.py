# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/9/25 11:42'

from PyQt5.QtWidgets import *
# 常用快捷键
from PyQt5.QtGui import QKeySequence


# 记事本主界面
class MainWindow(QMainWindow):
    def closeEvent(self, e) -> None:
        if not text.document().isModified():
            return
        answer = QMessageBox.question(window, '关闭之前查看', "关闭之前是否保存文件？",
                                        QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard)
        if answer&QMessageBox.Save:
            save()
        elif answer&QMessageBox.Cancel:
            e.igore()


app = QApplication([])
app.setApplicationName("文本编辑器")
# 文本内容
text = QPlainTextEdit()
# 设置window界面
window = MainWindow()
window.setMinimumSize(800, 600)
window.setCentralWidget(text)

# 添加菜单项
menu = window.menuBar().addMenu("文件")

# 文件路径全局变量
file_path = None

# 1.打开文件
open_action = QAction("打开")


def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, "open")[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path


# 设置快捷方式
open_action.setShortcut(QKeySequence.Open)
# 设置槽，事件监听
open_action.triggered.connect(open_file)
menu.addAction(open_action)
# 2.保存
save_action = QAction("保存")


def save():
    if file_path is None:
        pass
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)


save_action.setShortcut(QKeySequence.Save)
save_action.triggered.connect(save)
menu.addAction(save_action)
# 3.另存为
save_as_action = QAction("另存为")


def save_as():
    global file_path
    path=QFileDialog.getSaveFileName(window, "另存为")[0]
    if path:
        file_path=path
        save()


save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)
# 菜单增加分割线
menu.addSeparator()
# 4.关闭退出
exit_action = QAction("关闭")
exit_action.setShortcut(QKeySequence.Close)
exit_action.triggered.connect(window.close)
menu.addAction(exit_action)

# 5.帮助
help_menu=window.menuBar().addMenu("帮助")
about_action=QAction("关于")


def show_about_dialog():
    about_text="<center>这是一个简易的文本编辑器</center>版本1.0<p></p>"
    QMessageBox.about(window,"说明",about_text)


about_action.triggered.connect(show_about_dialog)
help_menu.addAction(about_action)


# 窗体显示
window.show()
app.exec_()
