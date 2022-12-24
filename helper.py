import random
import numpy as np


class Helper:
    def __init__(self):
        self.question_id = 1000
        self.db = {}

        with open("db_ru_en.txt", encoding='utf-8') as f:
            data = f.readlines()

        self.dictionary = {}
        for line in data:
            ru, en = line.split("-")
            self.dictionary[en.strip()] = ru.strip()

    #   =================== GENERATE ======================

    def generate_question_word(self):
        rus = list(self.dictionary.values())
        en_word = random.choice(list(self.dictionary.keys()))
        ru_word = self.dictionary[en_word]
        rus.remove(ru_word)
        var = [ru_word] + random.sample(rus, 3)
        np.random.shuffle(var)

        question_id = self.get_question_id()
        self.db[question_id] = ru_word

        return {"question_id": question_id, "variance": var, "english": en_word}


    def generate_question_letter(self):
        en_word = list(random.choice(list(self.dictionary.keys())))
        letter_ind = random.randint(0, len(en_word) - 1)
        question_id = self.get_question_id()
        self.db[question_id] = en_word[letter_ind]
        en_word[letter_ind] = '*'
        en_word = ''.join(en_word)

        return {"question_id": question_id, "skip_letter": en_word}


    #   =================== CHECK ======================

    def check_answer(self, question_id, answer):
        if question_id in self.db:
            correct_answer = self.db[question_id]
            return {"is_correct": correct_answer == answer}
        else:
            return {"is_correct": False, "error": "entered question_id not existing"}

    #   =================== READ ======================

    def get_correct_result(self, question_id):
        if question_id in self.db:
            correct_answer = self.db[question_id]
            return {"correct_answer": correct_answer}
        else:
            return {"error": "entered question_id not existing"}



    def get_question_id(self):
        self.question_id += 1
        return self.question_id