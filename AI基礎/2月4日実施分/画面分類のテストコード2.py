{{
  "nbformat":4、
  "nbformat_minor":0、
  "メタデータ":{
    「コラボ」:{
      "name": "画像分類のコード2.ipynb"、
      「来歴」:[]、
      "collapsed_sections":[]
    }、
    "kernelspec":{
      "名前":"python3"、
      "display_name":"Python 3"
    }、
    "language_info":{
      "名前": "python"
    }
  }、
  「セル」:[
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "nD4Ix13cqjGa"
      }、
      "ソース": [
        "Phなし＃をアップロード¥n"、
        "¥n"、
        "** tensorflow **は機械学習用のPAN ¥n"、
        "¥n"、
        "* matplotlib.pyplot *は（画像）を表示して¥n"、
        "¥n"、
        「numpyはやや計算をしてててけ」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id":"IgX0EpVJnK6Z"
      }、
      "ソース":[
        "テンソルフローをtfとしてインポート¥n"、
        "matplotlib.pyplotをpltとしてインポート¥n"、
        「numpyをnpとしてインポートする」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "1hCiLyZRq2Uo"
      }、
      "ソース": [
        "データセットをする\ n"、
        "\ n"、
        "（x_train、y_train）はトレーニング用のデータ\ n"、
        "\ n"、
        "（x_test、y_test）はテスト用のデータ"
      ]
    }、
    {{
      "cell_type":"コード"、
      "メタデータ":{
        "id": "_ MFtMaL2nRvj"
      }、
      "ソース": [
        "fashion_mnist = tf.keras.datasets.fashion_mnist \ n"、
        "（x_train、y_train）、（x_test、y_test）= fashion_mnist.load_data（）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "ogssJxidrhGQ"
      }、
      "ソース": [
        "x_train中身をすること\ n"、
        "\ n"、
        "fashion_mnistの表は28＊28ピクセルのカラーとラベルのラベル適用"
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id":"S-Onkv-mnk-X"
      }、
      "ソース": [
        "print（x_train [0]）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "ullotMRcrqJw"
      }、
      "ソース": [
        「画像表示」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id":"lZPXCRuwoZC6"
      }、
      "ソース":[
        "plt.imshow（x_train [0]）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "ttnBBqwHruII"
      }、
      "ソース": [
        「表数字をたものなのか確認」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id":"9e3n-i5Xo2L5"
      }、
      "ソース": [
        "print（y_train [0]）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "-tkvXrjXr0Cp"
      }、
      "ソース": [
        "データの正規化\ n"、
        "\ n"、
        "データをダウンロード変形する\ n"、
        "\ n"、
        「精度をいいにれ」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "6K-V86iJouWC"
      }、
      "ソース": [
        "x_train = tf.keras.utils.normalize（x_train、axis = 1）¥n"、
        "x_test = tf.keras.utils.normalize（x_test、axis = 1）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "63PTScMtsvsQ"
      }、
      "ソース": [
        "学習モデルの¥n"、
        "¥n"
      ]
    }、
    {{
      "cell_type":"コード"、
      "メタデータ":{
        "id": "u5yz_DKLpEKC"
      }、
      "ソース": [
        "model = tf.keras.models.Sequential（）¥ n"、
        "model.add（tf.keras.layers.Flatten（））¥n"、
        "model.add（tf.keras.layers.Dense（128、activation = tf.nn.relu））¥n"、
        "model.add（tf.keras.layers.Dense（128、activation = tf.nn.relu））¥n"、
        "model.add（tf.keras.layers.Dense（10、activation = tf.nn.softmax））¥n"、
        "¥n"、
        "model.compile（optimizer = ¥" adam ¥"、¥n"、
        "loss = ¥" sparse_categorical_crossentropy ¥"、¥n"、
        "metrics = [¥" accuracy ¥"]）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "xS3Egckls2ix"
      }、
      "ソース": [
        「学習用データを学習する学習」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "xFG0E-MBpMAx"
      }、
      "ソース": [
        "model.fit（x_train、y_train、epochs = 5）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "0rBaaetfs6cA"
      }、
      "ソース":[
        「評価されたモデルを評価」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "blIrJnCmpZzh"
      }、
      "ソース": [
        "val_loss、vall_acc = model.evaluate（x_test、y_test）¥ n"、
        "print（val_loss、vall_acc）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "nA4uUR6GtBYg"
      }、
      "ソース": [
        「予測と画像を」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id":"c6BBwU6TpivJ"
      }、
      "ソース": [
        "predictions = model.predict（[x_test]）¥ n"、
        "fig = plt.figure（figsize =（9、9））¥n"、
        "plt.subplots_adjust（wspace = 1、hspace = 1）¥ n"、
        "for i in range（9）:¥n"、
        "ax = fig.add_subplot（3、3、1 + i）¥n"、
        "ax。imshow（x_test [i]）¥ n"、
        "ax.set_title（¥" prediction:{} ¥"。format（np.argmax（predictions [i]）））¥n"、
        「plt.show（）」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "ireiEZ5y7sKb"
      }、
      "ソース": [
        「ここでた画像をしてました」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "pxNN3blR0_Fu"
      }、
      "ソース": [
        "google.colabインポートファイルから¥n"、
        "uploaded_file = files.upload（）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type":"コード"、
      "メタデータ":{
        "id": "euhJ1ZF4psya"
      }、
      "ソース": [
        "uploaded_file_name = list（uploaded_file.keys（））[0]"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "rEybBi4z2LUE"
      }、
      "ソース": [
        "import cv2 ¥n"、
        "¥n"、
        "defpredict_number（uploaded_file）:¥n"、
        "＃写真¥n"、
        "img = cv2.imread（uploaded_file）¥n"、
        "＃ここだ画像を表示¥n"、
        "print（¥"ここだ元画像¥"）¥n"、
        "plt.imshow（img）¥n"、
        "plt.axis（¥" off ¥ "）¥n"、
        "plt.show（）¥ n"、
        "img = cv2.cvtColor（img、cv2.COLOR_BGR2GRAY）¥n"、
        "＃写真画像をリ捕¥ n"、
        "img = cv2.resize（img、（28,28））¥ n"、
        "¥n"、
        "＃ネガ反転反転¥n"、
        "img = 255-img ¥n"、
        "¥n"、
        "＃モデルに流しされた画像する¥ n"、
        "print（¥"ここにモデルに流しイラスト¥n "）¥n"、
        "plt.imshow（img）¥ n"、
        "plt.axis（¥" off ¥ "）¥n"、
        "plt.show（）¥n"、
        "¥n"、
        "＃データを（1、28、28）の三次元配列に変換¥n"、
        "img = img.reshape（1、28、28、1）.astype（ 'float32'）¥255 ¥n"、
        "＃予測¥n"、
        "ret = model.predict（img）¥n"、
        "return ret ¥n"、
        "¥n"、
        "＃画像を指定¥n"、
        "ans = Forecast_number（uploaded_file_name）¥n"、
        "print（¥"この画像の数字は¥"+ str（np.argmax（ans））+ ¥"デス¥¥n ¥"）¥n"
      ]、
      "execution_count":null、
      「出力」:[]
    }
  ]
}