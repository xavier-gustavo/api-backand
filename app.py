from flask import Flask, request
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': "Gustavo",
        "description": "Filho"
    },
    {
        "id": 2,
        "name": "Leandro",
        "description": "Pai"
    },
    {
        "id": 3,
        "name": "Priscila",
        "description": "Mãe"
    }
]

tasksJSON = json.dumps(tasks)

@app.route(('/teste/cadastro'),methods=['GET'])
def home():

    request_data = request.get_json()
    tasksData = json.loads(tasksJSON)
    tasksData.append(request_data['task'])
    return json.dumps(tasksData)

if __name__ == "__main__":
    app.run()