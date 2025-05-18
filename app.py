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



if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5001)