from crypt import methods
from flask import Flask, render_template, request

# Flaskインスタンスの作成
app = Flask(__name__)  # アプリケーション本体


# ルーティング
# appのrouteデコレーターでルートにアクセスした時にindexを呼び出す
# GETアクセスした時
@app.route('/', methods=['GET'])
def get_index():
  return render_template('index.html',
    message = 'What is your name and ID?',
    name = '',
    id = ''
  )
# POSTアクセスした時
@app.route('/', methods=['POST'])
def form_index():
  nickname = request.form['nickname']
  number = request.form['number']
  return render_template('index.html',
    message = "Hello, %s!" % nickname,
    name = nickname,
    id = number
  )


# クエリパラメータを埋め込む
@app.route('/todo/<id>-<name>')
def todo(id, name):
  i = 'ID : %s' % (id)
  nickname = '%s' % (name)
  return render_template('todo.html',
    name = nickname,
    ID = i
  )

# pythonコマンドでapp.pyを実行できるようにする
if __name__ == '__main__':  # 起動モジュールがメインプログラムのモジュールである場合
  app.debug = True  # デバッグ機能ON
  app.run(host='localhost')  # localhostがホスト名である時Webアプリケーションを起動
