# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc-design.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_cl

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(527, 664)
        MainWindow.setMinimumSize(QSize(350, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculate.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(50, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none")
        self.le_entry.setMaxLength(10)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.gridLayout.addWidget(self.le_entry, 1, 0, 1, 2)

        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        self.lbl_temp.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy1)
        self.lbl_temp.setBaseSize(QSize(0, 0))
        self.lbl_temp.setStyleSheet(u"color: #888")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_temp, 0, 1, 1, 1)

        self.btn_set_colors = QPushButton(self.centralwidget)
        self.btn_set_colors.setObjectName(u"btn_set_colors")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_set_colors.sizePolicy().hasHeightForWidth())
        self.btn_set_colors.setSizePolicy(sizePolicy2)
        self.btn_set_colors.setMinimumSize(QSize(0, 0))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/\u0448\u0435\u0441\u0442\u0435\u0440\u043d\u044f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_set_colors.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_set_colors, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.lt_buttons = QGridLayout()
        self.lt_buttons.setObjectName(u"lt_buttons")
        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy3)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy3.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy3)
        self.btn_point.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy3.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy3)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_bckspace = QPushButton(self.centralwidget)
        self.btn_bckspace.setObjectName(u"btn_bckspace")
        sizePolicy3.setHeightForWidth(self.btn_bckspace.sizePolicy().hasHeightForWidth())
        self.btn_bckspace.setSizePolicy(sizePolicy3)
        self.btn_bckspace.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/back3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_bckspace.setIcon(icon2)
        self.btn_bckspace.setIconSize(QSize(30, 30))

        self.lt_buttons.addWidget(self.btn_bckspace, 0, 2, 1, 1)

        self.btn_ce = QPushButton(self.centralwidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy3.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy3)
        self.btn_ce.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_ce, 0, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy3.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy3)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy3.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy3)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_idk = QPushButton(self.centralwidget)
        self.btn_idk.setObjectName(u"btn_idk")
        sizePolicy3.setHeightForWidth(self.btn_idk.sizePolicy().hasHeightForWidth())
        self.btn_idk.setSizePolicy(sizePolicy3)
        self.btn_idk.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_idk, 4, 0, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy3.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy3)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy3.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy3)
        self.btn_sub.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_sub, 1, 3, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy3.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy3)
        self.btn_minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_del = QPushButton(self.centralwidget)
        self.btn_del.setObjectName(u"btn_del")
        sizePolicy3.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy3)
        self.btn_del.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_del, 0, 3, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy3.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy3)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy3.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy3)
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy3.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy3)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy3.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy3)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy3.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy3)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy3.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy3)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_otvet = QPushButton(self.centralwidget)
        self.btn_otvet.setObjectName(u"btn_otvet")
        sizePolicy3.setHeightForWidth(self.btn_otvet.sizePolicy().hasHeightForWidth())
        self.btn_otvet.setSizePolicy(sizePolicy3)
        self.btn_otvet.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn_otvet, 4, 3, 1, 1)

        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        sizePolicy3.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy3)
        self.btn3.setCursor(QCursor(Qt.PointingHandCursor))

        self.lt_buttons.addWidget(self.btn3, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.lt_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculate Customs", None))
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_temp.setText("")
        self.btn_set_colors.setText("")
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_bckspace.setText("")
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_idk.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_del.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_otvet.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_otvet.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

