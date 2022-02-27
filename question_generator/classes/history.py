from question_generator.classes.theme import Theme


class History(Theme):
    def __init__(self):
        super().__init__()
        self.properties = [
            {"predicate": "dbo:date", "wiki_page_length": 150000},
            "dbo:commander",
            "dbo:after",
            "dbo:as",
            {"predicate": "dbo:activeYearsStartYear", "wiki_page_length": 150000},
            "dbo:influenced"
            "dbo:notableCommander",
        ]
        self.wiki_page_length = 20000
