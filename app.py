from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/get_success', methods=['GET'])
def get_success():
    # Get first name and last name from query parameters
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    # Check if both first name and last name are provided
    if first_name and last_name:
        # Success response
        response = {
            'status': 'success',
            'message': f'Hello, {first_name} {last_name}! Success!'
        }
        return jsonify(response), 200, {'Content-Type': 'application/json'}
    else:
        # Error response if either first name or last name is missing
        response = {
            'status': 'error',
            'message': 'Both first name and last name are required.'
        }
        return jsonify(response), 400, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)
