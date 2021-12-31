from enum import Enum


class QuestionType(Enum):
    PERSON = 1


def build_question(subject, predicate, object_range) -> str:
    persons_range = ["http://dbpedia.org/ontology/Agent", "http://dbpedia.org/ontology/Person",
                     "http://dbpedia.org/ontology/Actor"]
    if object_range in persons_range:
        return f"Who is {predicate} in {subject}?"
    else:
        return f"What is the {predicate} of {subject}?"
