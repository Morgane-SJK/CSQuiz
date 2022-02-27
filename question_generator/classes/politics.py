from question_generator.classes.theme import Theme


class Politics(Theme):
    def __init__(self):
        super().__init__()
        self.properties = [
            "dbo:party",
            "dbo:europeanParliamentGroup",
            "dbo:politicalPartyInLegislature",
            "dbo:politicalPartyOfLeader",
        ]
        self.wiki_page_length = 10000
