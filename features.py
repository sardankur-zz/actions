from sklearn.feature_extraction.text import CountVectorizer


class QuestionMarkVectorizer(CountVectorizer):
    def __init__(self):
        super(QuestionMarkVectorizer, self)\
            .__init__(vocabulary=['?'],
                      ngram_range=(1,1),
                      binary=True,
                      analyzer='char')
