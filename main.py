import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv

import PySide6
from PyQt5.uic.properties import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QColorDialog, QWidget
from PySide6.QtGui import *
import re

from cl_design import Ui_MainWindow
from set_colors import Ui_Dialog

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

default_font_size = 16
default_entry_font_size = 40

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry_max_len = self.ui.le_entry.maxLength()
        # numbers
        self.ui.btn_0.clicked.connect(self.add_digits)
        self.ui.btn_1.clicked.connect(self.add_digits)
        self.ui.btn_2.clicked.connect(self.add_digits)
        self.ui.btn3.clicked.connect(self.add_digits)
        self.ui.btn_4.clicked.connect(self.add_digits)
        self.ui.btn_5.clicked.connect(self.add_digits)
        self.ui.btn_6.clicked.connect(self.add_digits)
        self.ui.btn_7.clicked.connect(self.add_digits)
        self.ui.btn_8.clicked.connect(self.add_digits)
        self.ui.btn_9.clicked.connect(self.add_digits)
        #actions
        self.ui.btn_clear.clicked.connect(self.clear_digits)
        self.ui.btn_ce.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)
        self.ui.btn_idk.clicked.connect(self.negative)
        self.ui.btn_bckspace.clicked.connect(self.backspace)
        #mathematic
        self.ui.btn_otvet.clicked.connect(self.calculate)
        self.ui.btn_plus.clicked.connect(self.math_op)
        self.ui.btn_minus.clicked.connect(self.math_op)
        self.ui.btn_sub.clicked.connect(self.math_op)
        self.ui.btn_del.clicked.connect(self.math_op)
        #setting
        self.ui.btn_set_colors.clicked.connect(self.open_set_color_wind)
        self.set_col_wind = QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.set_col_wind)
        self.ui_window.btn_color_form_2.clicked.connect(self.set_color_for_form)
        self.ui_window.btn_color_text_2.clicked.connect(self.set_color_for_text)


    def open_set_color_wind(self):
        self.set_col_wind.show()

    def set_color_for_form(self):
        self.color_form = QColorDialog.getColor(QColor('#121212'), self, 'Выбор цвета интерфейса')
        data = self.open_css_file()
        data[2] = f"	background-color: {self.color_form.name()};\n"
        self.write_css_file(data)


    def set_color_for_text(self):
        self.color_text = QColorDialog.getColor(QColor('white'), self, 'Выбор цвета текста')
        data = self.open_css_file()
        data[1] = f"	color: {self.color_text.name()};\n"
        self.write_css_file(data)

    def open_css_file(self):
        with open('style.css', 'r') as file:
            data = file.readlines()
        return data

    def write_css_file(self, data):
        with open('style.css', 'w') as file:
            file.writelines(data)

        with open("style.css", "r") as file:
            app.setStyleSheet(file.read())

    def add_digits(self):
        self.clear_temp()
        btn = self.sender()

        digit_btns = ('btn_0','btn_1','btn_2','btn3','btn_4','btn_5','btn_6','btn_7','btn_8','btn_9')

        if btn.objectName() in digit_btns:
            if self.ui.le_entry.text() == '0':
                self.ui.le_entry.setText(btn.text())
            else:
                self.ui.le_entry.setText(self.ui.le_entry.text() + btn.text())

        self.adjust_entry_font_size()

    def backspace(self):
        self.clear_temp()
        entry = self.ui.le_entry.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.le_entry.setText('0')
            else:
                self.ui.le_entry.setText(entry[:-1])
        else:
            self.ui.le_entry.setText('0')

        self.adjust_entry_font_size()


    def clear_digits(self):
        self.ui.le_entry.setText('0')
        self.adjust_entry_font_size()
        self.ui.lbl_temp.clear()
        self.adjust_temp_font_size()


    def clear_entry(self):
        self.clear_temp()
        self.ui.le_entry.setText('0')
        self.adjust_entry_font_size()

    def clear_temp(self):
        if self.get_math_sign() == '=':
            self.ui.lbl_temp.clear()
            self.adjust_temp_font_size()

    def add_point(self):
        self.clear_temp()
        if '.' not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + '.')
            self.adjust_entry_font_size()

    def negative(self):
        self.clear_temp()
        entry = self.ui.le_entry.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]

        if len(entry) == self.entry_max_len + 1 and '-' in entry:
            self.ui.le_entry.setMaxLength(self.entry_max_len + 1)
        else:
            self.ui.le_entry.setMaxLength(self.entry_max_len)

        self.ui.le_entry.setText(entry)
        self.adjust_entry_font_size()

    @staticmethod
    def del_zeros_digit(num):
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self):
        btn = self.sender()
        entry = self.del_zeros_digit(self.ui.le_entry.text())

        if not self.ui.lbl_temp.text() or self.get_math_sign() == "=":
            self.ui.lbl_temp.setText(entry + f' {btn.text()} ')
            self.adjust_temp_font_size()
            self.ui.le_entry.setText('0')
            self.adjust_entry_font_size()


    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.le_entry.text().strip('.')

        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().strip('.').split()[-1]

    def get_entry_text_width(self) -> int:
        return self.ui.le_entry.fontMetrics().boundingRect(self.ui.le_entry.text()).width()

    def get_temp_text_width(self):
        return self.ui.lbl_temp.fontMetrics().boundingRect(self.ui.lbl_temp.text()).width()

    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entry.text()
        temp = self.ui.lbl_temp.text()

        if temp:
            try:
                result = self.del_zeros_digit(
                    str(operators[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
                )
                self.ui.lbl_temp.setText(temp + self.del_zeros_digit(entry) + ' =')
                self.adjust_temp_font_size()
                self.ui.le_entry.setText(result)
                self.adjust_entry_font_size()
                return result
            except:
                pass

    def math_op(self, math_sign):
        temp = self.ui.lbl_temp.text()
        btn = self.sender()

        if not temp:
            self.add_temp()
        else:
            if self.get_math_sign() != btn.text():
                if self.get_math_sign() == '=':
                    self.add_temp()
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{btn.text()} ')

            else:
                self.ui.lbl_temp.setText(self.calculate() + f'{btn.text()}')
            self.adjust_temp_font_size()

    def adjust_entry_font_size(self) -> None:
        font_size = default_entry_font_size
        while self.get_entry_text_width() > self.ui.le_entry.width() - 15:
            font_size -= 1
            self.ui.le_entry.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

        while self.get_entry_text_width() < self.ui.le_entry.width():
            font_size += 1
            if font_size > default_entry_font_size:
                break
            self.ui.le_entry.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = default_font_size
        while self.get_temp_text_width() > self.ui.lbl_temp.width() - 10:
            font_size -= 1
            self.ui.lbl_temp.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888;')

        font_size = 1
        while self.get_temp_text_width() < self.ui.lbl_temp.width() - 60:
            font_size += 1
            if font_size > default_font_size:
                break
            self.ui.lbl_temp.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888;')


    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open("style.css", "r") as file:
        app.setStyleSheet(file.read())

    window = Calculator()
    window.show()

    sys.exit(app.exec())