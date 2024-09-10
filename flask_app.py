from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
    app.run(port=5000,debug=True)

@app.route('/')
def home():
    return "<p>Mijn Droom om door te groeien als Full-Stack Developer is dichterbij aan het komen!!</p>"