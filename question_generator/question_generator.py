import pandas as pd
import numpy as np
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
        self.themes = {'Cinema': Films(), 'Art': Art(), 'Geography': Geography(),
                       'History': History(), 'Politics': Politics()}
        self.question_memory = []

    def new_question(self, theme_name, language, depth=0):
        if depth == 10:
            return [{"question": "Désolé nous manquons de données pour générer une question avec la langue et le theme demandé <br> Sachez que:",
                     "right_answer": "Vous pouvez changez de thème dans le menu.",
                     "wrong_answers": ["Vous pouvez changer de langue dans le menu.",
                                       "L'anglais dispose de plus de thèmes.",
                                       "L'anglais dispose de plus de type de questions."]}]

        theme = self.themes[theme_name]
        predicate, wikipage_length = theme.get_predicate_and_page_length(language)
        question_data = get_question_data(predicate, language, wikipage_length)
        print(predicate)

        if len(question_data) == 0:
            return self.new_question(theme_name, language, depth + 1)

        subjects = list(map(lambda entry: entry["label_subject"]["value"], question_data))
        objects = list(
            map(lambda entry: entry["label_object"]["value"] if "label_object" in entry else entry["object"]["value"],
                question_data))
        object_range = list(map(lambda entry: entry["range"]["value"], question_data))
        predicate_label = list(map(lambda entry: entry["label_predicate"]["value"], question_data))[0]

        data_df = pd.DataFrame(list(zip(subjects, objects, object_range)),
                               columns=["subject", "object", "object_range"])
        data_df.object = data_df.object.map(lambda x: text_treatment(x))
        data_df.subject = data_df.subject.map(lambda x: text_treatment(x)).map(lambda x: re.sub("\\d\\d\\d\\d", "", x))

        right_answer = data_df.sample(1)
        right_answer_subject = right_answer["subject"].item()
        right_answer_object = right_answer["object"].item()
        right_answer_range = right_answer["object_range"].item()

        same_object_removal_mask = data_df["object"] != right_answer_object
        same_subject_removal_mask = data_df["subject"] != right_answer_subject

        wrong_answer_list = data_df[same_object_removal_mask & same_subject_removal_mask]["object"].unique()

        if len(wrong_answer_list) < 3:
            return self.new_question(theme_name, language, depth + 1)

        chosen_wrong_answers = [item for item in
                                np.random.choice(wrong_answer_list, 3, replace=False)]

        question_text = build_question(right_answer_subject, predicate_label, right_answer_range, language,
                                            right_answer_range, theme_name),
        if question_text in self.question_memory:
            return self.new_question(theme_name, language, depth)

        self.question_memory.append(question_text)

        return [{"question": question_text,
                 "right_answer": right_answer_object,
                 "wrong_answers": chosen_wrong_answers}]


def text_treatment(string):
    if re.match("\\w\\.\\w+E\\w+", string):
        return f"{float(string):_.0f}".replace('_', ' ')
    string_without_attributes = re.sub("\(.*\)", "", string)
    return string_without_attributes.split("/")[-1].replace("_", " ")
