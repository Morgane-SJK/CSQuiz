import random

class Theme():
    """
    Theme superclass.
    """
    def __init__(self):
        self.wiki_page_length = 200000
        self.properties = []
        self.page_length_multiplier = {"French": 0.5}

    def get_predicate_and_page_length(self, language):
        """
        Returns the predicate and the minimal required page length depending on priority rules.
        :param language: Language of the question.
        :type language: str
        :return: (predicate, page_length)
        :rtype: (str, int)
        """
        predicate = random.choice(self.properties)

        if isinstance(predicate, str):
            return predicate, self.wiki_page_length * self.page_length_multiplier.get(language, 1)

        if "wiki_page_length" in predicate:
            return predicate["predicate"], predicate["wiki_page_length"] * self.page_length_multiplier.get(language, 1)

        return predicate["predicate"], self.wiki_page_length * self.page_length_multiplier.get(language, 1)
