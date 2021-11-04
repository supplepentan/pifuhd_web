# request フォームから送信した情報を扱うためのモジュール
# redirect  ページの移動
# url_for アドレス遷移
from flask import Flask, request, abort, render_template, redirect, url_for
from time import time
from datetime import timedelta
import os
from pathlib import Path
from typing import List
import sys
import cv2
import glob
from PIL import Image
#from run import process
import numpy as np
import io
import base64
import datetime

import apps.resize
import apps.simple_test


# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
def allwed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def handle_image():
    try:
        """
        # ファイルがなかった場合の処理
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        # データの取り出し
        file = request.files['file']
        # ファイル名がなかった時の処理
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        # ファイルのチェック
        if file and allwed_file(file.filename):
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
        """

        com_img = apps.resize.resize(request.files['file'], './image/template.png')
        com_img.save('./sample_images/test.png')
        apps.simple_test.trans()

        return render_template('index.html', img = True)
    except:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)