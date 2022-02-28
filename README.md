# CSQuiz

#### Due date

:calendar: **28/02/2022**

#### <span style="color: #fc264d;"> Our project is deployed on [heroku](https://the-cs-quiz.herokuapp.com/) </span>

## Students

- [Alexandre Forestier](https://github.com/alexfrst)
- [Morgane Senejko](https://github.com/Morgane-SJK)
- [Magali Morin](https://github.com/magalimorin18)

## :books: Subject of the project

The aim of the project is to create a general knowledge quiz with specific themes. The data needed for
the quiz is extracted from DBpedia thanks to Sparql queries.


**To solve this problem we implemented:**

1. A Web-Server in charge of the data gathering and the question generation
2. A web-page displaying the questions

## :runner: Running the code

```bash
python quizz.py
```

### Requirements

```bash
make install
```

## :package: Structure of the project

```bash
├── question_generator
│   ├── classes
│        ├── __init__.py
│        ├── art.py
│        ├── films.py
│        ├── geography.py
│        ├── history.py
│        ├── politics.py
│        ├── theme.py
│   ├── __init__.py
│   ├── db_queries.py
│   ├── french_dictionnary_scrapper.py
│   ├── question_generator.py
│   └── question_templates.py
├── static
│   ├── css
│        ├── header.css
│        ├── index.css
│   ├── img
│   └── js
│        ├── quiz.js
├── template
│   ├── index.html
│   ├── index_french.html
│   ├── rules.html
│   └── rules_french.html
├── Makefile
├── Procfile
├── quizz.py
├── README.md
├──requirements.txt
└──wsgi.py
```
