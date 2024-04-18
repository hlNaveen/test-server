from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Server</h1>"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        data = request.json  # Assuming JSON data is sent with POST
        return jsonify({
            "message": "Hello, {}!".format(data.get('name', 'Guest')),
            "yourData": data
        })
    else:
        name = request.args.get('name', 'Guest')
        return "<h1>Hello, {}!</h1>".format(name)

if __name__ == "__main__":
    app.run(debug=True)
