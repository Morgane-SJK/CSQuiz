import pandas as pd
import numpy as np
import random
import re
from question_generator.db_queries import get_question_data
from question_generator.question_templates import build_question
from question_generator.classes.films import Films
from question_generator.classes.art import Art
from question_generator.classes.geography import Geography
from question_generator.classes.history import History
from question_generator.classes.politics import Politics


class QuestionGenerator():
    def __init__(self):
        self.themes = {'Cinema' : Films(), 'Art' : Art(), 'Geography' : Geography(), 
        'History' : History(), 'Politics' : Politics()}

    def new_question(self, theme, language):
        theme = self.themes[theme]
        predicate = random.choice(theme.properties)
        question_data = get_question_data(predicate, language)

        subjects = list(map(lambda entry: entry["label_subject"]["value"], question_data))
        objects = list(map(lambda entry: entry["label_object"]["value"] if "label_object" in entry else entry["object"]["value"], question_data))
        object_range = list(map(lambda entry: entry["range"]["value"], question_data))
        predicate_label = list(map(lambda entry: entry["label_predicate"]["value"], question_data))[0]

        data_df = pd.DataFrame(list(zip(subjects, objects,object_range)), columns=["subject", "object","object_range"])

        right_answer = data_df.sample(1)
        right_answer_subject = right_answer["subject"].item()
        right_answer_object = right_answer["object"].item()
        right_answer_range = right_answer["object_range"].item()

        same_object_removal_mask = data_df["object"] != right_answer_object
        same_subject_removal_mask = data_df["subject"] != right_answer_subject

        wrong_answer_list = data_df[same_object_removal_mask & same_subject_removal_mask]["object"]
        chosen_wrong_answers = np.random.choice(wrong_answer_list, 3, replace=False)

        return [{"question": build_question(right_answer_subject, predicate_label, right_answer_range, language),
                 "right_answer": re.sub("\(.*\)", "", right_answer_object),
                 "wrong_answers": [re.sub("\(.*\)", "", answer) for answer in chosen_wrong_answers]}]
