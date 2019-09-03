from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello333():
    return "<h1>이종현 개잘생김</h1>"

@app.route('/bit/')
def hello334():
    return "<h1>난 해적왕이 될꺼야!</h1>"

if __name__ == '__main__':
    #app.run(host="127.0.0.1", port=5000, debug=False)
    app.run(host="127.0.0.1", port=8888, debug=False)

#  Running on http://127.0.0.1:8888/: 웹서버가 돌아감
# 127.0.0.1 - - [03/Sep/2019 10:07:16] "GET /bit/ HTTP/1.1" 200: 200이 뜨면, 정상적으로 작동