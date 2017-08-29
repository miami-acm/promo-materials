import random
import re
import subprocess

class akinator(object):
    def __init__(self):
        self.questions = self.return_questions()
        self.answers = []
        self.num_questions = 9
        self.numbers = []
        for i in range(5):
            done = False
            while not done:
                temp = random.randint(1, self.num_questions)
                if self.questions[temp - 1] not in self.numbers:
                    self.numbers.append(self.questions[temp - 1])
                    done = True
        self.questions = self.numbers
        print self.questions
        self.queries()

    def unwrap(self, num):
        return {
            "1": "yes",
            "2": "no",
            "3": "sometimes",
            "4": "rarely",
            "5": "unknown"
        }[num]

    def queries(self):
        for i in self.questions:
            print "1. Yes, 2. No, 3. Sometimes, 4. Rarely, 5. Unknown"
            temp = raw_input(i[1])
            self.answers.append([i[0], self.unwrap(temp)])
        self.add_rules()
        print self.answers

    def add_rules(self):
        f = open("20q.pl", "w")
        f.write("response(unknown). \n")
        f.write("response(rarely). \n")
        f.write("response(no). \n")
        f.write("response(yes). \n")
        f.write("response(sometimes). \n\n")
        f.write("types(animal). \n")
        f.write("types(vegetable). \n")
        f.write("types(mineral). \n")
        f.write("types(concept). \n")
        f.write("types(unknown). \n\n")
        for i in self.answers:
            f.write("ans(%s, %s). \n"%(i[0], i[1]))
        f.write("\namount(X, Y) :- name(X), #count{Q : ans(Q, A), answer(X, Q, A)} = Y. \n")
        f.close()
        self.akinate()

    def akinate(self):
        self.answer_sets = subprocess.check_output("dlv *.pl answers\*.pl -silent -filter=amount")
        self.responses = re.findall("(\(\w+,\d\))", self.answer_sets)
        # for i in self.responses:
        #     self.responses[self.responses.index(i)] = eval(i)
        # print self.responses

        #TODO - print the winner / get the regex working

    def return_questions(self):
        f = open("questions.pl", "r")
        questions = []
        while True:
            x = f.readline()
            x = re.search("(\w+), \"(.+)\"", x)  # question((g1), (g2))
            if not x: break
            questions.append([x.group(1), x.group(2)])
        f.close()
        return questions


ak = akinator()
