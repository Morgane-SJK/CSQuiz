import requests
import json

db_url = "http://dbpedia.org/sparql"


def _query(q):
    """
    Queries the dbpedia sparql endpoint.
    :param q: Query string.
    :type q: str
    :return: Query answer.
    :rtype: dict
    """
    try:
        params = {'query': q}
        resp = requests.get(db_url, params=params, headers={'Accept': 'application/json'})
        return resp.text
    except Exception as e:
        print(e)
        raise


def _query_resource(predicate, language, wiki_page_length):
    """
    Generates and sends a query to the dbpedia sparql endpoint.
    :param predicate: Predicate to query.
    :type predicate: str
    :param language: Queried language.
    :type language: str
    :param wiki_page_length: Page length of the wikipedia page used to have relevant results.
    :type wiki_page_length: int|float
    :return: Query answer
    :rtype: dict
    """
    language_code_mapping = {"English": "EN", "German": "DE", "French": "FR", "Spanish": "ES", "Italian": "IT",
                             "Portuguese": "PT", "Russian": "RU", "Chinese": "ZH"}
    langage_code = "en"
    if language in language_code_mapping:
        langage_code = language_code_mapping[language]
    query_string = f"""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label_subject ?object ?label_object ?label_predicate ?range
    WHERE {{
        ?subject {predicate} ?object .
        ?subject dbo:wikiPageLength ?wikipagelength.
        ?subject rdfs:label ?label_subject.
        OPTIONAL {{?object rdfs:label ?label_object.}}
        {predicate} rdfs:range ?range.
        {predicate} rdfs:label ?label_predicate.
        
        FILTER langMatches( lang(?label_subject), "{langage_code}" )
        FILTER  (langMatches( lang(?label_object), "{langage_code}" ) || !bound(?label_object))
        FILTER langMatches( lang(?label_predicate), "{langage_code}" )
        FILTER (?wikipagelength> {wiki_page_length})
    }}
    ORDER BY ?wikipagelength
    LIMIT 200
    """

    return json.loads(_query(query_string))


def get_resource_type(predicate):
    query_string = f"""
    SELECT ?range
    WHERE {{
        {predicate} rdfs:range ?range.
    }}
    """
    return json.loads(_query(query_string))["results"]["bindings"]


def get_question_data(predicate, language, theme):
    """
    Generates sends and removes not useful fields from a query to the dbpedia sparql endpoint.
    :param predicate: predicate to query.
    :type predicate: str
    :param language: queried language.
    :type language: str
    :param wiki_page_length: page length of the wikipedia page used to have relant results.
    :type wiki_page_length: int|float
    :return: query answer
    :rtype: dict
    """
    query_response = _query_resource(predicate, language, theme)
    return query_response["results"]["bindings"]
