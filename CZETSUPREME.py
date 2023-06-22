import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Prev', self)
        back_btn.triggered.connect(self.browser.back) 
        navbar.addAction(back_btn)

        forward_btn = QAction('Next', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.Url_bar = QLineEdit()
        self.Url_bar.returnPressed.connect(self.navigate_to_Url)
        navbar.addWidget(self.Url_bar)

        self.browser.urlChanged.connect(self.update_Url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))

    def navigate_to_Url(self):
        Url = self.Url_bar.text()
        self.browser.setUrl(QUrl(Url))

    def update_Url(self, Url):
        self.Url_bar.setText(Url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('SUPREME')
window = MainWindow()
app.exec_()