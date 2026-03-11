from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Pipeline is running successfully!"
if __name__ == "__main__":
    app.run()

from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200