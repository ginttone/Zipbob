import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import random
import pickle
import json
from tensorflow.python.framework import ops

nltk.download('punkt')

# 집밥 json 데이터를 data로 로드시키기
# json 경로 설정하기 :
# 전체 서버 실행시킬 때 ML/ 경로를 추가한다.
with open('ML/Zipbob_chatbotdata.json', encoding='UTF8') as file:
    # with open('Zipbob_chatbotdata.json',  encoding='UTF8') as file:
    data = json.load(file)

# # -----------------------------------------------------
# # 시작 : 실행 안 해도 되는 부분
# # -----------------------------------------------------
# try:
#     with open("data.pickle", "rb") as f:
#         words, labels, training, output = pickle.load(f)
# except:
#     words = []
#     labels = []
#     docs_x = []
#     docs_y = []
# for intent in data['intents']:
#     for pattern in intent['patterns']:
#         wrds = nltk.word_tokenize(pattern)
#         words.extend(wrds)
#         docs_x.append(wrds)
#         docs_y.append(intent["tag"])
#
#     if intent['tag'] not in labels:
#         labels.append(intent['tag'])
#
# words = [stemmer.stem(w.lower()) for w in words if w != "?"]
# words = sorted(list(set(words)))
# labels = sorted(labels)
# training = []
# output = []
#
# out_empty = [0 for _ in range(len(labels))]
#
# for x, doc in enumerate(docs_x):
#     bag = []
#     wrds = [stemmer.stem(w.lower()) for w in doc]
#
#     for w in words:
#         if w in wrds:
#             bag.append(1)
#         else:
#             bag.append(0)
#
#     output_row = out_empty[:]
#     output_row[labels.index(docs_y[x])] = 1
#     training.append(bag)
#     output.append(output_row)
#
# training = numpy.array(training)
# output = numpy.array(output)
#
# ops.reset_default_graph()
#
# net = tflearn.input_data(shape=[None, len(training[0])])
# net = tflearn.fully_connected(net, 8)
# net = tflearn.fully_connected(net, 8)
# net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
# net = tflearn.regression(net)
#
# model = tflearn.DNN(net)
# model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
# model.save("model.tflearn")
# # -----------------------------------------------------
# # 끝 : pickle로 저장하여 실행 안 해도 되는 부분
# # -----------------------------------------------------

## 피클 불러오기
with open("ML/Zipbobchat.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)

ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

# 전체 Zipbob 폴더 밑에 checkpoint, model.tflearn등 파일 있는 것 확인되면 정상
# # -----------------------------------------------------
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


def chat(usersentence):
    while True:
        inp = usersentence
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
                print(responses)

        if len(responses) != 0:
            break
    print(random.choice(responses))

    return random.choice(responses)


if __name__ == '__main__':
    chat("안녕")
