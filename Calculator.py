# from PySide6.QtWidgets import QApplication, QWidget,QPushButton

# # Only needed for access to command line arguments
# import sys

# # You need one (and only one) QApplication instance per application.
# # Pass in sys.argv to allow command line arguments for your app.
# # If you know you won't use command line arguments QApplication([]) works too.
# app = QApplication(sys.argv)

# # Create a Qt widget, which will be our window.
# window = QWidget()
# x = QPushButton("Push Me")

# window.show(x)  # IMPORTANT!!!!! Windows are hidden by default.

# # Start the event loop.
# app.exec()

# # Your application won't reach here until you exit and the event
# # loop has stopped.




# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# # 1. Create the Application Engine (required)
# app = QApplication(sys.argv)

# # 2. Create the main Window (the car)
# window = QMainWindow()
# window.setWindowTitle("Calculator")
# window.setGeometry(300, 300, 400, 500)  # (x, y, width, height)


# window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# # Start the event loop.
# sys.exit(app.exec())



import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My First App")
window.setGeometry(300, 300, 400, 200)

button = QPushButton("Click Me!")
window.setCentralWidget(button)

def on_button_click():
    button.setText("I was clicked!")

button.clicked.connect(on_button_click)

window.show()
sys.exit(app.exec())
