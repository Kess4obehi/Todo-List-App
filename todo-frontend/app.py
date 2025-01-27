from flask import Flask, render_template, url_for, request, flash, redirect, session
import requests

app = Flask(__name__)
app.secret_key = 'my_secrete_key'



API_URL = 'http://127.0.0.1:3000'

@app.route('/', methods=['GET', 'POST'])
def landing_page():
    return render_template('landing_page.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        #Get the information from the html templates
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash("Confirm Password does not match with the password")
            return redirect(url_for('signup'))
        
        # create a dictionary of the information
        form_data = {
            "username": username,
            "email": email,
            "password": password
        }

        response = requests.post(API_URL+'/signup', form_data)
        
        if response.status_code == 200:
            return redirect(url_for('login'))
        
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_email = request.form.get('username_email')
        password = request.form.get('password')

        form_data = {
            "username": username_email,
            "password": password
        }

        response = requests.post(API_URL+'/login', form_data)

        if response.status_code == 200:
            # get the session from the backend
            session_response = requests.get(f"{API_URL}/get_session", cookies=response.cookies)
            
            if session_response.status_code == 200:
                session_response_json = session_response.json()
                user_id = session_response_json.get("session")
                print(user_id)
                session['user_id'] = user_id # use the session in the backend to create your session here
                return redirect(url_for('dashboard'))
            else:
                flash("No active session found. Please log in.")
                return redirect(url_for('login'))
        else:
            flash('Incorrect Login Details')
            return redirect(url_for('login'))
    return render_template('login.html')
    

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # if request.method == "GET":
    #     response = requests.get(API_URL+'/read_todo_list')
    #     if response.status_code == 200:
    #         response_py = response.json()
    #         todo = response_py.get('message', [])
    #         return render_template('dashboard.html', todo=todo)
    #     else:
    #         return ('Error')
        
    if request.method == "POST":
        start_date = request.form.get('start_date')
        finish_date = request.form.get('finish_date')
        priority = request.form.get('priority')
        category = request.form.get('category')
        notes = request.form.get('notes')

        form_data = {
            "start_date": start_date,
            "finish_date": finish_date,
            "priority": priority,
            "category": category,
            "notes": notes
        }

        response = requests.post(API_URL+'/create_todo', form_data)
        
        if response.status_code != 200:
            return ('Error in POST')
    
    # for GET
    response = requests.get(API_URL+'/read_todo_list')
    if response.status_code == 200:
        response_py = response.json()
        todo = response_py.get('message', [])
        return render_template('dashboard.html', todo=todo)
    else:
        return ('Error')

@app.route('/logout')
def logout():
    logout_response = requests.get(API_URL+'/logout')
    if logout_response.status_code == 200:
        flash("Logged Out Successfully")
        return redirect(url_for('login'))
    return ('Error Occurred while Logging Out')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
