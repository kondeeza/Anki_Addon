# -*- coding: utf-8 -*-
#
# Entry point for the add-on into Anki
# Please do not edit this if you do not know what you are doing.
#
# Copyright: mo  <paradoxez919@gmail.com>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>
from anki.hooks import addHook
from aqt.qt import *



def setupMenu(browser):
    menu = browser.form.menuEdit
    menu.addSeparator()
    q = menu.addAction('KR_00_temp_addon')
    q.triggered.connect(lambda _, b=browser: onclicked(b))


def onclicked(b):
    Form, Window = uic.loadUiType("untitled.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec()


addHook("browser.setupMenus", setupMenu)