# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/10/20 11:22'

import sys

from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType

# UI--Logic分离
# 下划线表示接受的第二个参数不用
from book.dbutil import get_conn, close_conn

ui, _ = loadUiType("book.ui")


class MainApp(QMainWindow, ui):

    # 定义构造方法
    def __init__(self):
        QMainWindow.__init__(self)
        # 设置Ui
        self.setupUi(self)
        # 隐藏主题设置
        self.handle_ui_change()
        # button与槽的通信
        self.handle_buttons()
        self.show_category()
        self.show_author()
        self.show_publisher()
        self.show_category_combobox()
        self.show_author_combobox()
        self.show_publisher_combobox()
        self.show_books()
        # self.show_client()
        # self.show_all_operations()

    # UI变化处理
    def handle_ui_change(self):
        # 最开始隐藏主题
        self.hide_themes()
        # 隐藏最上层tabWidght
        self.tabWidget.tabBar().setVisible(False)

    # 所有Button的消息与槽的通信
    def handle_buttons(self):
        self.themeButton.clicked.connect(self.show_themes)
        self.theme_change_Button.clicked.connect(self.hide_themes)
        self.bookButton.clicked.connect(self.open_book_tab)
        self.settingButton.clicked.connect(self.open_setting_tab)
        self.userButton.clicked.connect(self.open_user_tab)
        self.add_category_Button.clicked.connect(self.add_category)
        self.add_author_Button.clicked.connect(self.add_author)
        self.add_publisher_Button.clicked.connect(self.add_publisher)
        # self.add_book_save_Button.clicked.connect(self.add_book)
        # self.editor_book_search_Button.clicked.connect(self.search_book)
        # self.editor_book_save_Button.clicked.connect(self.editor_book)
        # self.editor_book_delete_Button.clicked.connect(self.delete_book)
        self.dark_orange_button.clicked.connect(self.dark_orange_theme)
        self.dark_blue_button.clicked.connect(self.dark_blue_theme)
        self.dark_gray_button.clicked.connect(self.dark_gray_theme)
        self.qdark_button.clicked.connect(self.qdark_theme)
        # self.add_user_button.clicked.connect(self.add_user)
        # self.login_button.clicked.connect(self.user_login)
        # self.editor_user_button.clicked.connect(self.editor_user)
        # self.clientButton.clicked.connect(self.open_client_tab)
        # self.add_client_button.clicked.connect(self.add_client)
        # self.search_client_button.clicked.connect(self.select_client)
        # self.update_client_button.clicked.connect(self.editor_client)
        # self.delete_client_button.clicked.connect(self.delete_client)
        # self.add_operation.clicked.connect(self.handel_day_operation)
        # self.dayButton.clicked.connect(self.open_day_operation_tab)
        # self.export_button.clicked.connect(self.export_day_operations)

    # 主题的显示
    def show_themes(self):
        self.theme_groupBox.show()

    # 主题的隐藏
    def hide_themes(self):
        self.theme_groupBox.hide()

    # 选项卡联动，按照tab的索引切换
    def open_book_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def open_setting_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def open_user_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def open_client_tab(self):
        self.tabWidget.setCurrentIndex(3)

    def open_day_operation_tab(self):
        self.tabWidget.setCurrentIndex(4)

    # 1、添加类别
    def add_category(self):
        #  数据库操作流程
        # 1、获取连接
        conn = get_conn()
        # 2、获取cursor
        cur = conn.cursor()
        # 3、SQl语句
        sql = "insert into category(category_name) values(%s)"
        category_name = self.add_category_name.text()
        # 4、执行语句
        cur.execute(sql, (category_name,))
        # 5、insert、update、delete必须显示提交
        conn.commit()
        # 6、关闭资源
        close_conn(conn, cur)
        # 7、消息提示
        self.statusBar().showMessage('类别添加成功！')
        self.add_category_name.setText('')
        self.show_category()

    # 显示已有类别，并且添加完毕后直接可以看到
    def show_category(self):
        conn = get_conn()
        cur = conn.cursor()
        sql = "select category_name from category"
        cur.execute(sql)
        data = cur.fetchall()

        if data:
            # 一开始没有数据时
            self.category_table.setRowCount(0)
            self.category_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.category_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.category_table.rowCount()
                self.category_table.insertRow(row_position)

    # 添加作者
    def add_author(self):
        #  数据库操作流程
        # 1、获取连接
        conn = get_conn()
        # 2、获取cursor
        cur = conn.cursor()
        # 3、SQl语句
        sql = "insert into author(author_name) values(%s)"
        author_name = self.add_author_name.text()
        # 4、执行语句
        cur.execute(sql, (author_name,))
        # 5、insert、update、delete必须显示提交
        conn.commit()
        # 6、关闭资源
        close_conn(conn, cur)
        # 7、消息提示
        self.statusBar().showMessage('作者添加成功！')
        self.add_author_name.setText('')
        self.show_author()

    # 显示所有作者
    def show_author(self):
        conn = get_conn()
        cur = conn.cursor()
        sql = "select author_name from author"
        cur.execute(sql)
        data = cur.fetchall()

        if data:
            self.author_table.setRowCount(0)
            self.author_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.author_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.author_table.rowCount()
                self.author_table.insertRow(row_position)

    # 添加出版社
    def add_publisher(self):
        #  数据库操作流程
        # 1、获取连接
        conn = get_conn()
        # 2、获取cursor
        cur = conn.cursor()
        # 3、SQl语句
        sql = "insert into publisher(publisher_name) values(%s)"
        publisher_name = self.add_publisher_name.text()
        # 4、执行语句
        cur.execute(sql, (publisher_name,))
        # 5、insert、update、delete必须显示提交
        conn.commit()
        # 6、关闭资源
        close_conn(conn, cur)
        # 7、消息提示
        self.statusBar().showMessage('作者添加成功！')
        self.add_publisher_name.setText('')
        self.show_publisher()

    # 显示出版社信息
    def show_publisher(self):
        conn = get_conn()
        cur = conn.cursor()
        sql = "select publisher_name from publisher"
        cur.execute(sql)
        data = cur.fetchall()

        if data:
            self.publisher_table.setRowCount(0)
            self.publisher_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.publisher_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.publisher_table.rowCount()
                self.publisher_table.insertRow(row_position)

    # 将基础数据和combobox绑定 显示在下拉列表中
    def show_category_combobox(self):
        conn = get_conn()
        cur = conn.cursor()
        sql = "select category_name from category"
        cur.execute(sql)
        data = cur.fetchall()

        if data:
            self.add_book_type.clear()
            self.edit_book_type.clear()
            for category in data:
                self.add_book_type.addItem(category[0])
                self.edit_book_type.addItem(category[0])

    def show_author_combobox(self):
        conn = get_conn()
        cur = conn.cursor()
        sql = "select author_name from author"
        cur.execute(sql)
        data = cur.fetchall()

        if data:
            self.add_book_author.clear()
            self.edit_book_author.clear()
            for author in data:
                self.add_book_author.addItem(author[0])
                self.edit_book_author.addItem(author[0])

    def show_publisher_combobox(self):
        conn = get_conn()
        cur = conn.cursor()
        sql = "select publisher_name from publisher"
        cur.execute(sql)
        data = cur.fetchall()

        if data:
            self.add_book_publisher.clear()
            self.edit_book_publisher.clear()
            for publisher in data:
                self.add_book_publisher.addItem(publisher[0])
                self.edit_book_publisher.addItem(publisher[0])

    # 获取所有图书
    def show_books(self):
        #  数据库操作流程
        # 1、获取连接
        conn = get_conn()
        # 2、获取cursor
        cur = conn.cursor()
        sql = "select book_code, book_name, book_description, book_category," \
              " book_author, book_publisher, book_price from book"
        cur.execute(sql)
        data = cur.fetchall()

        self.book_table.setRowCount(0)
        self.book_table.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.book_table.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_postion = self.book_table.rowCount()
            self.book_table.insertRow(row_postion)


 # 主题设置
    def dark_blue_theme(self):
        style = open("themes/darkblue.css", 'r')
        style = style.read()
        self.setStyleSheet(style)

    # 主题设置
    def dark_gray_theme(self):
        style = open("themes/darkgray.css", 'r')
        style = style.read()
        self.setStyleSheet(style)

    # 主题设置
    def dark_orange_theme(self):
        style = open("themes/darkorange.css", 'r')
        style = style.read()
        self.setStyleSheet(style)

    # 主题设置
    def qdark_theme(self):
        style = open("themes/qdark.css", 'r')
        style = style.read()
        self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
