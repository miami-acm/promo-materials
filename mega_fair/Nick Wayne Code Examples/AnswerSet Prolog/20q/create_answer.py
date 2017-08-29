import re

def return_questions():
    f = open("questions.pl", "r")
    questions = []
    while True:
        x = f.readline()
        x = re.search("(\w+), \"(.+)\"", x)  # question((g1), (g2))
        if not x: break
        questions.append([x.group(1), x.group(2)])
    f.close()
    return questions

class answer(object):

    def __init__(self):
        self.name = ""
        self.type = ""
        self.questions = return_questions()
        self.answers = []
        self.interview()

    def interview(self):
        self.name = raw_input("what is the answer? ").lower()
        print "animal, vegetable, mineral, concept, unknown"
        self.type = raw_input("what is the type? ").lower()
        self.ask_questions()

    def ask_questions(self):
        for i in self.questions:
            print "1. Yes, 2. No, 3. Sometimes, 4. Rarely, 5. Unknown"
            temp = raw_input("%s "%(i[1]))
            self.answers.append([i[0], temp])

        self.output()

    def unwrap(self, num):
        return {
            "1": "yes",
            "2": "no",
            "3": "sometimes",
            "4": "rarely",
            "5": "unknown"
        }[num]


    def output(self):
        f = open("answers/%s.pl"%(self.name), "w")
        f.write("name(%s). \n"%(self.name))
        f.write("type(%s). \n" %(self.type))
        for i in self.answers:
            f.write("answer(%s, %s, %s). \n"%(self.name, i[0], self.unwrap(i[1])))
        f.close()


a = answer()



