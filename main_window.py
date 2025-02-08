from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,\
    QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QApplication
from PyQt5.QtCore import Qt

window = QWidget()
window.resize(1000, 1000)
window.setStyleSheet('backround-color:#FAF3E0')

btn_menu = QPushButton('Меню')
btn_menu.setStyleSheet('color: #777777; backround-color:#e4dddb; font-size: 20px')

btn_rest = QPushButton('Відпочити')
btn_rest.setStyleSheet('color: #777777; backround-color:#e4dddb; font-size: 20px')

btn_next = QPushButton('Відповісти')
btn_next.setStyleSheet('color: #777777; backround-color:#e4dddb; font-size: 20px')

rb_ans1 = QRadioButton("1")
rb_ans1.setStyleSheet('font-size: 15px')

rb_ans2 = QRadioButton("2")
rb_ans2.setStyleSheet('font-size: 15px')

rb_ans3 = QRadioButton("3")
rb_ans3.setStyleSheet('font-size: 15px')

rb_ans4 = QRadioButton("4")
rb_ans4.setStyleSheet('font-size: 15px')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)

lb_question = QLabel('Запитання')
lb_question.setStyleSheet('font-size: 15px, color: #263238')
lb_rest = QLabel('хвилин')
lb_result = QLabel('Правильно')
lb_right_answer = QLabel('відповідь')

sp_rest = QSpinBox()
sp_rest.setStyleSheet('font-size: 20px')

gb_question = QGroupBox('Варіанти відповідей')
gb_question.setStyleSheet('font-size: 15px, color: #263238')


rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h1 = QHBoxLayout()

rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)

rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)

gb_question.setLayout(rb_h1)

gb_answer = QGroupBox()
gb_answer.setStyleSheet('backround-color:#e4dddb')

v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
gb_answer.setLayout(v1)

h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QVBoxLayout()

h1_main.addWidget(btn_menu)
h1_main.addStretch(1)
h1_main.addWidget(btn_rest)
h1_main.addWidget(sp_rest)
h1_main.addWidget(lb_rest)

h2_main.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
h3_main.addWidget(gb_answer)
h3_main.addWidget(gb_question)
gb_answer.hide()

h4_main.addStretch(1)
h4_main.addWidget(btn_next, stretch=2)
h4_main.addStretch(1)

v1_main.addLayout(h1_main, stretch=1)
v1_main.addLayout(h2_main, stretch=2)
v1_main.addLayout(h3_main, stretch=8)
v1_main.addLayout(h4_main)
v1_main.setSpacing(5)
window.setLayout(v1_main)
window.resize(550, 450)
# window.setStyleSheet('color: #2c3e50; backround-color:#e4dddb')

# color: #3b5999 


