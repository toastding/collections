import requests

parameters = {
        "amount": 10,
        "type": "boolean"
    }

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = [
    {
        "category": data['results'][0].get('category'),
        "type": "boolean",
        "difficulty": "medium",
        "question": data['results'][0].get('question'),
        "correct_answer": data['results'][0].get('correct_answer'),
        "incorrect_answers": [
            data['results'][0].get('incorrect_answer')
        ]
    }
]

