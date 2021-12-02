# Import stuff
import sys
from PyQt5 import QtWidgets
from window import Ui_MainWindow


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    print('[INFO] Starting application...')
    # Create the Qt Application
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())

