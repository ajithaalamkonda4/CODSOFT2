{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPEsHjnFZEDyCj5/Tk47SyM",
      "include_colab_link": true
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
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ajithaalamkonda4/CODSOFT2/blob/main/handwrittenText.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HuR0Y6KvFBcn",
        "outputId": "2011b629-2930-4540-8f9c-2a71aa6cd54d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt\n",
            "\u001b[1m1115394/1115394\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 0us/step\n",
            "Total characters: 1115394\n",
            "First Citizen:\n",
            "Before we proceed any further, hear me speak.\n",
            "\n",
            "All:\n",
            "Speak, speak.\n",
            "\n",
            "First Citizen:\n",
            "You are all resolved rather to die than to famish?\n",
            "\n",
            "All:\n",
            "Resolved. resolved.\n",
            "\n",
            "First Citizen:\n",
            "First, you know Caius Marcius is chief enemy to the people.\n",
            "\n",
            "All:\n",
            "We know't, we know't.\n",
            "\n",
            "First Citizen:\n",
            "Let us\n"
          ]
        }
      ],
      "source": [
        "import tensorflow as tf\n",
        "\n",
        "path = tf.keras.utils.get_file(\n",
        "    'shakespeare.txt',\n",
        "    'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt'\n",
        ")\n",
        "\n",
        "with open(path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "print(\"Total characters:\", len(text))\n",
        "print(text[:300])"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install tensorflow numpy matplotlib"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PLQdXZN9FlkZ",
        "outputId": "4faee0fb-c6f3-488c-b8ed-d8ecbae35671"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: tensorflow in /usr/local/lib/python3.12/dist-packages (2.20.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.12/dist-packages (2.0.2)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.12/dist-packages (3.10.0)\n",
            "Requirement already satisfied: absl-py>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (1.4.0)\n",
            "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (1.6.3)\n",
            "Requirement already satisfied: flatbuffers>=24.3.25 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (25.12.19)\n",
            "Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (0.7.0)\n",
            "Requirement already satisfied: google_pasta>=0.1.1 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (0.2.0)\n",
            "Requirement already satisfied: libclang>=13.0.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (18.1.1)\n",
            "Requirement already satisfied: opt_einsum>=2.3.2 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (3.4.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.12/dist-packages (from tensorflow) (26.2)\n",
            "Requirement already satisfied: protobuf>=5.28.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (5.29.6)\n",
            "Requirement already satisfied: requests<3,>=2.21.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (2.32.4)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.12/dist-packages (from tensorflow) (75.2.0)\n",
            "Requirement already satisfied: six>=1.12.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (1.17.0)\n",
            "Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (3.3.0)\n",
            "Requirement already satisfied: typing_extensions>=3.6.6 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (4.15.0)\n",
            "Requirement already satisfied: wrapt>=1.11.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (2.2.1)\n",
            "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (1.81.0)\n",
            "Requirement already satisfied: tensorboard~=2.20.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (2.20.0)\n",
            "Requirement already satisfied: keras>=3.10.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (3.13.2)\n",
            "Requirement already satisfied: h5py>=3.11.0 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (3.16.0)\n",
            "Requirement already satisfied: ml_dtypes<1.0.0,>=0.5.1 in /usr/local/lib/python3.12/dist-packages (from tensorflow) (0.5.4)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.3.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (4.63.0)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.5.0)\n",
            "Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (11.3.0)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (3.3.2)\n",
            "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (2.9.0.post0)\n",
            "Requirement already satisfied: wheel<1.0,>=0.23.0 in /usr/local/lib/python3.12/dist-packages (from astunparse>=1.6.0->tensorflow) (0.47.0)\n",
            "Requirement already satisfied: rich in /usr/local/lib/python3.12/dist-packages (from keras>=3.10.0->tensorflow) (13.9.4)\n",
            "Requirement already satisfied: namex in /usr/local/lib/python3.12/dist-packages (from keras>=3.10.0->tensorflow) (0.1.0)\n",
            "Requirement already satisfied: optree in /usr/local/lib/python3.12/dist-packages (from keras>=3.10.0->tensorflow) (0.19.1)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.21.0->tensorflow) (3.4.7)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.21.0->tensorflow) (3.18)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.21.0->tensorflow) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.21.0->tensorflow) (2026.5.20)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.12/dist-packages (from tensorboard~=2.20.0->tensorflow) (3.10.2)\n",
            "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.12/dist-packages (from tensorboard~=2.20.0->tensorflow) (0.7.2)\n",
            "Requirement already satisfied: werkzeug>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from tensorboard~=2.20.0->tensorflow) (3.1.8)\n",
            "Requirement already satisfied: markupsafe>=2.1.1 in /usr/local/lib/python3.12/dist-packages (from werkzeug>=1.0.1->tensorboard~=2.20.0->tensorflow) (3.0.3)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.12/dist-packages (from rich->keras>=3.10.0->tensorflow) (4.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.12/dist-packages (from rich->keras>=3.10.0->tensorflow) (2.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.12/dist-packages (from markdown-it-py>=2.2.0->rich->keras>=3.10.0->tensorflow) (0.1.2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import tensorflow as tf\n",
        "from tensorflow.keras.models import Sequential\n",
        "from tensorflow.keras.layers import LSTM, Dense\n",
        "from tensorflow.keras.callbacks import EarlyStopping\n",
        "import matplotlib.pyplot as plt\n",
        "import random\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "# ============================================================\n",
        "# STEP 1: LOAD DATASET (Shakespeare - Auto Download)\n",
        "# ============================================================\n",
        "print(\"STEP 1: Loading Dataset\")\n",
        "\n",
        "path = tf.keras.utils.get_file(\n",
        "    'shakespeare.txt',\n",
        "    'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt'\n",
        ")\n",
        "\n",
        "with open(path, 'r') as f:\n",
        "    text = f.read()\n",
        "\n",
        "# Use a smaller portion to train faster\n",
        "text = text[:200000]\n",
        "\n",
        "print(\"Total characters:\", len(text))\n",
        "print(\"Sample text:\\n\", text[:300])\n",
        "\n",
        "# ============================================================\n",
        "# STEP 2: PREPARE CHARACTER MAPPINGS\n",
        "# ============================================================\n",
        "print(\"\\nSTEP 2: Preparing Character Mappings\")\n",
        "\n",
        "chars      = sorted(list(set(text)))\n",
        "vocab_size = len(chars)\n",
        "\n",
        "print(\"Total unique characters:\", vocab_size)\n",
        "\n",
        "char_to_idx = {ch: i for i, ch in enumerate(chars)}\n",
        "idx_to_char = {i: ch for i, ch in enumerate(chars)}\n",
        "\n",
        "print(\"Mapping done!\")\n",
        "\n",
        "# ============================================================\n",
        "# STEP 3: CREATE SEQUENCES\n",
        "# ============================================================\n",
        "print(\"\\nSTEP 3: Creating Sequences\")\n",
        "\n",
        "SEQ_LENGTH = 100\n",
        "STEP       = 3\n",
        "\n",
        "sequences  = []\n",
        "next_chars = []\n",
        "\n",
        "for i in range(0, len(text) - SEQ_LENGTH, STEP):\n",
        "    sequences.append(text[i: i + SEQ_LENGTH])\n",
        "    next_chars.append(text[i + SEQ_LENGTH])\n",
        "\n",
        "print(\"Total sequences:\", len(sequences))\n",
        "\n",
        "# ============================================================\n",
        "# STEP 4: VECTORIZE\n",
        "# ============================================================\n",
        "print(\"\\nSTEP 4: Vectorizing...\")\n",
        "\n",
        "X = np.zeros((len(sequences), SEQ_LENGTH, vocab_size), dtype=np.bool_)\n",
        "y = np.zeros((len(sequences), vocab_size), dtype=np.bool_)\n",
        "\n",
        "for i, seq in enumerate(sequences):\n",
        "    for t, char in enumerate(seq):\n",
        "        X[i, t, char_to_idx[char]] = 1\n",
        "    y[i, char_to_idx[next_chars[i]]] = 1\n",
        "\n",
        "print(\"X shape:\", X.shape)\n",
        "print(\"y shape:\", y.shape)\n",
        "\n",
        "# ============================================================\n",
        "# STEP 5: BUILD MODEL\n",
        "# ============================================================\n",
        "print(\"\\nSTEP 5: Building LSTM Model\")\n",
        "\n",
        "model = Sequential([\n",
        "    LSTM(128, input_shape=(SEQ_LENGTH, vocab_size)),\n",
        "    Dense(vocab_size, activation='softmax')\n",
        "])\n",
        "\n",
        "model.compile(\n",
        "    loss='categorical_crossentropy',\n",
        "    optimizer='adam'\n",
        ")\n",
        "\n",
        "model.summary()\n",
        "\n",
        "# ============================================================\n",
        "# STEP 6: HELPER FUNCTION\n",
        "# ============================================================\n",
        "def sample(preds, temperature=1.0):\n",
        "    preds = np.asarray(preds).astype('float64')\n",
        "    preds = np.log(preds + 1e-10) / temperature\n",
        "    exp_preds = np.exp(preds)\n",
        "    preds = exp_preds / np.sum(exp_preds)\n",
        "    return np.argmax(np.random.multinomial(1, preds, 1))\n",
        "\n",
        "def generate_text(seed_text, length=300, temperature=0.5):\n",
        "    generated = seed_text\n",
        "    for _ in range(length):\n",
        "        x_pred = np.zeros((1, SEQ_LENGTH, vocab_size))\n",
        "        for t, char in enumerate(seed_text):\n",
        "            if char in char_to_idx:\n",
        "                x_pred[0, t, char_to_idx[char]] = 1\n",
        "        preds     = model.predict(x_pred, verbose=0)[0]\n",
        "        next_idx  = sample(preds, temperature=temperature)\n",
        "        next_char = idx_to_char[next_idx]\n",
        "        generated += next_char\n",
        "        seed_text  = seed_text[1:] + next_char\n",
        "    return generated[SEQ_LENGTH:]\n",
        "\n",
        "# ============================================================\n",
        "# STEP 7: TRAIN MODEL\n",
        "# ============================================================\n",
        "print(\"\\nSTEP 6: Training Model...\")\n",
        "\n",
        "class TextGenerator(tf.keras.callbacks.Callback):\n",
        "    def on_epoch_end(self, epoch, logs=None):\n",
        "        if (epoch + 1) % 5 == 0:\n",
        "            print(\"\\n--- Text after epoch\", epoch + 1, \"---\")\n",
        "            start_idx = random.randint(0, len(text) - SEQ_LENGTH - 1)\n",
        "            seed      = text[start_idx: start_idx + SEQ_LENGTH]\n",
        "            result    = generate_text(seed, length=200, temperature=0.5)\n",
        "            print(result)\n",
        "            print(\"-\" * 50)\n",
        "\n",
        "history = model.fit(\n",
        "    X, y,\n",
        "    batch_size=128,\n",
        "    epochs=30,\n",
        "    callbacks=[\n",
        "        EarlyStopping(monitor='loss', patience=5, restore_best_weights=True),\n",
        "        TextGenerator()\n",
        "    ]\n",
        ")\n",
        "\n",
        "# ============================================================\n",
        "# STEP 8: PLOT TRAINING LOSS\n",
        "# ============================================================\n",
        "print(\"\\nSTEP 7: Training Loss\")\n",
        "\n",
        "plt.figure(figsize=(8, 5))\n",
        "plt.plot(history.history['loss'], color='steelblue', linewidth=2)\n",
        "plt.title('Model Training Loss')\n",
        "plt.xlabel('Epoch')\n",
        "plt.ylabel('Loss')\n",
        "plt.grid(True)\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ============================================================\n",
        "# STEP 9: GENERATE TEXT\n",
        "# ============================================================\n",
        "print(\"\\nSTEP 8: Generating Text with Different Temperatures\")\n",
        "\n",
        "start_idx = random.randint(0, len(text) - SEQ_LENGTH - 1)\n",
        "seed      = text[start_idx: start_idx + SEQ_LENGTH]\n",
        "\n",
        "print(\"\\nSEED TEXT:\")\n",
        "print(seed)\n",
        "print(\"=\" * 50)\n",
        "\n",
        "for temp in [0.3, 0.5, 0.8]:\n",
        "    print(\"\\nTemperature:\", temp)\n",
        "    print(\"-\" * 50)\n",
        "    result = generate_text(seed, length=300, temperature=temp)\n",
        "    print(result)\n",
        "    print(\"-\" * 50)\n",
        "\n",
        "# ============================================================\n",
        "# STEP 10: SAVE MODEL\n",
        "# ============================================================\n",
        "print(\"\\nSTEP 9: Saving Model\")\n",
        "model.save('/content/rnn_text_model.h5')\n",
        "print(\"Model saved!\")\n",
        "\n",
        "print(\"\\nALL DONE! Character-level RNN Text Generation complete.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 957
        },
        "id": "Iq8ZUmKzF6bY",
        "outputId": "76617e41-6e81-46c1-b796-a1cc302e7281"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "STEP 1: Loading Dataset\n",
            "Total characters: 200000\n",
            "Sample text:\n",
            " First Citizen:\n",
            "Before we proceed any further, hear me speak.\n",
            "\n",
            "All:\n",
            "Speak, speak.\n",
            "\n",
            "First Citizen:\n",
            "You are all resolved rather to die than to famish?\n",
            "\n",
            "All:\n",
            "Resolved. resolved.\n",
            "\n",
            "First Citizen:\n",
            "First, you know Caius Marcius is chief enemy to the people.\n",
            "\n",
            "All:\n",
            "We know't, we know't.\n",
            "\n",
            "First Citizen:\n",
            "Let us\n",
            "\n",
            "STEP 2: Preparing Character Mappings\n",
            "Total unique characters: 62\n",
            "Mapping done!\n",
            "\n",
            "STEP 3: Creating Sequences\n",
            "Total sequences: 66634\n",
            "\n",
            "STEP 4: Vectorizing...\n",
            "X shape: (66634, 100, 62)\n",
            "y shape: (66634, 62)\n",
            "\n",
            "STEP 5: Building LSTM Model\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1mModel: \"sequential\"\u001b[0m\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Model: \"sequential\"</span>\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓\n",
              "┃\u001b[1m \u001b[0m\u001b[1mLayer (type)                   \u001b[0m\u001b[1m \u001b[0m┃\u001b[1m \u001b[0m\u001b[1mOutput Shape          \u001b[0m\u001b[1m \u001b[0m┃\u001b[1m \u001b[0m\u001b[1m      Param #\u001b[0m\u001b[1m \u001b[0m┃\n",
              "┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩\n",
              "│ lstm (\u001b[38;5;33mLSTM\u001b[0m)                     │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m128\u001b[0m)            │        \u001b[38;5;34m97,792\u001b[0m │\n",
              "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
              "│ dense (\u001b[38;5;33mDense\u001b[0m)                   │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m62\u001b[0m)             │         \u001b[38;5;34m7,998\u001b[0m │\n",
              "└─────────────────────────────────┴────────────────────────┴───────────────┘\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓\n",
              "┃<span style=\"font-weight: bold\"> Layer (type)                    </span>┃<span style=\"font-weight: bold\"> Output Shape           </span>┃<span style=\"font-weight: bold\">       Param # </span>┃\n",
              "┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩\n",
              "│ lstm (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">LSTM</span>)                     │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">128</span>)            │        <span style=\"color: #00af00; text-decoration-color: #00af00\">97,792</span> │\n",
              "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
              "│ dense (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Dense</span>)                   │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">62</span>)             │         <span style=\"color: #00af00; text-decoration-color: #00af00\">7,998</span> │\n",
              "└─────────────────────────────────┴────────────────────────┴───────────────┘\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1m Total params: \u001b[0m\u001b[38;5;34m105,790\u001b[0m (413.24 KB)\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\"> Total params: </span><span style=\"color: #00af00; text-decoration-color: #00af00\">105,790</span> (413.24 KB)\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1m Trainable params: \u001b[0m\u001b[38;5;34m105,790\u001b[0m (413.24 KB)\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\"> Trainable params: </span><span style=\"color: #00af00; text-decoration-color: #00af00\">105,790</span> (413.24 KB)\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1m Non-trainable params: \u001b[0m\u001b[38;5;34m0\u001b[0m (0.00 B)\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\"> Non-trainable params: </span><span style=\"color: #00af00; text-decoration-color: #00af00\">0</span> (0.00 B)\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "STEP 6: Training Model...\n",
            "Epoch 1/30\n",
            "\u001b[1m521/521\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m144s\u001b[0m 271ms/step - loss: 2.9994\n",
            "Epoch 2/30\n",
            "\u001b[1m521/521\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m141s\u001b[0m 270ms/step - loss: 2.4033\n",
            "Epoch 3/30\n",
            "\u001b[1m200/521\u001b[0m \u001b[32m━━━━━━━\u001b[0m\u001b[37m━━━━━━━━━━━━━\u001b[0m \u001b[1m1:24\u001b[0m 264ms/step - loss: 2.2737"
          ]
        }
      ]
    }
  ]
}