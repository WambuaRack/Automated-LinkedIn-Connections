from flask import Flask, render_template, request, redirect, url_for
from linkedin_automation import run_linkedin_automation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    try:
        email = request.form['email']
        password = request.form['password']
        run_linkedin_automation(email, password)
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
