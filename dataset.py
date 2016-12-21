import collections
import re
import preprocess
from nltk.tokenize import sent_tokenize

def get_data(file, delimiter='\t'):
    f = open(file, 'r')
    data = []
    for line in f:
        data.append(line.split(delimiter))
    return data

def extract_list(data, index):
    if isinstance(index, collections.Sequence):
        return [[item[idx] for idx in index] for item in data]
    else:
        return [item[index] for item in data]

def extract_dict(data, indexKey, indexVal):
    dict = {}
    for item in data:
        dict[item[indexKey]] = item[indexVal]
    return dict

def print_matrix(vectorizer, data) :
    print(vectorizer.fit_transform(data).toarray())

from os import listdir
from os.path import isfile, join

class Swbd:
    # tags to extract
    # qy
    # qw
    # qy^d
    # bh
    # ad
    # qo
    # qh
    # fp
    # qr
    # qrr
    # ^g
    # qw^d

    def contains(self, text):
        question_set = ['qy', 'qw', 'qy^d', 'bh', 'ad', 'qo',
                        'qh', 'fp', 'qr', 'qrr', '^g', 'qw^d']
        test = False
        for item in question_set:
            if item  == text:
                test = True
            else :
                try:
                    text.index(item)
                    test = True
                except ValueError:
                    pass
        return test

    def extract(self):
        f = open("data/swbd/swbd_1.txt", 'r')
        raw_data = []
        i = 1
        question_set = set()
        for line in f:
            split = line.split("\t");
            if self.contains(split[0]):
                text = re.sub('\{.*\}|\[.*\]|<.*>', '', split[1])
                raw_data.append(split[0] + '\t' + text)

        with open('data/swbd/swbd_2.txt', mode='wt', encoding='utf-8') as myfile:
            for data in raw_data:
                myfile.write(data)


    def rich(self):
        f = open("data/swbd/swbd.txt", 'r')
        raw_data = []
        i = 1
        for line in f:
            print(i)
            i = i +1
            split = line.split("          ", 1);
            tag = split[0];
            text = split[1];
            text = text.replace("/", "")
            text = text.strip();
            text = text.split(":")[1].strip();
            raw_data.append([tag, text])

        with open('data/swbd/swbd_1.txt', mode='wt', encoding='utf-8') as myfile:
            for data in raw_data:
                myfile.write(data[0] + "\t" + data[1] + "\n")




    def get_swbd_data(self, dir):
        i = 0;
        files = []
        data = []
        for i in range(0, 13):
            s = ""
            s = "0" + str(i) if i <= 9 else str(i)
            s = "sw" + s + "utt"
            filedir = dir + s
            files = listdir(filedir)
            total = []
            for file in files:
                new_raw_data = []
                if file != "words":
                    f = open(filedir + "/" + file, 'r')
                    raw_data = []
                    for line in f:
                        raw_data.append(line)
                    raw_data = raw_data[33:]

                    for data in raw_data:
                        if data != "\n":
                            new_raw_data.append(data.strip())
                total.extend(new_raw_data)
        with open(dir + '/swbd.txt', mode='wt', encoding='utf-8') as myfile:
            for item in total:
                myfile.write(item + "\n")

def testprocess():
    f = open("data/interrogative_train3.txt", "r");
    f2 = open("data/interrogative_train4.txt", "w");
    for line in f:
        lines = line.split("\t")
        tag = "O"
        if lines[0] == "A":
            tag = "-"
        f2.write(tag + "\t" + line)
    f2.close()
    f.close()

class yahoo_dataset:

    def parse(self, path):
        g = open(path, 'r')
        for l in g:
            yield eval(l)
        g.close()

    def extract(self, inFile, outFile, count, offset):

        f = open(outFile, 'w')

        j = 0
        opq = 0
        ynq = 0

        punctuation = """!"#$%&'()*+,-./:;<=>@[\]^_`{|}~"""
        translator = str.maketrans({key: None for key in punctuation})

        replacer = preprocess.SearchAndReplaceUrl()

        for l in self.parse(inFile):

            if (opq + ynq) > count:
                break

            if (l["questionType"] == "open-ended"):
                if(len(sent_tokenize(l["question"])) == 1) :
                    question = preprocess.PreProcess.transform(replacer, l["question"])
                    question = question.translate(translator)
                    if (len(question) < 150 and len(question) > 30):
                        if (opq + ynq) > offset:
                            f.write("OE\tQ\t" + question + "\n")
                        opq = opq + 1


            if (l["questionType"] == "yes/no"):
                if len(sent_tokenize(l["question"])) == 1:
                    question = preprocess.PreProcess.transform(replacer, l["question"])
                    question = question.translate(translator)
                    if (len(question) < 150 and len(question) > 30):
                        if (opq + ynq) > offset:
                            f.write("YN\tQ\t" + question + "\n")
                        ynq = ynq + 1

            if len(sent_tokenize(l["answer"])) == 1:
                answer = preprocess.PreProcess.transform(replacer, l["answer"])
                answer = answer.translate(translator)
                if (len(answer) < 150 and len(answer) > 30):
                    f.write("-\tA\t" + answer + "\n")

        f.close()

class illinois:

    def extract(self, inFile, outFile, count, offset):


        d_type = {
            "LOC:city" : "L",
            "LOC:country": "L",
            "LOC:mount": "L",
            "LOC:other": "L",
            "LOC:state": "L",
            "NUM:date" : "D",
            "NUM:count" : "N",
            "NUM:code" : "N",
            "NUM:dist": "N",
            "NUM:money": "N",
            "NUM:ord": "N",
            "NUM:other": "N",
            "NUM:perc": "N",
            "NUM:period": "N",
            "NUM:speed": "N",
            "NUM:temp": "N",
            "NUM:volsize": "N",
            "NUM:weight": "N"
        }

        types = {
            "D" : "DT",
            "L" : "LOC",
            "N" : "NUM",
            "T" : "FT"
        }

        f = open(outFile, 'w')
        fin = open(inFile, 'r')
        data = {}
        for line in fin:
            split = line.split(":", 1)
            type = split[0]
            split2 = split[1].split(" ", 1)
            type = type + ":" + split2[0]
            sent = split2[1]


            if type not in data :
                data[type] = []

            data[type].append(sent)

        for key in data:
            sentences = data[key]
            for item in sentences:
                if key in d_type:
                    datatype = d_type[key]
                    datatype = types[datatype]
                else :
                    datatype = "FT"
                f.write(datatype + "\tT\tQ\t" + item)

        pass