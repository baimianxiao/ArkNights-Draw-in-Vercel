# -*- encoding:utf-8 -*-

from flask import Flask, send_file
from PIL import Image
from os.path import dirname, abspath, join
import io

app = Flask(__name__)
dir = dirname(abspath(__file__))

@app.route("/arknights/arknightsdraw", methods=['POST', 'GET'])
def arknights():
    return "sss"



@app.route('/',methods=['POST', 'GET'])
def arknights_draw():
    # 从数组加载图片
    # arr = np.array(raw_data)
    # img = Image.fromarray(arr.astype('uint8'))
    img = Image.open(join(dir, '..', 'docs', 'main.png'))
    # 在内存中创建图片对象
    file_object = io.BytesIO()
    # write PNG in file-object
    img.save(file_object, 'png')
    file_object.seek(0)
    return send_file(file_object, mimetype='image/png')



if __name__ == "__main__":
    app.run(debug=True)
    print("servers start")
