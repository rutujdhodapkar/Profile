from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    # Replace 'index.html' with the full path to your file if it's outside 'templates'
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
