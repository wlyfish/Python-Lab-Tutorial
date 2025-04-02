#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2025/4/2 14:11
 @Author  : wly
 @File    : 参考文献查重.py
 @Description: 
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QListWidget, QListWidgetItem, \
    QVBoxLayout, QWidget, QHBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor
from PyQt5.QtCore import Qt
import re


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('参考文献重复检测（基于标题）')
        self.setGeometry(100, 100, 1000, 600)

        # 创建输入框
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("在此输入参考文献列表")

        # 创建检测按钮
        self.detect_button = QPushButton("检测重复（按标题）")
        self.detect_button.clicked.connect(self.detect_duplicates_by_title)

        # 创建结果显示列表
        self.result_list = QListWidget()
        self.result_list.itemClicked.connect(self.highlight_by_title)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.input_text)
        layout.addWidget(self.detect_button)
        layout.addWidget(self.result_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def detect_duplicates_by_title(self):
        text = self.input_text.toPlainText()
        entries = self.parse_entries(text)
        duplicates = self.find_duplicates_by_title(entries)

        self.result_list.clear()
        if not duplicates:
            QMessageBox.information(self, "检测结果", "未发现重复的参考文献标题")
            return

        for key in duplicates:
            items = duplicates[key]
            if len(items) > 1:
                item_text = f"重复标题：{key}（条目：{', '.join([str(e['编号']) for e in items])}）"
                list_item = QListWidgetItem(item_text)
                list_item.setData(Qt.UserRole, items)
                self.result_list.addItem(list_item)

    def parse_entries(self, text):
        entries = []
        lines = text.split('\n')
        current_entry = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('[') and ']' in stripped:
                if current_entry:
                    entry_text = ' '.join(current_entry)
                    parsed_entry = self.parse_entry(entry_text)
                    if parsed_entry:
                        entries.append(parsed_entry)
                    current_entry = []
                current_entry.append(line)
            else:
                current_entry.append(line)
        if current_entry:
            entry_text = ' '.join(current_entry)
            parsed_entry = self.parse_entry(entry_text)
            if parsed_entry:
                entries.append(parsed_entry)
        return entries

    def parse_entry(self, entry_text):
        entry = {}
        number_part = entry_text.split(']')[0]
        entry['编号'] = number_part.strip('[]').strip()

        # 使用正则提取标题（标题在第一个句号之后，第二个句号之前）
        match = re.search(r'\.\s*(.*?)\s*\.', entry_text)
        if match:
            title = match.group(1).strip()
            # 标题标准化处理：去除标点、转小写、去空格
            standardized_title = re.sub(r'[^\w]+', ' ', title).strip().lower()
            entry['标题'] = title
            entry['标准化标题'] = standardized_title
            entry['原始文本'] = entry_text
            return entry
        else:
            return None  # 格式错误无法提取标题

    def find_duplicates_by_title(self, entries):
        duplicates = {}
        for entry in entries:
            key = entry['标准化标题']
            if key in duplicates:
                duplicates[key].append(entry)
            else:
                duplicates[key] = [entry]
        result = {}
        for key in duplicates:
            if len(duplicates[key]) > 1:
                result[key] = duplicates[key]
        return result

    def highlight_by_title(self, item):
        entries = item.data(Qt.UserRole)
        cursor = self.input_text.textCursor()
        cursor.beginEditBlock()

        # 清除之前的高亮
        format = cursor.charFormat()
        format.setBackground(Qt.white)
        cursor.select(QTextCursor.Document)
        cursor.mergeCharFormat(format)

        # 高亮所有包含该标题的条目
        for entry in entries:
            search_text = entry['标题']
            normalized_search = entry['标准化标题']
            # 使用标准化标题进行模糊匹配
            pattern = re.compile(re.escape(search_text), re.IGNORECASE)

            # 搜索所有匹配项
            pos = 0
            while True:
                index = self.input_text.toPlainText().lower().find(normalized_search, pos)
                if index == -1:
                    break
                cursor.setPosition(index)
                cursor.movePosition(QTextCursor.EndOfLine, QTextCursor.KeepAnchor)
                format = QTextCharFormat()
                format.setBackground(QColor("#FFFF00"))
                cursor.mergeCharFormat(format)
                pos = index + len(search_text)

        # 滚动到第一个匹配位置
        if entries:
            cursor.setPosition(entries[0]['原始文本'].find(entries[0]['标题']))
            self.input_text.setTextCursor(cursor)
        cursor.endEditBlock()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())