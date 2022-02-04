{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "音声認識.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6sjE2HsP80xm"
      },
      "source": [
        "wavファイルから音声を読み込み、文字列として返却するプログラムです¥n",
        "¥n",
        "Speech Recognition APIとは¥n",
        "¥n",
        "音声データをAPIに渡すとその音声データをテキストに変換して返してくれます。¥n",
        "¥n",
        "まずはSpeech Recognitionのインストールを行います。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HASD44okzuxg"
      },
      "source": [
        "pip install SpeechRecognition"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tc6j8iSC9kEe"
      },
      "source": [
        "次は文字列に変換する音声データをアップロードします"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Fimgo-Xi6rjv"
      },
      "source": [
        "from google.colab import files¥n",
        "uploaded_file = files.upload()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "A_rqIOvD9rus"
      },
      "source": [
        "アップロードした音声データのファイル名を取得します"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1PZxS3gd6v0-"
      },
      "source": [
        "uploaded_file_name = list(uploaded_file.keys())[0]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AGLmgtdq9xNE"
      },
      "source": [
        "speech_recognitionをインポートします¥n",
        "¥n",
        "インポートしたらRecognize メソッドを実行します¥n",
        "¥n",
        "これは同期音声認識操作を開始します。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TcTGfyYX5UR_"
      },
      "source": [
        "import speech_recognition as sr¥n",
        "r = sr.Recognizer()¥n",
        "with sr.AudioFile(uploaded_file_name) as source:¥n",
        "      audio = r.record(source)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jU95Z8QoAIL8"
      },
      "source": [
        "音声を文字列にして表示する"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HPiMQCW28Lie"
      },
      "source": [
        "print('文字起こし結果:¥¥n',r.recognize_google(audio,language='ja'))"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}