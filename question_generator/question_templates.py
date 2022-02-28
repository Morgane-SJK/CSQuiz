from enum import Enum
from question_generator.french_dictionnary_scrapper import get_word_gender


class QuestionType(Enum):
    PERSON = 1


gender_memory = {}


def build_question(subject, predicate, object_range, language, subject_range, theme) -> str:
    persons_range = ["http://dbpedia.org/ontology/Agent", "http://dbpedia.org/ontology/Person", 
                     "http://dbpedia.org/ontology/Painter", "http://dbpedia.org/ontology/Athlete", 
                     "http://dbpedia.org/ontology/Commander"]

    vowels = "aeiou"

    #change verb if History
    verb_fr = "est"
    verb_en = "is"
    if (theme == "History"):
        verb_fr = "était"
        verb_en = "was"

    if language == 'French':
        l_app = "l'"
        d_app = "d'"
        if object_range in persons_range:
            return f"Qui {verb_fr} {l_app if predicate[0] in vowels else 'le '}{predicate}  {d_app if subject[0] in vowels else 'de '}{subject}?"
        elif (object_range == "http://dbpedia.org/ontology/Actor"):
            return f"Qui {verb_fr} {predicate} dans {subject}?"
        else:
            determinant_pred = determinant_handler_predicate_french(predicate)
            determinant_subj = determinant_handler_subject_french(subject, subject_range)
            pronoun = pronoun_handler_french(predicate)

            return f'{pronoun} est {determinant_pred} {predicate} {determinant_subj}{subject}?'

    if object_range in persons_range:
        return f"Who {verb_en} the {predicate} of {subject}?"
    elif (object_range == "http://dbpedia.org/ontology/Actor"):
            return f"Who {verb_en} {predicate} in {subject}?"
    else:
        return f"What is the {predicate.replace('active years','')} of {subject}?"

def pronoun_handler_french(predicate):
    if predicate not in gender_memory:
        gender_memory[predicate] = get_word_gender(predicate.lower())

    if gender_memory[predicate] == "F":
        return "Quelle"
    return "Quel"

def determinant_handler_predicate_french(predicate):
    vowels = "aeiou"

    if predicate[0] in vowels:
        return "l'"

    if predicate not in gender_memory:
        gender_memory[predicate] = get_word_gender(predicate.lower())

    if gender_memory[predicate] == "F":
        return "la"

    return "le"


def determinant_handler_subject_french(subject, subject_range):
    vowels = "aeiou"
    if subject[0].lower() in vowels:
        return "d'"

    first_word = subject.split(" ")[0].lower()

    if first_word[-1] == "s":
        return "des "

    print(subject_range)
    if subject_range in ["http://dbpedia.org/ontology/Work"]:
        return "de "

    if first_word not in gender_memory:
        gender_memory[first_word] = get_word_gender(first_word)

    if gender_memory[first_word] == "F":
        return "de la "

    return "du "
