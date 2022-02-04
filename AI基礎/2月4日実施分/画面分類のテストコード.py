
{{
    "nbformat":4、
    "nbfornat minor":0、
    "メタデータ":{
        「コラボ」:{
            "name":"画像分類のコード.ipynd"、
            「来歴」:「」、
            "collapsed_sections":[]
        }、
    "karnelspec":{
        "名前": "python3"
        "display_name":"Python3"
    }、
    "language_info":{
        "名前":"python"
    }
}、
    「セル」:[
        {{
            "cell type":"マークダウン"、
            "メタデータ":{
                "id":"nD41x13cqjGa"
            }、
            "ソース":[
                "Phなし#をアップロード¥n"、
                "¥n"、
                "tensofflowは機械学習用のPAN¥n"、
                "¥n"、
                "matplotlib.pythonはグラフ(画像)を表示する¥n"、
                "¥n"、
                「numpyはやや計算をしてててけ」
            ]
        }、
        {{
            "cell type":"コード"、
            "メタデータ":{
                "id":"IgXOEpVJnK6Z"
            }、
            "ソース":[
                "テンソルフローをtfとしてインポート¥n"、
                "matplotlib.pyplotをpitとしてインポート¥n"、
                「numpyをnpとしてインポートする」
            ]、
            "execution count":null、
            「出力」:[]
        }、
        {{
            "cell type":"マークダウン"、
            "メタデータ":{
                "id":"1hCiLyZRq2Uo"
            }、
            "ソース":[
                "データセットをする¥n"、
                "￥n"、
                "(x train、y_train)はトレーニングデータ¥n"、
                "¥n"、
                "(x_test、y_test)はテスト用のデータ"
            ]
        }
        {{
            "cell type":"コード"、
            "メタデータ":{
                "id":"_MFtMaL2nRvj"
            }、
            "ソース":[
                "mnist=tf.keras.datasets.mnist¥n"、
                "(x_train、y_train)、(x_test、y_test)=mnist.load_date()"
            ]、
            "execution count":null、
            「出力」:[]
        }、
        {{
            "cell_type":"マークダウン"、
            "メタデータ":{
                "id":"S-Onkv-mnk-X"
            }、
            "ソース":[
                "print(x_train[0])"
            ]、
            "execution_count":null、
            「出力」:[]
        }、
        {{  
            "cell_type":"マークダウン"、
            "メタデータ":{
                "id":"ullotMRcrqJw"
            }、
            {{
                "cell_type":"コード"、
                "メタデータ":{
                    "id":"lZPXCRuwoZC6"
                }、
                "ソース":[
                    「画像表示」
                ]
            }、
            {{
                "cell_type":"コード"、
                "メタデータ":{
                "id":"lZPXCRuwoZC6"
                }、
            "ソース":[
                "plt.imshow(x_train[0])"
            ]、
            "execution_count":null、
            「出力」:[]
            }、
            {{
                "cell_type":"マークダウン"、
                "メタデータ":{
                    "id":"ttnBBqwHrull"
                }、
                "ソース":[
                    「表数字をたものなのか確認」
                ]
            }
            {{
                "cell_type":"コード"、
                "メタデータ":{
                    "id":"9e3n-i5Xo2L5"
                }、
                "ソース":[
                    "print(y_train[0])"
                ]、
                "execution_count":null、
                「出力」:[]
            }、
            {{
                "cell_type":"マークダウン"、
                "メタデータ":{
                    "id":"-tKvXrjXr0Cp"
                }、
                "ソース":[
                    "データの正規化¥n"、
                    "¥n"、
                    "データをダウンロード変形する¥n"、
                    "¥n"、
                    「精度をいいにれ」
                ]
            }、
            {{
                "cell_type":"コード"、
                "メタデータ":{
                    "id":"6K-V86iJouWC"
                }、
                "ソース":[
                    "x_train= tf.keras.utils.normalize(x_train、axis=1)¥n"、
                    "x_test = tf.keras.utils.normalize(x_test、axis = 1)"
                ]、
                "execution_count":null、
                「出力」:[]
            }、
            {{
                "cell_type":"マークダウン"、
                "メタデータ":{
                    "id":"63PTScMtsvqQ"
                }、
                "ソース":[
                    "model = tf.keras.models.Sequential（） ¥n"、
                    "model.add（tf.keras.layers.Flatten（））¥n"、
                    "model.add（tf.keras.layers.Dense（128、activation = tf.nn.relu））¥n"、
                    "model.add（tf.keras.layers.Dense（128、activation = tf.nn.relu））¥n"、
                    "model.add（tf.keras.layers.Dense（10、activation = tf.nn.softmax））¥n"、
                    "¥n"、
                    "model.compile（optimizer = ¥" adam ¥"、¥n"、
                    "loss = ¥" sparse_categorical_crossentropy:¥"、¥n"、
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
                    "id":"xFG0E-MBpMAx"
                }、
            "ソース": [
                "model.fit（x_train、y_train、epochs = 3）"
            ]、
            "execution_count":null、
            「出力」:[]
            }、
         {{
            "cell_type": "マークダウン"、
            "メタデータ":{
                "id":"0rBaaetfs6cA"
            }、
            "ソース": [
        「評価されたモデルを評価」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "blIrJnCmpZzh"
      }、
      "ソース": [
        "val_loss、vall_acc = model.evaluate（x_test、y_test）\ n"、
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
        "predictions = model.predict（[x_test]）¥n"、
        "fig = plt.figure（figsize =（9、9））¥n"、
        "plt.subplots_adjust（wspace = 1、hspace = 1）¥n"、
        "for i in range（9）:¥n"、
        "ax = fig.add_subplot（3、3、1 + i）¥n"、
        "ax。imshow（x_test [i]）¥n"、
        "ax.set_title（¥" prediction:{} ¥"。format（np.argmax（predictions [i]）））¥ n"、
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
      "ソース":[
        「ここでた画像をしてました」
      ]
    }、
    {{
      "cell_type":"コード"、
      "メタデータ":{
        "id": "pxNN3blR0_Fu"
      }、
      "ソース": [
        "google.colabインポートファイルから\ n"、
        "uploaded_file = files.upload（）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "euhJ1ZF4psya"
      }、
      "ソース":[
        "uploaded_file_name = list（uploaded_file.keys（））[0]"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
         "cell_type": "コード"、
      "メタデータ":{
        "id":"rEybBi4z2LUE"
      }、
      "ソース": [
        "import cv2 ¥ n"、
        "¥n"、
        "defpredict_number（uploaded_file）:¥n"、
        "＃写真¥n"、
        "img = cv2.imread（uploaded_file）¥n"、
        "＃ここだ画像を表示¥n"、
        "print（¥"ここだ元画像¥ "）¥n"、
        "plt.imshow（img）¥n"、
        "plt.axis（¥" off ¥"）¥n"、
        "plt.show（）¥n"、
        "img = cv2.cvtColor（img、cv2.COLOR_BGR2GRAY）¥n"、
        "＃写真画像をリ捕¥n"、
        "img = cv2.resize（img、（28,28））¥n"、
        "¥ n"、
        "＃ネガ反転反転¥n"、
        "img = 255-img ¥n"、
        "¥n"、
        "＃モデルに流しされた画像する¥n"、
        "print（¥"ここにモデルに流しイラスト¥n "）¥n"、
        "plt.imshow（img）¥n"、
        "plt.axis（¥" off ¥"）¥n"、
        "plt.show（）¥n"、
        "¥n"、
        "＃
        "img = img.reshape（1、28、28、1）.astype（ 'float32'）/ 255 ¥n"、
        "＃予測¥n"、
        "ret = model.predict（img）¥n"、
        "return ret ¥n"、
        "¥n"、
        "¥n"、
        "＃画像を指定¥n"、
        "ans = Forecast_number（uploaded_file_name）¥n"、
        "print（¥"この画像の数字は¥ "+ str（np.argmax（ans））+ ¥"です¥¥n ¥ "）"
      ]、
       "execution_count":null、
      「出力」:[]
    }
}}
        
            
