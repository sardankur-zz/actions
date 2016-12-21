import sys
import dataset

def main(args):
    sentence = ""
    # swbd = dataset.Swbd();
    # swbd.extract();
    # pass
    # dataset.testprocess()

    # yahoo = dataset.yahoo_dataset();
    # yahoo.extract("data/amazon/qa_Appliances.json", "data/amazon/question_train4.txt", 6000, 0)
    # yahoo.extract("data/amazon/qa_Appliances.json", "data/amazon/question_test2.txt", 6000, 5500)

    illionis = dataset.illinois();
    illionis.extract("data/illinois/test.txt", "data/illinois/question_test1.txt", 0 , 0)


if __name__ == "__main__":
    main(sys.argv)