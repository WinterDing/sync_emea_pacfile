#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Winter Ding"
# Email: flyawaydxd@126.com

from PyQt5.QtWidgets import QApplication, QTextBrowser, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
import sys
from sync_pacfile import main
from sync_log import logger


class PushButton(QWidget):
    def __init__(self, func):
        self.func = func
        self.res = None
        super(PushButton,self).__init__()
        self.initUI()
    def initUI(self):

        self.syncButton = QPushButton('Sync EMEA Pacfile')
        self.logButton = QPushButton('Show Status')
        self.clearButton = QPushButton('Clear Status')
        self.closeButton = QPushButton('Close Window')

        self.lcd = QTextBrowser()
        self.lcd.setFixedHeight(90)
        self.lcd.setFont(QFont("Microsoft YaHei", 10))

        self.syncButton.clicked.connect(self.sync)
        self.closeButton.clicked.connect(self.close)
        self.clearButton.clicked.connect(self.clearText)
        self.logButton.clicked.connect(self.showLog)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.syncButton)
        buttonLayout.addWidget(self.logButton)
        buttonLayout.addWidget(self.clearButton)
        buttonLayout.addWidget(self.closeButton)


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(self.lcd)


        self.setLayout(mainLayout)
        self.setWindowTitle("PushButton_test")
        self.show()

    def sync(self):
        self.res = 'process'
        self.res = self.func()
        logger.info('End: Sync process finish')

    def clearText(self):
        self.lcd.clear()

    def showLog(self):
        res_mesg = {
            'fail': 'Fail to sync, please check log file',
            'success': 'Sync finish, please verify',
            'process': 'Sync is in process, please wait',
            None: 'Sync has not start, please click "Sync EMEA Pacfile"'
        }
        self.lcd.setText(res_mesg[self.res])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButton(main)
    sys.exit(app.exec_())
