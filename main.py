import sys
import sqlite3

from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from addEditCoffeeForm_ui import Ui_MainWindow


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Зададим тип базы данных
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        self.db.setDatabaseName('coffee.sqlite')
        # И откроем подключение
        self.db.open()

        # QTableView - виджет для отображения данных из базы
        self.view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('main')
        self.model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        self.view.setModel(self.model)
        self.view.move(10, 10)
        self.view.resize(617, 315)

        self.setGeometry(300, 100, 650, 450)
        self.setWindowTitle('Пример работы с QtSql')

        self.btn = QPushButton('Создать/изменить', self)
        # Изменяем рамер кнопки. Теперь он 100 на 100 пикселей
        self.btn.resize(150, 90)
        # Размещаем кпопку на родительском виджете
        # по координатам (100, 100)
        self.btn.move(10, 350)
        self.btn.clicked.connect(self.op)

        self.upd_btn = QPushButton('Обновить', self)
        # Изменяем рамер кнопки. Теперь он 100 на 100 пикселей
        self.upd_btn.resize(150, 90)
        # Размещаем кпопку на родительском виджете
        # по координатам (100, 100)
        self.upd_btn.move(250, 350)
        self.upd_btn.clicked.connect(self.update)

    def update(self):
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('main')
        self.model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        self.view.setModel(self.model)

    def op(self):
        self.new = New()
        self.new.show()


class New(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pserach_ushButton.clicked.connect(self.search)
        self.id = None
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.val.setMaximum(99999)
        self.price_pinBox.setMaximum(99999)
        self.pushButton.clicked.connect(self.submit)

    def search(self):
        result = self.cur.execute(f"""SELECT * FROM main
                    WHERE id={self.ID_Edit.text()}""").fetchall()[0]
        print(result)
        self.Sort_Edit.setText(result[1])
        if result[3] == 'True':
            self.checkBox.setChecked(True)
        self.description_plainTextEdit.setPlainText(result[4])
        self.price_pinBox.setValue(result[5])
        self.roast_spinBox.setValue(int(result[2]))
        self.val.setValue(int(result[6]))
        self.id = self.ID_Edit.text()

    def submit(self):
        print(15)
        if self.id is None:
            self.cur.execute(f'''INSERT INTO main(sort_name, roast_degree, is_grains, description, price, value) 
            VALUES("{self.Sort_Edit.text()}", {self.roast_spinBox.value()}, {self.checkBox.isChecked()}, "{self.description_plainTextEdit.toPlainText()}", {self.price_pinBox.value()}, {self.val.value()})''')
            self.con.commit()
            self.hide()
        else:
            self.cur.execute(f'''UPDATE main
SET sort_name="{self.Sort_Edit.text()}",
    roast_degree={self.roast_spinBox.value()},
    is_grains={self.checkBox.isChecked()},
    description="{self.description_plainTextEdit.toPlainText()}",
    price={self.price_pinBox.value()},
    value={self.val.value()}
WHERE id={self.id}''')
            self.con.commit()
            self.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
