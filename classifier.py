import dataset
import features
import talon
from talon import signature
from talon import quotations
from sklearn.pipeline import Pipeline, FeatureUnion
from preprocess import PreProcess, Strip, RemoveQuestionMark, SingatureRemoval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import sent_tokenize

punctuation = """!"#$%&'()*+,-./:;<=>@[\]^_`{|}~"""
translator = str.maketrans({key: None for key in punctuation})

talon.init()

def build_classifier() :

    trainFile_1 = "../data/amazon/question_train1.txt"

    train_1 = dataset.get_data(trainFile_1)
    trainData_1 = dataset.extract_list(train_1, 2)

    trainTarget_1 = dataset.extract_list(train_1, 1)

    # PreProcess.chain_transform([Strip(), RemoveQuestionMark()], trainData)
    PreProcess.chain_transform([Strip()], trainData_1)

    transformers_1 = [
        ('count', CountVectorizer(ngram_range=(1, 3)), 1),
        ('question_mark', features.QuestionMarkVectorizer(), 20)
    ]

    clf_1 = Pipeline([
        ('feature_union', FeatureUnion(transformer_list=dataset.extract_list(transformers_1, [0, 1]),
                                       transformer_weights=dataset.extract_dict(transformers_1, 0, 2))),
        ('multinomial', MultinomialNB()
         # ('svm', SVC()
         # ('tree', tree.DecisionTreeClassifier()
         )
    ]).fit(trainData_1, trainTarget_1)

    trainFile_2 = "../data/amazon/question_train2.txt"

    train_2 = dataset.get_data(trainFile_2)
    trainData_2 = dataset.extract_list(train_2, 2)

    trainTarget_2 = dataset.extract_list(train_2, 0)

    transformers_2 = [
        ('count', CountVectorizer(ngram_range=(1, 3)), 1)
    ]

    clf_2 = Pipeline([
        ('feature_union', FeatureUnion(transformer_list=dataset.extract_list(transformers_2, [0, 1]),
                                       transformer_weights=dataset.extract_dict(transformers_2, 0, 2))),
        ('multinomial', MultinomialNB()
         # ('svm', SVC()
         # ('tree', tree.DecisionTreeClassifier()
         )
    ]).fit(trainData_2, trainTarget_2)

    trainFile_3 = "../data/illinois/question_train1.txt"

    train_3 = dataset.get_data(trainFile_3)
    trainData_3 = dataset.extract_list(train_3, 3)
    trainTarget_3 = dataset.extract_list(train_3, 0)

    PreProcess.chain_transform([Strip(), RemoveQuestionMark()], trainData_3)

    transformers_3 = [
        ('count', CountVectorizer(ngram_range=(1, 3)), 1)
    ]

    clf_3 = Pipeline([
        ('feature_union', FeatureUnion(transformer_list=dataset.extract_list(transformers_3, [0, 1]),
                                       transformer_weights=dataset.extract_dict(transformers_3, 0, 2))),
        ('multinomial', MultinomialNB()
         # ('svm', SVC()
         # ('tree', tree.DecisionTreeClassifier()
         )
    ]).fit(trainData_3, trainTarget_3)

    return clf_1, clf_2, clf_3

def get_classifier() :
    pass


def remove_unwanted_text(string, a, b, c):
    string1 = signature.extract(string)
    string2 = quotations.extract_from(string)
    return string




def classify(input_d, clf_1, clf_2, clf_3) :
    input_d = PreProcess.transform(SingatureRemoval(), input_d)
    input_d = sent_tokenize(input_d)

    output_d = []
    predict = ""
    for sentence in input_d:
            sentence = PreProcess.transform(Strip(), sentence)
            ele = {}
            predict_1 = clf_1.predict([sentence])[0]
            if predict_1 == 'Q':
                predict_2 = clf_2.predict([sentence])[0]
                if predict_2 == 'OE':
                    predict_3 = clf_3.predict([sentence])[0]
                    predict = predict_3
                else:
                    predict = predict_2
            else :
                predict = predict_1

            ele["type"] = predict
            ele["label"] = sentence
            output_d.append(ele)
    return output_d