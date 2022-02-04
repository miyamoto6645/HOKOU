{{
  "nbformat":4、
  "nbformat_minor":0、
  "メタデータ":{
    「コラボ」:{
      "名前": "spleeter.ipynb"、
      「来歴」:[]、
      "collapsed_sections":[]
    }、
    "kernelspec":{
      "display_name": "Python 3"、
      "名前": "python3"
    }
  }、
  「セル」:[
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "K6mcSc0mmp3i"
      }、
      "ソース" [
        「#スプリーターのインストール」
      ]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "APdmXJY2FExq"
      }、
      "ソース": [
        "FFmpegは三重でややルートの変換・圧縮がいち自由になります。で行で操作することになります。
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "f8Brdfh6mzEz"
      }、
      "ソース": [
        "!apt install ffmpeg"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "QGaQkadKFGlx"
      }、
      "ソース": [
        「実リーターハ音楽ダウンロードを試してますます」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id":"V_6Ram1lmc1F"
      }、
      "ソース": [
        「pipinstallspleeter」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "I1tEjoZsFbGh"
      }、
      "ソース": [
        "IPythonは、Pythonの対話型インタプリタをつけた（これい）。¥n"、
        "¥n"、
        "もももの拡張に留まます、できますとありの機能をもら。¥n"、
        "¥n"、
        "¥n"、
        "¥n"、
        "拡張された対話型シェル¥ n"、
        "¥n"、
        "分離型間通信モデル¥n"、
        "¥n"、
        "並列計算モジュール¥n"、
        "¥n"、
        "¥n"、
        「IPython.displayは「画像やします」を表示しますます。」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "W0LktyMypXqE"
      }、
      "ソース": [
        「IPython.displayからオーディオをインポート」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "afbcUSken16L"
      }、
      "ソース": [
        「#コマンドラインとはまた」
      ]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "QOCQXHfWGxkq"
      }、
      "ソース": [
        「音楽ファイルをダウンロードされたURLからダウンロードします。」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "O1kQaoJSoAD0"
      }、
      "ソース": [
        "!wget https://github.com/deezer/spleeter/raw/master/audio_example.mp3"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "S59b4NumG59J"
      }、
      "ソース": [
        「音楽もをける」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "ibG6uF55p4lH"
      }、
      "ソース": [
        "Audio（ 'audio_example.mp3'）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "7w1x7dAkG-FI"
      }、
      "ソース": [
        「音楽データを分割します」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "dGL-k5xxoKbu"
      }、
      "ソース": [
        「!spleeterseparate -o output / audio_example.mp3」
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "DU2Akuy8Hnjh"
      }、
      "ソース": [
        「分割してします」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "IDuPWcAMoZP_"
      }、
      "ソース": [
        "!ls output / audio_example"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "マークダウン"、
      "メタデータ":{
        "id": "BoiZZ2VIHrZh"
      }、
      "ソース": [
        「ここの音楽を流しみます」
      ]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "e7CHpyiloxrk"
      }、
      "ソース": [
        "Audio（ 'output / audio_example / vocals.wav'）"
      ]、
      "execution_count":null、
      「出力」:[]
    }、
    {{
      "cell_type": "コード"、
      "メタデータ":{
        "id": "ibXd-WCTpT0w"
      }、
      "ソース": [
        "Audio（ 'output / audio_example / accompaniment.wav'）"
      ]、
      "execution_count":null、
      「出力」:[]
    }
  ]
}