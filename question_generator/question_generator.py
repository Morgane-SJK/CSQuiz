import random
import pandas as pd
from question_generator.db_queries import get_question_data
from question_generator.question_templates import build_question
from question_generator.films import Films


class QuestionGenerator():
    def __init__(self):
        self.themes = [Films()]

    def new_question(self):
        theme = random.choice(self.themes)
        data = get_question_data(random.choice(theme.properties))
        subject = list(map(lambda entry: entry["label_subject"]["value"], data))
        object = list(map(lambda entry: entry["label_object"]["value"], data))
        predicate = list(map(lambda entry: entry["label_predicate"]["value"], data))
        data_df = pd.DataFrame(list(zip(subject, object)), columns=["subject", "object"])
        right_answer = data_df.sample(1)
        wrong_answers = data_df[data_df["object"] != right_answer["object"].item()].sample(3)

        return [{"question": build_question(right_answer["subject"].item(), predicate[0]),
                 "right_answer": right_answer["object"].item(),
                 "wrong_answers": list(wrong_answers["object"])}]
