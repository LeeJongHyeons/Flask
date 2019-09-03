from flask import Flask

app = Flask(__name__)

from flask import make_response

@app.route('/')
def index():
    response = make_response('<h1> 짜요짜요  !!!</h1>') # response: 서버에서 응답하는걸 출력, # client: 고객(서버측에 응답)
    response.set_cookie('answer', '42')
    return response

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)

