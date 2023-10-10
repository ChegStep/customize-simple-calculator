# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_color.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(497, 191)
        Dialog.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #666\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_color_form_2 = QPushButton(Dialog)
        self.btn_color_form_2.setObjectName(u"btn_color_form_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_color_form_2.sizePolicy().hasHeightForWidth())
        self.btn_color_form_2.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.btn_color_form_2, 0, 0, 1, 1)

        self.btn_color_text_2 = QPushButton(Dialog)
        self.btn_color_text_2.setObjectName(u"btn_color_text_2")
        sizePolicy.setHeightForWidth(self.btn_color_text_2.sizePolicy().hasHeightForWidth())
        self.btn_color_text_2.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.btn_color_text_2, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430", None))
        self.btn_color_form_2.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430 \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440\u0430", None))
        self.btn_color_text_2.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430 \u0442\u0435\u043a\u0441\u0442\u0430", None))
    # retranslateUi

