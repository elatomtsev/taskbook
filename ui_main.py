# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zadacha.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(621, 423)
        icon = QIcon()
        icon.addFile(u"icons/book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.find_task = QLineEdit(self.frame_2)
        self.find_task.setObjectName(u"find_task")

        self.horizontalLayout_2.addWidget(self.find_task)

        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.add_task = QPushButton(self.frame_2)
        self.add_task.setObjectName(u"add_task")

        self.horizontalLayout_2.addWidget(self.add_task)


        self.verticalLayout.addWidget(self.frame_2)

        self.table_task = QTableWidget(self.centralwidget)
        if (self.table_task.columnCount() < 2):
            self.table_task.setColumnCount(2)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.table_task.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.table_task.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_task.setObjectName(u"table_task")
        self.table_task.setShowGrid(True)
        self.table_task.setGridStyle(Qt.PenStyle.SolidLine)
        self.table_task.setRowCount(0)
        self.table_task.setColumnCount(2)
        self.table_task.horizontalHeader().setVisible(True)
        self.table_task.horizontalHeader().setCascadingSectionResizes(False)
        self.table_task.horizontalHeader().setDefaultSectionSize(100)
        self.table_task.horizontalHeader().setHighlightSections(True)
        self.table_task.horizontalHeader().setStretchLastSection(True)
        self.table_task.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.table_task)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edit_task = QPushButton(self.frame)
        self.edit_task.setObjectName(u"edit_task")

        self.horizontalLayout.addWidget(self.edit_task)

        self.del_task = QPushButton(self.frame)
        self.del_task.setObjectName(u"del_task")

        self.horizontalLayout.addWidget(self.del_task)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u043d\u0438\u043a", None))
        self.find_task.setText("")
        self.find_task.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.add_task.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        ___qtablewidgetitem = self.table_task.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem1 = self.table_task.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        self.edit_task.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.del_task.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
    # retranslateUi
