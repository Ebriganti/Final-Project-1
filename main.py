from controller import*

def main():
    """
    Creates the window for the gui
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()