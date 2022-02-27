from question_generator.classes.theme import Theme


class Geography(Theme):
    def __init__(self):
        super().__init__()
        self.properties = [
            "dbo:capital", "dbo:currency", "dbo:humanDevelopmentIndex"
        ],
        self.wiki_page_length = 400000
