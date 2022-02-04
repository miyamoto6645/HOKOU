{{
  "nbformat":4、
  "nbformat_minor":0、
  "メタデータ":{
    「コラボ」:{
      "name": "IMDB映画シリーズ感情分類.ipynb"、
      「来歴」:[]、
      "collapsed_sections":[]
    }、
    "kernelspec":{
      "名前": "python3"、
      "display_name": "Python 3"
    }、
    "language_info":{
      "名前": "python"
    }
  }、
  「セル」:[
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id":"oZc-I-_AVayU"
      }、
      "ソース": [
        「IMDBデータセットダウンロードする」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "s5L0pt1MTDA1"
      }、
      "ソース": [
        "from keras.datasets import imdb \ n"、
        "\ n"、
        "（train_data、train_labels）、（test_data、test_labels）= imdb.load_data（num_words = 10000）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "OcRIIH6qVjZM"
      }、
      "ソース": [
        "トレーニング用データの中身をのぞ射用¥n"、
        "¥n"、
        「0ガネガティブで1ガポジティブ」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "qhIH-vejTJH7"
      }、
      "ソース": [
        "train_data [0] ¥n"、
        "train_labels [0]"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type":"マークダウン"、
      "メタデータ":{
        "id": "WQBh1d6EVzbr"
      }、
      "ソース": [
        「整数のスナップになっますデータを入力に変換」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "AzTyWPOHTR7M"
      }、
      "ソース": [
        "word_index = imdb.get_word_index（）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "7tk3jiDbV0ST"
      }、
      "ソース": [
        "ダウンロードされたリスト、整数の表のリストで表されたダウンロードを文字列にありします。¥n"、
        「3を指定しするのは、0,1,2が得られたな文字の直にされます。
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "XYP4_0veTZO0"
      }、
      "ソース": [
        "reverse_word_index = dict（[（value、key）for（key、value）in word_index.items（）]）¥n"、
        "decoded_review = '' .join（[reverse_word_index.get（i-3、 '？'）for i in train_data [0]]）¥n"、
        "¥n"、
        「decoded_review」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type":"マークダウン"、
      "メタデータ":{
        "id": "Y_2_ejIDWAur"
      }、
      "ソース": [
        「更新は、整数のスナップしらないあり、この適用なる学習の入力できないので、One-hotの言葉しします。できます。
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "lG_rLzy8Tcds"
      }、
      "ソース": [
        "numpyをnpとしてインポート¥n"、
        "¥n"、
        "def vectorize_sequences（sequences、dimension = 10000）:¥n"、
        "結果= np.zeros（（len（sequences）、dimension））¥n"、
        "for i、enumerate（sequences）のシーケンス:¥n"、
        "results [i、sequence] = 1。¥n"、
        「結果を返す¥n」、
        "¥n"、
        "x_train = vectorize_sequences（train_data）¥n"、
        "x_test = vectorize_sequences（test_data）¥n"、
        "¥n"、
        "x_train [0]"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id":"yqYPNe_kWHAL"
      }、
      "ソース": [
        「六小数に変換します。」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "lNFWUiIdTjX8"
      }、
      "ソース": [
        "y_train = np.asarray（train_labels）.astype（ 'float32'）¥n"、
        "y_test = np.asarray（test_labels）.astype（ 'float32'）¥n"、
        "¥n"、
        「y_train」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "aA3q3AytWMBD"
      }、
      "ソース": [
        「ここからここをてします。layers.Denseを使用して、全結合層のみのネットワークします。 16、活性化関数hareluを使用します。また、input_shapeにOne-hotの形の次元します。をいします。」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "ER5LHjZHTny0"
      }、
      "ソース": [
        「kerasインポートモデルから¥n」、
        「kerasインポートレイヤーから¥n」、
        "¥n"、
        "model = models.Sequential（）¥n"、
        "model.add（layers.Dense（16、activation = 'relu'、input_shape =（10000、）））¥n"、
        "model.add（layers.Dense（16、activation = 'relu'））¥n"、
        "model.add（layers.Dense（1、activation = 'sigmoid'））"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "R9yuzxfTWR4L"
      }、
      "ソース": [
        「モデル情報はありのようにコメントできます。」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id":"ExMjjnBxTrqc"
      }、
      "ソース": [
        「model.summary（）」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "MaIJMyNaWVrL"
      }、
      "ソース": [
        「学習のオプティマイザー、ルーム関数、メトリクスを選択します。」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "NejwJ4HiTvg1"
      }、
      "ソース": [
        "model.compile（optimizer = 'rmsprop'、¥n"、
        "loss = 'binary_crossentropy'、¥n"、
        "metrics = ['accuracy']）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "rBH0ySGNWbZr"
      }、
      "ソース": [
        「学習データ計算用と、validation用に前ます。でたほうが精度がなるなる知れません。」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "C14sCKQoT0EM"
      }、
      "ソース": [
        "x_val = x_train [:10000] ¥n"、
        "partial_x_train = x_train [10000:] ¥n"、
        "y_val = y_train [:10000] ¥n"、
        "partial_y_train = y_train [10000:]"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "ed5ZgSxnWhRb"
      }、
      "ソース": [
        「学習はできのようにモデル.fitを実行してます。epochsは20、バッチは512にありは設定しました。」
      ]
    }、
    {{
      "cell_type":"コード"、
      "メタデータ":{
        "id": "8SB30hCvT3RO"
      }、
      "ソース": [
        "history = model.fit（partial_x_train、¥n"、
        "partial_y_train、¥n"、
        "エポック= 20、¥n"、
        "batch_size = 512、¥n"、
        "validation_data =（x_val、y_val））¥n"、
        "history_dict = history.history"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "OCB0O9AbWk-D"
      }、
      "ソース": [
        「model.fithahistoryobjectを来ます。historyobjectははじめのhistoryを来てて学習の際の情報を検討する。」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "xAvj-QLLUCss"
      }、
      "ソース": [
        "history_dict.keys（）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "yKzVtBvJWqZb"
      }、
      "ソース": [
        「ロスの更新をに表示してみます。」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "P_q1tM1WUHJM"
      }、
      "ソース": [
        "%matplotlibインライン¥n"、
        "matplotlib.pyplotをpltとしてインポート¥n"、
        "¥n"、
        "loss_values = history_dict ['loss'] ¥n"、
        "val_loss_values = history_dict ['val_loss'] ¥n"、
        "acc = history_dict ['accuracy'] ¥n"、
        "¥n"、
        "エポック= range（1、len（acc）+ 1）¥ n"、
        "¥n"、
        "plt.plot（epochs、loss_values、 'bo'、label = 'トレーニング損失'）¥n"、
        "plt.plot（epochs、val_loss_values、 'b'、label = '検証損失'）¥n"、
        "plt.title（ 'トレーニングと検証の損失'）¥n"、
        "plt.xlabel（ 'Epochs'）¥n"、
        "plt.ylabel（ 'Loss'）¥n"、
        "plt.legend（）¥n"、
        "¥n"、
        「plt.show（）」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "sHrB9wJVWs4j"
      }、
      "ソース": [
        「もできもいのコードをしてててみます。」
      ]
    }、
    {{
      "cell_type":"コード"、
      "メタデータ":{
        "id": "CUXTVUGqUTVs"
      }、
      "ソース": [
        "val_acc_values = history_dict ['val_accuracy'] ¥n"、
        "¥n"、
        "plt.plot（epochs、acc、 'bo'、label = 'Training acc'）¥n"、
        "plt.plot（epochs、val_acc_values、 'b'、label = 'Validation acc'）¥n"、
        "plt.title（ 'トレーニングと検証の精度'）¥n"、
        "plt.xlabel（ 'Epochs'）¥n"、
        "plt.ylabel（ 'Accuracy'）¥n"、
        "plt.legend（）¥n"、
        "¥ n"、
        「plt.show（）」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type":"マークダウン"、
      "メタデータ":{
        "id": "KxVrRG_iWyh7"
      }、
      "ソース": [
        「テストデータ精度を確認」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "D2UZAMpjUnVE"
      }、
      "ソース": [
        "結果= model.evaluate（x_test、y_test）¥n"、
        「印刷（結果）」
      ]、
      "execution_count":null、
      「出力」:[]
    }
  ]
}