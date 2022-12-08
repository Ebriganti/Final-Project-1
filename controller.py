from PyQt5.QtWidgets import *
from view import *
from cats import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    """
    Houses the functions for aspects of the gui with functionality
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the window
        :param args: parts of the window
        :param kwargs: aspects of the window
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_submit.clicked.connect(lambda: self.ear_submit())
        self.pushButton_clear.clicked.connect(lambda: self.ear_clear())
        self.pushButton_submit_2.clicked.connect(lambda: self.exp_submit())
        self.pushButton_clear_2.clicked.connect(lambda: self.exp_clear())
    def ear_submit(self) -> None:
        """
        Submits ear calculator data and changes the output accordingly
        """
        try:
            amount = int(self.lineEdit_amount.text())
            if self.radioButton_cat.isChecked():
                self.label_output.setText(f'The {amount} cats have {cat_ears(amount)} ears!')
            elif self.radioButton_alien.isChecked():
                self.label_output.setText(f'The {amount} aliens have {alien_ears(amount)} ears!')
        except:
            self.label_output.setText(f'Amount must be a positive whole number.')

    def ear_clear(self) -> None:
        """
        Clears the ear calculator input, clears the output, and clicks the cat radio button
        """
        self.lineEdit_amount.setText('')
        self.radioButton_cat.setChecked(True)
        self.label_output.setText('')

    def exp_submit(self) -> None:
        """
        Submits exponent calculator data and changes the output accordingly
        """
        try:
            base = float(self.lineEdit_base.text())
            exponent = float(self.lineEdit_power.text())
            self.label_output_2.setText(f'The answer is {power(base,exponent)}')
        except:
            self.label_output_2.setText(f'Base and power must be integers or floats\nNegative bases cannot have a float as a power')

    def exp_clear(self) -> None:
        """
        Clears the exponent calculator inputs and output
        """
        self.lineEdit_base.setText('')
        self.lineEdit_power.setText('')
        self.label_output_2.setText('')