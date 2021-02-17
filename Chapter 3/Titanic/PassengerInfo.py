# Format:
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
class PassengerInfo:
    def __init__(self, infoList):
        # self.infoList = infoList
        self.id = infoList[0]
        self.survived = infoList[1]
        self.pClass = infoList[2]
        self.name = infoList[3]
        self.sex = 0 if (infoList[4] == "male") else 1      # self.sex = (infoList[4] == "male") ? 0 : 1
        self.sibsp = infoList[5]
        self.parch = infoList[6]
        self.ticket = infoList[7]
        self.fare = infoList[8]
        self.cabin = infoList[9]
        self.embarked = infoList[10]        # Needs to change to 1, 2, 3

        if (self.embarked == 'C'):
            self.embarked = 1
        elif (self.embarked == 'Q'):
            self.embarked = 2
        else:
            self.embarked = 3
