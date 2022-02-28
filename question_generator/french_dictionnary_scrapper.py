import requests
from bs4 import BeautifulSoup


def get_word_gender(word):
    """
    Scraps the gender a french word.
    :param word: Word to be checked.
    :type word: str
    :return: Word gender M|F.
    :rtype: str
    """
    response = requests.get(f"https://www.larousse.fr/dictionnaires/francais/{word}")
    soup = BeautifulSoup(response.content, 'html.parser')  # the parser that suits to the html
    wanted_words = soup.find_all("a", string=word)

    if len(wanted_words) == 0:
        genders = soup.select("p.CatgramDefinition")
        if len(genders) > 0:
            if genders[0].text == "nom féminin":
                return "F"
        return "M"
    else:
        word_endpoint = wanted_words[0]["href"]
        response = requests.get(f"https://www.larousse.fr{word_endpoint}")
        soup = BeautifulSoup(response.content, 'html.parser')
        words = soup.select(
            'div.wrapper div.row div.col-md-8 div#definition article div.header-article p.CatgramDefinition')
        gender = words[0].text

        if gender == "nom féminin":
            return "F"
        else:
            return "M"


if __name__ == '__main__':
    print(get_word_gender("république"))
    print(get_word_gender("capitale"))
