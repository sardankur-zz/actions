import json
from random import randint
import string

def transform(fromFile, toFile):
    with open(fromFile) as data_file:
        data = json.load(data_file)

    f = open(toFile, 'w');

    # i = randint(0,50000)
    i = randint(50000, 80000)
    j = 200
    punctuation = """!"#$%&'()*+,-./:;<=>@[\]^_`{|}~"""
    translator = str.maketrans({key: None for key in punctuation})

    while j != 0:
        dataItem = data[i];
        if i % 2 == 0 or i % 3 == 0:
            question = dataItem["question"].lower().replace("...", " ")
            question = question.translate(translator)
            if len(question) < 200:
                f.write("Q" + "\t" + question + "\n");
        else:
            answer = dataItem["answer"].lower().replace("...", " ")
            answer = answer.translate(translator)
            if len(answer) < 200:
                f.write("A" + "\t" + answer + "\n");
        j -= 1;
        # i = randint(0, 50000)
        i = randint(50000, 80000)
    f.close()

transform('data/nfL6.json', 'data/interrogative_test3.txt');