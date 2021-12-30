from enum import Enum


class QuestionType(Enum):
    PERSON = 1


def build_question(subject, predicate) -> str:
    return f"Who is {predicate} in {subject}?"
