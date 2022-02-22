from enum import Enum
from question_generator.french_dictionnary_scrapper import get_word_gender


class QuestionType(Enum):
    PERSON = 1


gender_memory = {}


def build_question(subject, predicate, object_range, language) -> str:
    persons_range = ["http://dbpedia.org/ontology/Agent", "http://dbpedia.org/ontology/Person",
                     "http://dbpedia.org/ontology/Actor", "http://dbpedia.org/ontology/Painter",
                     "http://dbpedia.org/ontology/Athlete", "http://dbpedia.org/ontology/Commander"]
    if language == 'English':
        if object_range in persons_range:
            return f"Who is {predicate} in {subject}?"
        else:
            return f"What is the {predicate} of {subject}?"
    elif language == 'French':

        if object_range in persons_range:
            return f"Qui est {predicate} dans {subject}?"
        else:
            determinant_pred = determinant_handler_predicate_french(predicate)
            determinant_subj = determinant_handler_subject_french(subject)

            return f'Quel est {determinant_pred} {predicate} {determinant_subj} {subject}?'


def determinant_handler_predicate_french(predicate):
    vowels = "aeiou"

    if predicate[0] in vowels:
        return "l'"

    if predicate not in gender_memory:
        gender_memory[predicate] = get_word_gender(predicate.lower())

    if gender_memory[predicate] == "F":
        return "la"

    return "le"


def determinant_handler_subject_french(subject):
    vowels = "aeiou"
    if subject[0].lower() in vowels:
        return "d'"

    first_word = subject.split(" ")[0].lower()

    if first_word[-1] == "s":
        return "des"

    if first_word not in gender_memory:
        gender_memory[first_word] = get_word_gender(first_word)

    if gender_memory[first_word] == "F":
        return "de la"

    return "du"
