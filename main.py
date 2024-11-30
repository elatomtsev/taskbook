from ui_main import Ui_MainWindow
from ui_dlg import Dialog

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt, QDateTime


# Сортировка дат работает через жопу
# Подлючить БД
# Сформировать .exe


class Start(QMainWindow):
    def __init__(self):
        super().__init__()
        # Инициализация основного окна
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dlg = Dialog(self)  #  Диалог добавления задачи
        self.dlg_edit = Dialog(self)  #  Диалог редактриования задачи

        # Если в диалоге нажата кнопка "добавить задачу"
        self.dlg.ui.but_add_task.clicked.connect(self.dlg_but_clicked)
        self.dlg.ui.but_add_task.setShortcut("Return")

        # Если нажата в гл. окне "добавить задачу"
        self.ui.add_task.clicked.connect(self.process_add_task)
        self.ui.add_task.setShortcut("n")

        # Если нажата в гл. окне "удалить задача"
        self.ui.del_task.clicked.connect(self.process_del_task)
        self.ui.del_task.setShortcut("delete")

        # Запуск процесса поиска задачи
        self.ui.find_task.textChanged.connect(self.process_find)

        # Если нажата в гл. окне "редактировать задачу"
        self.ui.edit_task.clicked.connect(self.process_edit_task)

        # Массив, который добавляет строки, которые не нужно отображать во время поиска
        self.hidden_task = []

        # Если в диалоге нажата кнопка "редактировать задачу"
        self.dlg_edit.ui.but_add_task.setText("Редактировать задачу")
        self.dlg_edit.ui.but_add_task.clicked.connect(self.dlg_edit_clicked)
        self.dlg_edit.ui.but_add_task.setShortcut("return")

    # Нажата кнопка "добавить задача" и запущен диалог
    def process_add_task(self):
        self.dlg.open()
        self.dlg.ui.date_add_task.setDateTime(QDateTime.currentDateTime())

    # Нажата кнопка "удалить задачу"
    def process_del_task(self):
        self.ui.table_task.removeRow(self.ui.table_task.currentRow())

    # В диалоге нажата кнопка "создать задачу"
    def dlg_but_clicked(self):
        if self.dlg.ui.name_add_task.text().strip(" "):
            self.ui.table_task.insertRow(0)
            info = (
                QTableWidgetItem(self.dlg.ui.date_add_task.text()),
                QTableWidgetItem(self.dlg.ui.name_add_task.text()),
            )
            self.ui.table_task.setItem(0, 0, info[0])
            self.ui.table_task.setItem(0, 1, info[1])

            self.dlg.close()
            self.dlg.ui.name_add_task.setText("")
            self.ui.table_task.sortByColumn(0, Qt.SortOrder.DescendingOrder)

    # Поиск задач по названию
    def process_find(self):
        # Отображаем все раннее спрятанные строки
        for i in self.hidden_task:
            self.ui.table_task.showRow(i)
        self.hidden_task.clear()

        # Прячем новые строки, которые не являются надстрокой поиска
        self.hidden_task = [
            i
            for i in range(self.ui.table_task.rowCount())
            if self.ui.find_task.text().lower().strip(" ")
            not in self.ui.table_task.item(i, 1).text().lower()
        ]
        for i in self.hidden_task:
            self.ui.table_task.hideRow(i)

    # Запущен диалог редактировать задачу и нажата кнопка "редактировать задачу"
    def process_edit_task(self):
        if self.ui.table_task.currentRow() == -1:
            return 0  # Если не выбран строка, то не открываем диалог
        self.dlg_edit.open()
        cur_row = self.ui.table_task.currentRow()
        self.dlg_edit.ui.name_add_task.setText(
            self.ui.table_task.item(cur_row, 1).text()
        )
        self.dlg_edit.ui.date_add_task.setDateTime(
            QDateTime.fromString(
                self.ui.table_task.item(cur_row, 0).text(), "dd.MM.yyyy h:m"
            )
        )

    # В диалоге нажата кнопка "редактировать задачу"
    def dlg_edit_clicked(self):
        if self.dlg_edit.ui.name_add_task.text().strip(" "):
            info = (
                QTableWidgetItem(self.dlg_edit.ui.date_add_task.text()),
                QTableWidgetItem(self.dlg_edit.ui.name_add_task.text()),
            )
            cur_row = self.ui.table_task.currentRow()
            self.ui.table_task.setItem(cur_row, 0, info[0])
            self.ui.table_task.setItem(cur_row, 1, info[1])

            self.dlg_edit.close()
            self.ui.table_task.sortByColumn(0, Qt.SortOrder.DescendingOrder)


if __name__ == "__main__":
    app = QApplication([])
    window = Start()
    window.show()

    app.exec()
