# when the user submits the form in the HTML page, an AJAX request is sent to the /api/ask endpoint on the Python server.
# The server processes the question and sends back a response, which is then displayed on the HTML page.

from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the query submission
@app.route('/submit-query', methods=['POST'])
def submit_query():
    user_query = request.form['user-query']
    
    # Process the user's query and generate a response
    # Replace this with your own logic to generate the response
    # For demonstration purposes, let's just echo back the user's question
    response = "You asked: " + user_query
    
    # Return both the user's question and the response
    return jsonify({'user_query': user_query, 'response': response})

if __name__ == '__main__':
    app.run(debug=True)
