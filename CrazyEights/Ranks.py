class Ranks():
    __ranks = {"ACE": 1,
             "TWO": 2,
             "THREE": 3,
             "FOUR": 4,
             "FIVE": 5,
             "SIX": 6,
             "SEVEN": 7,
             "EIGHT": 50,
             "NINE": 9,
             "TEN": 10,
             "JACK": 10,
             "QUEEN": 10,
             "KING": 10}

    def getRanks(self):
        return self.__ranks

    def getNumOfRanks(self):
        return len(self.__ranks)