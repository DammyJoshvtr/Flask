from flask import Flask, render_template, make_response, request

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

@app.route('/other')
def other():
  someText = 'hello World'
  return render_template('other.html', someText=someText)

@app.template_filter('reverse_string')
def reverse_string(s):
  return s[::-1]

@app.template_filter("repeat")
def repeat(s, times=2):
  return s*times

@app.template_filter('alternate_case')
def alternate_case(s):
  return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5001)