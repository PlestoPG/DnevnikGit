from datetime import datetime
from requests import Session
from urllib.parse import urlparse, parse_qs
from os import path, environ, system
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStyle, QApplication, QMainWindow
from pyperclip import copy


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon(resource_path('app_icon.ico'))
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(85, 0, 127);")
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(550, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMinimumSize(QtCore.QSize(500, 550))
        self.verticalWidget.setMaximumSize(QtCore.QSize(500, 550))
        self.verticalWidget.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: rgb(255,212,1);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 3)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.labellogin = QtWidgets.QLabel(parent=self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labellogin.sizePolicy().hasHeightForWidth())
        self.labellogin.setSizePolicy(sizePolicy)
        self.labellogin.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(30)
        font.setBold(False)
        font.setKerning(False)
        self.labellogin.setFont(font)
        self.labellogin.setStyleSheet("border: 0 px solid gray;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.labellogin.setObjectName("labellogin")
        self.horizontalLayout_2.addWidget(self.labellogin, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.exit_button = QtWidgets.QToolButton(parent=self.verticalWidget)
        self.exit_button.setMinimumSize(QtCore.QSize(30, 30))
        self.exit_button.setMaximumSize(QtCore.QSize(30, 30))
        self.exit_button.setMouseTracking(False)
        self.exit_button.setTabletTracking(False)
        self.exit_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.exit_button.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 15px;\n"
"padding: 0 8px;\n"
"background-color: rgb(255,160,1);")
        self.exit_button.setText("")
        self.exit_button.setIconSize(QtCore.QSize(24, 24))
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_2.addWidget(self.exit_button, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.inputlogin = QtWidgets.QLineEdit(parent=self.verticalWidget)
        self.inputlogin.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputlogin.sizePolicy().hasHeightForWidth())
        self.inputlogin.setSizePolicy(sizePolicy)
        self.inputlogin.setMinimumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(20)
        self.inputlogin.setFont(font)
        self.inputlogin.setStyleSheet("selection-background-color: rgb(200,180,1);\n"
"background-color: rgb(160,130,1);")
        self.inputlogin.setObjectName("inputlogin")
        self.verticalLayout_2.addWidget(self.inputlogin, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelpassword = QtWidgets.QLabel(parent=self.verticalWidget)
        self.labelpassword.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(30)
        font.setKerning(False)
        self.labelpassword.setFont(font)
        self.labelpassword.setStyleSheet("border: 0px solid gray;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.labelpassword.setObjectName("labelpassword")
        self.verticalLayout_3.addWidget(self.labelpassword, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.inputpassword = QtWidgets.QLineEdit(parent=self.verticalWidget)
        self.inputpassword.setMinimumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(20)
        self.inputpassword.setFont(font)
        self.inputpassword.setStyleSheet("background-color: rgb(160,130,1);\n"
"")
        self.inputpassword.setObjectName("inputpassword")
        self.verticalLayout_3.addWidget(self.inputpassword, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.enter = QtWidgets.QPushButton(parent=self.verticalWidget)
        self.enter.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(25)
        self.enter.setFont(font)
        self.enter.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.enter.setMouseTracking(False)
        self.enter.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255,212,1);\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,130,1);\n"
"    border-style: inset;\n"
"}")
        self.enter.setObjectName("enter")
        self.verticalLayout.addWidget(self.enter, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(400, 50))
        self.textBrowser.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraLight")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(160,130,1);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(370, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(440, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255,212,1);\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(160,130,1);\n"
"    border-style: inset;\n"
"}")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.enter, self.textBrowser)
        MainWindow.setTabOrder(self.textBrowser, self.inputlogin)
        MainWindow.setTabOrder(self.inputlogin, self.inputpassword)
        MainWindow.setTabOrder(self.inputpassword, self.enter)
        MainWindow.setTabOrder(self.enter, self.inputlogin)
        MainWindow.setTabOrder(self.inputlogin, self.textBrowser)
        MainWindow.setTabOrder(self.textBrowser, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Оценки"))
        self.labellogin.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Логин</p></body></html>"))
        self.labelpassword.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Пароль</p></body></html>"))
        self.enter.setText(_translate("MainWindow", "Войти"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Montserrat ExtraLight\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Здесь появится результат выполнения</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Нажми сюда для копирования текста"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Оценки')
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.oldPos = self.pos()
        self.show()

        if path.exists('Данные для входа'):
            with open('Данные для входа') as file:
                d_login, d_password = file.readlines()
                self.ui.inputlogin.setText(d_login)
                self.ui.inputpassword.setText(d_password)
        else:
            font = self.ui.enter.font()
            font.setPointSize(20)
            self.ui.enter.setFont(font)
            self.ui.enter.setText('Введите данные для входа')
            self.ui.enter.setEnabled(False)

        self.ui.inputlogin.textChanged.connect(self.ignite_enter_button)
        self.ui.inputpassword.textChanged.connect(self.ignite_enter_button)

        a = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton)
        self.ui.exit_button.setIcon(a)
        self.ui.exit_button.pressed.connect(self.close)
        self.ui.pushButton.pressed.connect(self.copy_output)
        self.ui.enter.pressed.connect(self.enter_pressed)
        self.copy_button()

    def copy_button(self, visible: bool = False):
        if visible:
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton.setStyleSheet("QPushButton {\nbackground-color: rgb(255,212,1);\npadding: 6px;\n}\n"
                                             "QPushButton:pressed {\nbackground-color: rgb(160,130,1);"
                                             "\nborder-style: inset;\n}")
            self.ui.pushButton.setText('Нажми сюда для копирования текста')
        else:
            self.ui.pushButton.setStyleSheet("border: 0px; color:rgb(255,212,1)")

    def copy_output(self):
        copy(self.ui.textBrowser.toPlainText())
        self.ui.pushButton.setText('Скопировано')
        self.ui.pushButton.setEnabled(False)

    def ignite_enter_button(self):
        with open('Данные для входа', 'w') as file:
            login = self.ui.inputlogin.text().strip("\n")
            password = self.ui.inputpassword.text().strip("\n")
            file.write(f'{login}\n{password}')
        if self.ui.inputlogin.text() and self.ui.inputpassword.text():
            font = self.ui.enter.font()
            font.setPointSize(25)
            self.ui.enter.setFont(font)
            self.ui.enter.setEnabled(True)
            self.ui.enter.setText('Войти')
        else:
            font = self.ui.enter.font()
            font.setPointSize(20)
            self.ui.enter.setFont(font)
            self.ui.enter.setEnabled(False)
            self.ui.enter.setText('Введите данные для входа')

    def enter_pressed(self):
        self.copy_button()
        self.ui.inputlogin.setEnabled(False)
        self.ui.inputpassword.setEnabled(False)
        self.ui.enter.setEnabled(False)
        self.ui.enter.setText('Обрабатываю...')
        try:
            if path.exists('Данные для входа') and (lines := open('Данные для входа').readlines()):
                d_login, d_password = lines
            else:
                d_login = input('Введите логин: ').strip()
                d_password = input('Введите пароль: ').strip()
            dn = DnevnikAPI(login=d_login, password=d_password)
            person = dn.get_info()['personId']
            marks_dict = {}
            today = datetime.today()
            if today.month < 6:
                start = datetime(today.year, 1, 1)
                end = datetime(today.year, 6, 1)
            else:
                start = datetime(today.year, 8, 1)
                end = datetime(today.year, 12, 31)
            for mark in dn.get_person_marks(person, dn.get_school()[0]['id'], start, end):
                lesson = dn.get_lesson_info(mark['lesson'])
                if lesson['subject']['name'] in marks_dict:
                    marks_dict[lesson['subject']['name']].append(int(mark['value']))
                else:
                    marks_dict[lesson['subject']['name']] = [int(mark['value'])]
            if marks_dict:
                reply = 'Целиком скопируй эту и следующую строки Школьному ассистенту во время добавления оценок.\n'
                self.ui.textBrowser.setText(f'{reply}{marks_dict}')
                self.copy_button(True)
                self.ui.enter.setEnabled(True)
            else:
                dates = f'{start.strftime("%d.%m.%y")} по {end.strftime("%d.%m.%y")}'
                self.ui.textBrowser.setText(f'Похоже, что оценки в период с {dates} отсутствуют.')
        except DiaryError:
            self.ui.textBrowser.setText('Не удалось войти, указанные данные недействительны')
        self.ui.enter.setText('Попробовать снова')
        self.ui.inputlogin.setEnabled(True)
        self.ui.inputpassword.setEnabled(True)

    """families = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont("Montserrat-Bold.ttf"))
        self.setMinimumSize(600, 800)
        self.setWindowTitle('Получение оценок из Дневника.ру')

        self.labellogin = QLabel()
        self.labellogin.setText('Логин')
        self.labellogin.setFont(QFont(families[0], 60))
        self.inputlogin = QLineEdit()
        self.inputlogin.setMinimumSize(500, 100)
        self.inputlogin.setPlaceholderText('Напиши логин сюда')

        self.labelpassword = QLabel()
        self.labelpassword.setText('Пароль')
        self.labelpassword.setFont(QFont(families[0], 60))
        self.inputpassword = QLineEdit()
        self.inputpassword.setMinimumSize(500, 100)
        self.inputpassword.setPlaceholderText('Напиши пароль сюда')

        self.enter = QPushButton("Войти")
        self.enter.setFont(QFont(families[0], 60))
        self.enter.setFixedSize(400, 100)
        self.enter.se('Qt::AlignLeft')
        self.enter.clicked.connect(self.the_enter_was_clicked)

        self.output = QLabel()
        self.output.setText('Вывод информации')
        self.output.setFont(QFont(families[0], 60))

        layout = QVBoxLayout()
        layout.addWidget(self.labellogin)
        layout.addWidget(self.inputlogin)
        layout.addWidget(self.labelpassword)
        layout.addWidget(self.inputpassword)
        layout.addWidget(self.enter)
        layout.addWidget(self.output)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)"""

    def the_enter_was_clicked(self):
        if True:
            self.enter.setEnabled(False)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()


class DnevnikBase:
    def __init__(self, login: str = None, password: str = None, token: str = None):
        self.session = Session()
        self.host = 'https://api.dnevnik.ru/v2/'
        self.token = token
        if token is None:
            self.token = self.get_token(login, password)
        self.session.headers = {"Access-Token": self.token}

    def get_token(self, login: str = None, password: str = None):
        client_id = 'bb97b3e445a340b9b9cab4b9ea0dbd6f'
        ret_url = f'https://login.dnevnik.ru/oauth2?response_type=token&client_id={client_id}&scope=EducationalInfo'
        params_dict = {"ReturnUrl": ret_url, "login": login, "password": password}
        token = self.session.post('https://login.dnevnik.ru/login/', params=params_dict, allow_redirects=True)
        parsed_url = urlparse(token.url)
        query = parse_qs(parsed_url.query)
        result = query.get("result")
        if result is None or result[0] != "success":
            token = self.session.post(ret_url)
            parsed_url = urlparse(token.url)
            query = parse_qs(parsed_url.query)
            result = query.get("result")
            if result is None or result[0] != "success":
                raise DiaryError("Что то не так с авторизацией")

        if token.status_code != 200:
            raise DiaryError("Сайт лежит или ведутся технические работы, использование api временно невозможно")
        token = parsed_url.fragment[13:-7]
        return token

    @staticmethod
    def _check_response(response):
        if response.headers.get("Content-Type") == "text/html":
            error_html = response.content.decode()
            e_text = error_html.split('<div class="error__description">')[-1].split("<p>")[1].strip()[:-4].split()
            error_text = " ".join(word for word in e_text)
            raise DiaryError(error_text)
        json_response = response.json()
        if isinstance(json_response, dict):
            if json_response.get("type") == "parameterInvalid":
                raise DiaryError(json_response["description"])
            if json_response.get("type") == "apiServerError":
                raise DiaryError("Неизвестная ошибка в API, проверьте правильность параметров")
            if json_response.get("type") == "apiUnknownError":
                raise DiaryError("Неизвестная ошибка в API, проверьте правильность параметров")
            if json_response.get("type") == "authorizationFailed":
                raise DiaryError("Ошибка авторизации")

    def get(self, method: str, params=None, **kwargs):
        if params is None:
            params = {}
        response = self.session.get(self.host + method, params=params, **kwargs)
        self._check_response(response)
        return response.json()

    def __enter__(self):
        return self


class DnevnikAPI(DnevnikBase):
    def __init__(self, login: str = None, password: str = None, token: str = None):
        super().__init__(login, password, token)
        self.login = login
        self.password = password

    def get_school(self):
        school_id = self.get("schools/person-schools")
        return school_id

    def get_info(self):
        user_id = self.get("users/me")
        return user_id

    def get_person_marks(self, person_id: int, school_id: int, start_time: datetime, end_time: datetime):
        marks = self.get(f"persons/{person_id}/schools/{school_id}/marks/{start_time}/{end_time}")
        return marks

    def get_lesson_info(self, lesson_id: int):
        lesson_info = self.get(f"lessons/{lesson_id}")
        return lesson_info


class DiaryError(Exception):
    pass


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
