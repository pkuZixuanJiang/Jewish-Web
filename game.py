import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QButtonGroup, QMessageBox

class QuizGame(QWidget):
    def __init__(self):
        super().__init__()

        # 游戏数据，选择题格式
        all_questions = [
            ("全球犹太人口中，哪一国家的犹太人口最多？", ["美国", "以色列", "法国", "加拿大"], "以色列"),
            ("美国的犹太人口大约为多少人？", ["600万", "300万", "1000万", "1200万"], "600万"),
            ("截至2024年，哪国的犹太人口位列全球第三？", ["法国", "德国", "俄罗斯", "阿根廷"], "法国"),
            ("截至2024年，全球犹太人口大约是多少？", ["1500万至2000万", "1000万至1500万", "2000万至2500万", "2500万至3000万"], "1500万至2000万"),
            ("犹太人口最多的国家是哪里？", ["美国", "以色列", "法国", "加拿大"], "以色列"),
            ("法国的犹太人口约为多少？", ["20万", "55万", "40万", "75万"], "55万"),
            ("截至2024年，加拿大的犹太人口约为多少？", ["19万", "29万", "39万", "49万"], "39万"),
            ("英国的犹太人口约为多少？", ["19万", "29万", "39万", "49万"], "29万"),
            ("阿根廷的犹太人口约为多少？", ["6万", "12万", "18万", "24万"], "18万"),
            ("俄罗斯的犹太人口约为多少？", ["5万", "10万", "15万", "20万"], "15万"),
            ("德国的犹太人口约为多少？", ["6万", "12万", "18万", "24万"], "12万"),
            ("以下哪个国家的犹太人口最少？", ["澳大利亚", "巴西", "俄罗斯", "德国"], "巴西"),
            ("下列哪位犹太人是量子电动力学的奠基人之一？", ["阿尔伯特·爱因斯坦", "约翰·冯·诺伊曼", "理查德·费曼", "巴鲁赫·斯宾诺莎"], "理查德·费曼"),
            ("谁是现代计算机体系结构的奠基人之一？", ["理查德·费曼", "约翰·冯·诺伊曼", "卡尔·马克思", "斯蒂文·斯皮尔伯格"], "约翰·冯·诺伊曼"),
            ("以下哪位犹太人是诺贝尔文学奖得主并且是一位著名音乐家？", ["娜塔莉·波特曼", "理查德·费曼", "鲍勃·迪伦", "梅耶·罗斯柴尔德"], "鲍勃·迪伦"),
            ("以下哪位犹太人曾在英国担任首位犹太裔首相？", ["阿尔伯特·爱因斯坦", "本杰明·迪斯雷利", "卡尔·马克思", "戴维·本·古里安"], "本杰明·迪斯雷利"),
            ("以下哪位科学家是相对论的创始人之一？",["阿尔伯特·爱因斯坦", "理查德·费曼", "约翰·冯·诺伊曼", "卡尔·马克思"], "阿尔伯特·爱因斯坦"),
            ("理查德·费曼是哪个领域的奠基人？", ["相对论", "量子电动力学", "现代哲学", "计算机体系结构"], "量子电动力学"),
            ("以下哪位是存在主义与荒诞文学的代表？", ["弗兰茨·卡夫卡", "巴鲁赫·斯宾诺莎", "卡尔·马克思", "鲍勃·迪伦"], "弗兰茨·卡夫卡"),
            ("以下哪位是现代哲学的奠基者之一？", ["卡尔·马克思", "巴鲁赫·斯宾诺莎", "戴维·本·古里安", "理查德·费曼"], "巴鲁赫·斯宾诺莎"),
            ("斯蒂文·斯皮尔伯格以哪个领域闻名？", ["文学", "哲学", "导演", "政治"], "导演"),
            ("以下哪位是罗斯柴尔德银行的创始人？", ["梅耶·罗斯柴尔德", "马克·扎克伯格", "谢尔盖·布林", "本杰明·迪斯雷利"], "梅耶·罗斯柴尔德"),
            ("以下哪位是谷歌的创始人之一？", ["马克·扎克伯格", "谢尔盖·布林", "露丝·巴德·金斯伯格", "斯蒂文·斯皮尔伯格"], "谢尔盖·布林"),
            ("戴维·本·古里安是哪个国家的建国总理？", ["美国", "英国", "以色列", "法国"], "以色列"),
            ("露丝·巴德·金斯伯格因推动什么领域而闻名？", ["经济发展", "性别平等", "文学成就", "娱乐事业"], "性别平等"),
            ("2010年，CNN解雇主持人Rick Sanchez的原因是什么？", ["因个人原因", "因其发表反犹言论", "因违背新闻伦理", "因财务问题"], "因其发表反犹言论"),
            ("2017年夏洛茨维尔事件中，哪些群体因反犹言论提起了诉讼？", ["黑人权益组织", "无组织提起诉讼", "犹太社区与律师团体", "妇女团体"], "犹太社区与律师团体"),
            ("2018年匹兹堡犹太教堂枪击案发生后，犹太社区采取了哪些行动？", ["全球募捐，支持受害者家庭", "向媒体发表声明", "加强宗教场所的安全", "申请政府赔偿"], "全球募捐，支持受害者家庭"),
            ("哪些国家的犹太人口位居全球前五？", ["以色列、美国、法国、加拿大、英国", "以色列、美国、法国、阿根廷、德国", "以色列、美国、德国、澳大利亚、巴西", "以色列、美国、俄罗斯、巴西、阿根廷"], "以色列、美国、法国、加拿大、英国"),
            ("2023年，德国的反犹事件呈现什么趋势？", ["无变化", "无法统计", "事件增多", "事件减少"], "事件增多"),
            ("在中国，关于犹太人的主流观念是什么？", ["犹太人控制世界", "犹太人文化保守", "犹太人经济影响力弱", "犹太人历史悠久"], "犹太人控制世界"),
            ("在2023年10月，加沙冲突爆发后的前四天，英国的反犹事件增长了多少？", ["100%", "200%", "300%", "400%"], "300%"),
            ("2023年10月7日至27日期间，德国记录了多少起反犹事件？", ["1,000起", "1,300起", "1,800起", "2,500起"], "1,800起"),
            ("2023年10月29日，哪一地区的抗议者冲进机场扬言驱逐犹太难民？", ["英国", "南非", "俄罗斯（达吉斯坦共和国）", "德国"], "俄罗斯（达吉斯坦共和国）"),
            ("2023年10月28日，南非的亲巴勒斯坦抗议者在何地撕下以色列人质照片？", ["大学校园", "机场", "犹太社区", "政府大楼"], "犹太社区"),
            ("2024年4月，美国大学校园中因支持巴勒斯坦的抗议引发了什么情绪的上升？", ["反犹情绪", "亲犹情绪", "反巴勒斯坦情绪", "种族平等情绪"], "反犹情绪"),
            ("2024年11月，德国出台新决议试图遏制反犹太主义，但引发了什么担忧？", ["移民问题", "言论自由", "经济危机", "犯罪率上升"], "言论自由"),
            ("截至2023年，美国反犹骚扰事件的增长率是多少？", ["95%", "45%", "65%", "125%"], "95%"),
            ("2023年，德国记录的总反犹罪行数量是多少？", ["5,164起", "7,523起", "1,676起", "3,256起"], "5,164起"),
            ("2023年，法国反犹人身攻击事件增长率为多少？", ["65%", "98%", "133%", "24%"], "98%"),
            ("联合国报告指出，全球反犹事件的总体趋势是什么？", ["下降趋势", "无变化", "上升趋势", "波动趋势"], "上升趋势"),
            ("德国柏林的犹太历史博物馆是为了应对什么问题而开展教育项目？", ["反移民", "反犹主义", "宗教教育", "犹太人历史保护"], "反犹主义"),
            ("以色列制作的电视剧《Fauda》主要展示了哪种文化？", ["犹太文化", "阿拉伯文化", "欧洲文化", "美国文化"], "犹太文化"),
            ("反犹主义事件中，哪些背景的犯罪者在德国尤为突出？", ["非洲背景", "本地德国人", "东欧背景", "伊斯兰背景"], "伊斯兰背景"),
            ("犹太人如何应对2017年夏洛茨维尔的反犹言论？", ["公开声明谴责", "提起民事诉讼", "邀请专家进行辩论", "加强宗教场所安保"], "提起民事诉讼"),
            ("2010年，CNN解雇Rick Sanchez的原因是什么？", ["工作能力不足", "发表反犹主义言论", "收视率下降", "与同事争吵"], "发表反犹主义言论"),
            ("在Rick Sanchez事件中，哪一组织迅速发表声明谴责其言论？", ["联合国", "反诽谤联盟（ADL）", "美国犹太联合会", "犹太历史博物馆"], "反诽谤联盟（ADL）"),
            ("2017年，夏洛茨维尔白人至上主义游行的结果是什么？", ["示威者被捕", "组织者赔偿超过2500万美元", "游行被和平结束", "法院驳回诉讼"], "组织者赔偿超过2500万美元"),
            ("2019年，德国柏林针对犹太人的袭击事件后，犹太组织采取了什么措施？", ["提起诉讼", "举办公开论坛和教育活动", "抗议游行", "申请赔偿"], "举办公开论坛和教育活动"),
            ("2018年，匹兹堡犹太教堂枪击案中，共有多少人遇害？", ["3人", "11人", "6人", "25人"], "11人"),
            ("在匹兹堡枪击案后，犹太社区采取了什么举措？", ["举办国际抗议活动", "跨信仰合作提供心理支持和募捐", "提起民事诉讼", "加强安保措施"], "跨信仰合作提供心理支持和募捐"),
            ("以色列制作的哪些电视剧帮助传播了犹太文化？", ["《Fauda》和《Shtisel》", "《权力的游戏》和《绝命毒师》", "《黑镜》和《纸牌屋》", "《王冠》和《大西洋帝国》"], "《Fauda》和《Shtisel》"),
            ("以色列电视剧的传播主要起到了什么作用？", ["增强文化认同感", "消除对犹太文化的误解", "推动经济发展", "加强宗教信仰"], "消除对犹太文化的误解"),
            ("哪一年发生了匹兹堡犹太教堂枪击案？",["2017年", "2018年", "2019年", "2020年"], "2018年"),
            ("德国柏林在针对犹太人袭击事件后，哪一机构与教育部门合作开展活动？", ["犹太历史博物馆", "联合国", "反诽谤联盟（ADL）", "美国犹太联合会"], "犹太历史博物馆"),
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
