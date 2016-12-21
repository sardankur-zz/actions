from flask import Flask, request, Response
from flask_cors import cross_origin
import classifier
import json

app = Flask(__name__)

clf_1 = None
clf_2 = None
clf_3 = None


@app.route("/parse_and_classify", methods=['POST'])
@cross_origin()
def parse_and_classify():
    if 'data' in request.form and request.form['data'] != None:
        input_d = request.form['data']
        output_d = classifier.classify(input_d, clf_1, clf_2, clf_3)
        return Response(json.dumps(output_d, ensure_ascii=False), mimetype='application/json')
    else:
        return None

@app.route("/get_parse_and_classify", methods=['POST'])
@cross_origin()
def get_parse_and_classify():
    if request.data != None:
        input_d = request.data.decode("utf-8")
        output_d = classifier.remove_unwanted_text(input_d, clf_1, clf_2, clf_3)
        return Response(json.dumps(output_d, ensure_ascii=False), mimetype='application/json')
    else:
        return None

if __name__ == "__main__":
    clf_1, clf_2, clf_3 = classifier.build_classifier()
    app.run()

