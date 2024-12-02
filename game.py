import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QButtonGroup, QMessageBox

class QuizGame(QWidget):
    def __init__(self):
        super().__init__()

        # 游戏数据，选择题格式
        all_questions = [
            ("截至2024年，全球犹太人口大约是多少？", ["1500万", "2000万", "2500万", "3000万"], "1500万"),
            ("全球犹太人口中，哪一国家的犹太人口最多？", ["美国", "以色列", "法国", "加拿大"], "以色列"),
            ("美国的犹太人口大约为多少人？", ["600万", "500万", "1000万", "1200万"], "600万"),
            ("截至2024年，哪国的犹太人口位列全球第三？", ["法国", "德国", "俄罗斯", "阿根廷"], "法国"),
            ("下列哪位犹太人是量子电动力学的奠基人之一？", ["阿尔伯特·爱因斯坦", "约翰·冯·诺伊曼", "理查德·费曼", "巴鲁赫·斯宾诺莎"], "理查德·费曼"),
            ("谁是现代计算机体系结构的奠基人之一？", ["理查德·费曼", "约翰·冯·诺伊曼", "卡尔·马克思", "斯蒂文·斯皮尔伯格"], "约翰·冯·诺伊曼"),
            ("以下哪位犹太人是诺贝尔文学奖得主并且是一位著名音乐家？", ["娜塔莉·波特曼", "理查德·费曼", "鲍勃·迪伦", "梅耶·罗斯柴尔德"], "鲍勃·迪伦"),
            ("以下哪位犹太人曾在英国担任首位犹太裔首相？", ["阿尔伯特·爱因斯坦", "本杰明·迪斯雷利", "卡尔·马克思", "戴维·本·古里安"], "本杰明·迪斯雷利"),
            ("2010年，CNN解雇主持人Rick Sanchez的原因是什么？", ["因个人原因", "因其发表反犹言论", "因违背新闻伦理", "因财务问题"], "因其发表反犹言论"),
            ("2017年夏洛茨维尔事件中，哪些群体因反犹言论提起了诉讼？", ["黑人权益组织", "无组织提起诉讼", "犹太社区与律师团体", "妇女团体"], "犹太社区与律师团体"),
            ("2018年匹兹堡犹太教堂枪击案发生后，犹太社区采取了哪些行动？", ["全球募捐，支持受害者家庭", "向媒体发表声明", "加强宗教场所的安全", "申请政府赔偿"], "全球募捐，支持受害者家庭"),
            ("哪些国家的犹太人口位居全球前五？", ["以色列、美国、法国、加拿大、英国", "以色列、美国、法国、阿根廷、德国", "以色列、美国、德国、澳大利亚、巴西", "以色列、美国、俄罗斯、巴西、阿根廷"], "以色列、美国、法国、加拿大、英国"),
            ("反犹主义事件在全球的总体趋势如何？", ["平稳", "下降", "呈上升趋势", "没有明显变化"], "呈上升趋势"),
            ("2023年，德国的反犹事件呈现什么趋势？", ["无变化", "无法统计", "事件增多", "事件减少"], "事件增多"),
            ("在中国，关于犹太人的主流观念是什么？", ["犹太人控制世界", "犹太人文化保守", "犹太人经济影响力弱", "犹太人历史悠久"], "犹太人控制世界"),
            ("德国柏林的犹太历史博物馆是为了应对什么问题而开展教育项目？", ["反移民", "反犹主义", "宗教教育", "犹太人历史保护"], "反犹主义"),
            ("以色列制作的电视剧《Fauda》主要展示了哪种文化？", ["犹太文化", "阿拉伯文化", "欧洲文化", "美国文化"], "犹太文化"),
            ("反犹主义事件中，哪些背景的犯罪者在德国尤为突出？", ["非洲背景", "本地德国人", "东欧背景", "伊斯兰背景"], "伊斯兰背景"),
            ("犹太人如何应对2017年夏洛茨维尔的反犹言论？", ["公开声明谴责", "提起民事诉讼", "邀请专家进行辩论", "加强宗教场所安保"], "提起民事诉讼"),
            ("2024年4月，美国大学校园中因加沙冲突引发了什么情况？", ["学生支持巴勒斯坦的抗议引发冲突", "校园活动正常进行，无影响", "各大学加强支持以色列的活动", "大学联合谴责反犹事件"], "学生支持巴勒斯坦的抗议引发冲突"),
            ("2024年11月，德国出台的新决议旨在遏制反犹太主义，但引发了什么担忧？", ["宗教自由的担忧", "政府干预教育的担忧", "言论自由的担忧", "犹太社区安全的担忧"], "言论自由的担忧")
        ]

        # 随机抽取 10 个问题并随机打乱问题顺序
        self.questions = random.sample(all_questions, 10)

        # 打乱每个问题的选项顺序
        for question in self.questions:
            random.shuffle(question[1])

        self.current_question = 0
        self.score = 0

        # 设置窗口
        self.setWindowTitle("Quiz Game")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f7f7f7;")

        # 创建控件
        self.question_label = QLabel(self.questions[self.current_question][0], self)
        self.question_label.setStyleSheet("font-size: 40px; font-weight: bold; color: #333;")

        self.button_group = QButtonGroup(self)
        self.radio_buttons = []

        # 创建选项
        for option in self.questions[self.current_question][1]:
            radio_button = QRadioButton(option, self)
            radio_button.setStyleSheet("font-size: 36px; color: #333;")
            self.button_group.addButton(radio_button)
            self.radio_buttons.append(radio_button)

        # 创建提交按钮
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 36px;
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.submit_button.clicked.connect(self.check_answer)

        # 创建分数标签
        self.score_label = QLabel(f"Score: {self.score}", self)
        self.score_label.setStyleSheet("font-size: 36px; color: #333;")

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.question_label)
        for radio_button in self.radio_buttons:
            layout.addWidget(radio_button)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.score_label)

        self.setLayout(layout)

    def check_answer(self):
        # 获取选中的答案
        selected_button = self.button_group.checkedButton()
        if selected_button:
            user_answer = selected_button.text().strip()
            question, options, correct_answer = self.questions[self.current_question]

            if user_answer == correct_answer:
                self.score += 1
                QMessageBox.information(self, "Correct", "回答正确!")
            else:
                QMessageBox.warning(self, "Wrong", f"回答错误! 正确答案是 {correct_answer}.")

            self.score_label.setText(f"得分: {self.score}")
            self.current_question += 1

            if self.current_question < len(self.questions):
                self.update_question()
            else:
                self.end_game()

        else:
            QMessageBox.warning(self, "No Selection", "Please select an answer!")

    def update_question(self):
        question, options, correct_answer = self.questions[self.current_question]
        self.question_label.setText(question)

        # 更新选项
        for i, radio_button in enumerate(self.radio_buttons):
            radio_button.setText(options[i])
            radio_button.setChecked(False)

    def end_game(self):
        QMessageBox.information(self, "Game Over", f"游戏结束！你的最终得分是 {self.score}/{len(self.questions)}.")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = QuizGame()
    game.show()
    sys.exit(app.exec_())
