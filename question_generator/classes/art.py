from question_generator.classes.theme import Theme


class Art(Theme):
    def __init__(self):
        super().__init__()
        self.properties = [
            {"predicate":"dbo:notableWork", "wiki_page_length":200000},
            "dbo:field",
            "dbo:movement",
            "dbo:training",
            "dbp:movement",
            "dbo:author",
            "dbo:museum"
        ]
        self.wiki_page_length = 100000
