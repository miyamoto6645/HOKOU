{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "テキスト分析.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1wOGTleTx_Za"
      },
      "source": [
        "osetiをインストールする¥n",
        "¥n",
        "osetiとは¥n",
        "東北大学の乾・鈴木研究室のページで公開されている日本語評価極性辞書を使ったSentiment Analysis (いわゆるネガポジ判定) ライブラリ oseti を公開しました。これは日本語評価極性辞書を用いて文の評価極性 (ポジティブ/ネガティブ) のスコアを計算するものです。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Glu5Ohb-V3RI"
      },
      "source": [
        "%%capture capt¥n",
        "¥",
        "# MeCabのインストール¥n",
        "!apt install mecab libmecab-dev mecab-ipadic-utf8¥n",
        "!pip install mecab-python3¥n",
        "¥n",
        "# mecab-ipadic-NEologdのインストール¥n",
        "!apt install git make curl xz-utils file¥n",
        "!git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git¥n",
        "!echo yes | mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a¥n",
        "¥n",
        "# Ref: https://qiita.com/Fulltea/items/90f6ebe6dcceaf64eaef¥n",
        "# Ref: https://qiita.com/SUZUKI_Masaya/items/685000d569452585210c¥n",
        "¥n",
        "!ln -s /etc/mecabrc /usr/local/etc/mecabrc¥n",
        "# Ref: https://qiita.com/Naritoshi/items/8f55d7d5cce9ce414395"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9MN3Hg1OjsQx",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "05043735-1095-4b6d-ec36-a2d92ee197c8"
      },
      "source": [
        "pip install oseti"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: oseti in /usr/local/lib/python3.7/dist-packages (0.2)¥n",
            "Requirement already satisfied: sengiri in /usr/local/lib/python3.7/dist-packages (from oseti) (0.2.1)¥n",
            "Requirement already satisfied: neologdn in /usr/local/lib/python3.7/dist-packages (from oseti) (0.5.1)¥n",
            "Requirement already satisfied: mecab-python3 in /usr/local/lib/python3.7/dist-packages (from oseti) (1.0.4)¥n",
            "Requirement already satisfied: emoji in /usr/local/lib/python3.7/dist-packages (from sengiri->oseti) (1.6.1)¥n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MgGJsOqayGLS"
      },
      "source": [
        "テキストを入れると文ごとの評価極性のスコアが出ます。¥n",
        "¥n",
        "スコアの値は[-1, 1]でプラス値が大きいほどポジティブで、マイナス値が大きいほどネガティブとなります。¥n",
        "¥n",
        "スコアの計算は、単語あるいは用言ごとにポジティブ (+1) あるいはネガティブ (-1) のラベルが付いた辞書を使い、それにマッチすると1あるいは-1の極性値が加えられ、極性値の総和 / マッチした単語・用言の数でスコアを出します。¥n",
        "¥n",
        "たとえば遅刻したけど楽しかったし嬉しかった。という文では、遅刻 (-1)、楽しい (+1)、嬉しい (+1) となり極性値の総和は1で、マッチした数は3なので1 / 3 = 0.3333となります。¥n",
        "¥n",
        "なお、「ない」や「ぬ」といった否定表現があると極性値を反転させます。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p3a3hCsQxpwz",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a726f3c0-a40c-4e53-f818-c409de883ac8"
      },
      "source": [
        "import oseti¥n",
        "¥n",
        "analyzer = oseti.Analyzer()¥n",
        "analyzer.analyze('天国で待ってる。')¥n",
        "# => [1.0]¥n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1.0]"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BW-uWyM7zAQh",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b3e5a501-8c20-4ffa-a244-1351abb6dee8"
      },
      "source": [
        "analyzer = oseti.Analyzer()¥n",
        "analyzer.analyze('天国で待ってない。')¥n",
        "# => [-1.0]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[-1.0]"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rJsQN3vQy4Ua",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a7b8e003-57f9-4730-b292-b3d223f905ff"
      },
      "source": [
        "analyzer.analyze('遅刻したけど楽しかったし嬉しかった。すごく充実した!')¥n",
        "# => [0.3333333333333333, 1.0]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[0.3333333333333333, 1.0]"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Jh7KfZNXzRVT"
      },
      "source": [
        "count_polarity methodでは、ポジティブ/ネガティブ表現の数のみを返却します。文単位でなく文書単位の極性値を測りたい場合や、違った手法でスコアリングしたい場合に向いています。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FGC8ZdZkxv5h",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7e8e58d3-ae60-4ab1-d773-24c2017ccad3"
      },
      "source": [
        "analyzer.count_polarity('遅刻したけど楽しかったし嬉しかった。すごく充実した！')¥n",
        "# => [{'positive': 2, 'negative': 1}, {'positive': 1, 'negative': 0}])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'negative': 1, 'positive': 2}, {'negative': 0, 'positive': 1}]"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yC1yP7DHy8ww",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7eefb9c4-746d-4779-bd6d-f61ba5c8fc13"
      },
      "source": [
        "analyzer.count_polarity('そこにはいつもと変わらない日常があった。')¥n",
        "# => [{'positive': 0, 'negative': 0}]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'negative': 0, 'positive': 0}]"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "evoxCiztzWA5"
      },
      "source": [
        "analyze_detail メソッドではどの単語がポジティブ/ネガティブ判定されたのかという情報も出力されます。デバッグ用に役立つかもしれません。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FzpdRHUjzZ2h",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "15f2b295-afca-4bca-a6c5-570c4b3487ab"
      },
      "source": [
        "analyzer.analyze_detail('お金も希望もない！')¥n",
        "# => [{'positive': [], 'negative': ['お金-NEGATION', '希望-NEGATION'], 'score': -1.0}])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'negative': ['お金-NEGATION', '希望-NEGATION'], 'positive': [], 'score': -1.0}]"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bk-462ZazjJJ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b4d6cf08-81e3-493c-958c-fc7ca0c81703"
      },
      "source": [
        "analyzer.analyze_detail('お金がないわけではない')¥n",
        "# => [{'positive': ['お金'], 'negative': [], 'score': 1.0}]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'negative': [], 'positive': ['お金'], 'score': 1.0}]"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    }
  ]
}