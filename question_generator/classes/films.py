from question_generator.classes.theme import Theme


class Films(Theme):
    def __init__(self):
        super().__init__()
        self.properties = [
            "dbo:director", "dbo:producer", "dbo:starring", "dbo:budget", "dbo:gross"
        ]
        self.page_length_multiplier = {"French": 0.5}
        self.wiki_page_length = 200000
