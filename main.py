from random import choice, shuffle
from PyQt5.QtWidgets import QApplication
from time import sleep
app = QApplication([])
from main_window import *
from menu_window import*

# app.setStyleSheet('backround-color:#e4dddb')

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Що з цього не має крил?', 'Мураха', 'Летюча миша', 'Метелик', 'Оса')
q2 = Question('Який колір не існує в природному спектрі?', 'зеленувато-білий', 'синій', 'червоно-фіолетовий', 'жовтий')
q3 = Question('Що важче: літр води чи літр олії?', 'однакові', 'вода', 'олія', 'не знаю')
q4 = Question('Який з цих предметів не має прямого відношення до часу?', 'пісок', 'годинник', 'календар', 'місяць')
q5 = Question('У якій країні не ростуть кактуси в природі?', 'Японія', 'США', 'Австралія', 'Єгипет')
q6 = Question('Яка тварина може змінювати колір шкіри?', 'хамелион', 'крокодил', 'саламандра', 'лосось')
q7 = Question('Який із цих елементів не є металом?', 'оксиген', 'мідь', 'залізо', 'золото')
q8 = Question('Як називається найшвидший морський ссавець?', 'кіт', 'морж', 'дельфін', 'тюлень')
q9 = Question('Що з цього не існує в космосі?', 'Літаючі тарілки', 'чорні діри', 'метеорити', 'Зоряні системи')
q10 = Question('Який з цих смаків не має прямого фізичного пояснення?', 'умамі', 'солоний', 'гіркий', 'солодкий')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
# random_question = choice(questions)

# asked_questions = []

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)
    

new_question()

def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                cur_q.got_right()
                lb_result.setText('Вірно!')
                answer.setChecked(False)
                break
    else:
        lb_result.setText('Не вірно!')
        cur_q.got_wrong()

    RadioGroup.setExclusive(True)

def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()
        # radio_button.clear()

        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

        btn_next.setText('Відповісти')

btn_next.clicked.connect(click_ok)

def rest():
    window.hide()
    sp_rest_min = int(sp_rest.value())*60
    sleep(sp_rest_min)
    window.show()
    
btn_rest.clicked.connect(rest)

def menu_generation():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right/cur_q.count_ask)*100
    text =  f'Разів відповіли: {cur_q.count_ask}\n'\
            f'Вірних відповідей: {cur_q.count_right}\n'\
            f'Успішність: {round(c, 2)}%'

    lb_statistic.setText(text)
    menu_win.show()
    window.hide()

btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans2.clear()
    le_wrong_ans1.clear()
    le_wrong_ans3.clear()

btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(), 
                     le_wrong_ans1.text(), le_wrong_ans2.text(), 
                     le_wrong_ans3.text())
    questions.append(new_q)
    clear()



window.show()
app.exec_()