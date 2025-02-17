# Execute this script with the command below to open the GUI
# python run.py

import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from src.ui.run_ui import Main_Dialog
# from src.ui.splash import Splash_Dialog

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    app = QtWidgets.QApplication(sys.argv)

    ui = Main_Dialog()
    ui.show()

    # splash = Splash_Dialog()
    # splash.show()

    sys.exit(app.exec_())
