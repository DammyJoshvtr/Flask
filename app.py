from flask import Flask, render_template, make_response, request, redirect, url_for, Response

import pandas as pd

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
  # you can dynamicallly change the content of the html file by passing certain keyword argumants...
  myValue = 'Flask'
  myResult = 5.00
  myList = [150, 20, 90, 'Flask']
  myArr = [160, 30, 'Python']
  return render_template('index.html', myValue=myValue, myResult=myResult, myList=myList, myArr=myArr)

@app.route('/greet/<name>')
def greet(name):
  return f'Good Afternoon {name}'

# to make a custom response...
@app.route('/hello')
def hello():
  response = make_response('Hello World\n')
  response.status_code = 202
  response.headers['content-type'] = 'application/octet/stream'
  return response


# to you make the route be /jnviddvjnjnjnvjnv, since you've used url_for in the template to make it dynamic
@app.route('/other')
def other():
  someText = 'hello World'
  return render_template('other.html', someText=someText)

@app.route('/redirect_endpoint')
def redirect_endpoint():
  return redirect(url_for('other'))


@app.template_filter('reverse_string')
def reverse_string(s):
  return s[::-1]

@app.template_filter("repeat")
def repeat(s, times=2):
  return s*times

@app.template_filter('alternate_case')
def alternate_case(s):
  return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

# dummy login form
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  elif request.method == 'POST':
    username = request.form.get('username')
    password =  request.form.get('password')
    
    if username == 'damilola' and password == 'password':
      return 'Success'
    else: return 'Failure Logging In'
    
@app.route('/file_upload', methods=['POST'])
def file_upload():
  file = request.files['file']
  
  if file.content_type == 'text/plain':
    return file.read().decode()
  

# creating a download functionality to convert excel to csv...
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
  file= request.files['file']
  
  df = pd.read_excel(file)
  
  response = Response(
    df.to_csv(), #since a path is not specified an object would be returned
    mimetype='text/csv',
    headers={
      'Content=Disposition': 'attachment: filename=result.csv'
    }
  )
  return response

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5001)