from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QWidget , QLabel, QPushButton, QHBoxLayout, QVBoxLayout 
app = QApplication([])
my_win.setWindowTitle('YUHU')
my_win.move(900,70)
my_win.resize(400,200)
v_line = QVBoxLayout()
winner = QLabel('Победитель')
v_line.addWidget(
    title, alignment = Qt.AlignCenter
)
my_win.setLayout(v_line)
my_win.show()
app.exec_()