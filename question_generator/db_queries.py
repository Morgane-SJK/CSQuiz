import requests
import json

db_url = "http://dbpedia.org/sparql"


def _query(q):
    try:
        params = {'query': q}
        resp = requests.get(db_url, params=params, headers={'Accept': 'application/json'})
        return resp.text
    except Exception as e:
        print(e)
        raise


def _query_resource(predicate):
    query_string = f"""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label_subject ?object ?label_object ?label_predicate
    WHERE {{
        ?subject {predicate} ?object .
        ?subject dbo:wikiPageLength ?wikipagelength.
        ?subject rdfs:label ?label_subject.
        ?object rdfs:label ?label_object.
        {predicate} rdfs:label ?label_predicate.
        
        FILTER langMatches( lang(?label_subject), "EN" )
        FILTER langMatches( lang(?label_object), "EN" )
        FILTER langMatches( lang(?label_predicate), "EN" )
        FILTER (?wikipagelength> 124488)
    }}
    ORDER BY ?wikipagelength
    LIMIT 200
    """
    return json.loads(_query(query_string))


def get_question_data(predicate):
    query_response = _query_resource(predicate)
    return query_response["results"]["bindings"]
