import gensim
from flask import jsonify
from flask import render_template, request

import evaluate
import utils
from text_manipulation import split_sentences
from webapp import app

if utils.config['test']:
    word2vec = None
else:
    word2vec = gensim.models.KeyedVectors.load_word2vec_format(utils.config['word2vecfile'], binary=True)

model = evaluate.load_model()


def treat_text(raw_text):
    sentences = split_sentences(raw_text, 1234)
    print(sentences)

    cutoffs = evaluate.predict_cutoffs(sentences, model, word2vec)
    total = []
    segment = []
    for i, (sentence, cutoff) in enumerate(zip(sentences, cutoffs)):
        segment.append(sentence)
        if cutoff:
            total.append(segment)
            segment = []

    return total


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    segmentation = treat_text(request.form['Text'])
    print(segmentation)
    return render_template('result.html', segmentation=segmentation)


@app.route('/get_segments', methods=['POST'])
def get_segments():
    data_json = request.get_json(force=True)
    segmentation = treat_text(data_json['text'])
    print(segmentation)

    out_dict = {}
    for segment in range(len(segmentation)):
        out_dict[segment] = segmentation[segment]

    return jsonify(out_dict)
