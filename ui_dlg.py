# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDialog, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_dlg_add_task(object):
    def setupUi(self, dlg_add_task):
        if not dlg_add_task.objectName():
            dlg_add_task.setObjectName(u"dlg_add_task")
        dlg_add_task.resize(327, 149)
        icon = QIcon()
        icon.addFile(u"icons/animal-penguin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        dlg_add_task.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(dlg_add_task)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_add_task = QLineEdit(dlg_add_task)
        self.name_add_task.setObjectName(u"name_add_task")

        self.verticalLayout.addWidget(self.name_add_task)

        self.date_add_task = QDateTimeEdit(dlg_add_task)
        self.date_add_task.setObjectName(u"date_add_task")

        self.verticalLayout.addWidget(self.date_add_task)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.but_add_task = QPushButton(dlg_add_task)
        self.but_add_task.setObjectName(u"but_add_task")

        self.verticalLayout.addWidget(self.but_add_task)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(dlg_add_task)

        QMetaObject.connectSlotsByName(dlg_add_task)
    # setupUi

    def retranslateUi(self, dlg_add_task):
        dlg_add_task.setWindowTitle(QCoreApplication.translate("dlg_add_task", u"\u0417\u0430\u0434\u0430\u0447\u0430", None))
        self.name_add_task.setPlaceholderText(QCoreApplication.translate("dlg_add_task", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435...", None))
        self.but_add_task.setText(QCoreApplication.translate("dlg_add_task", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
    # retranslateUi

class Dialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_dlg_add_task()
        self.ui.setupUi(self)