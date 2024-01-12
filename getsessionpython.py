from flask import Flask, request, jsonify
from pyngrok import ngrok

app = Flask(__name__)

@app.route('/api/get-success', methods=['GET'])
def get_success():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    if first_name and last_name:
        success_message = f"Hello, {first_name} {last_name}! Success!"
        return jsonify({"status": "success", "message": success_message})
    else:
        return jsonify({"status": "error", "message": "Please provide both first_name and last_name parameters."})

if __name__ == '__main__':
    # Start Ngrok when the app is run
    public_url = ngrok.connect(5000)
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:5000\"".format(public_url))

    # Start the Flask app
    app.run(port=5000)
