class Ratata(object):
    def __init__(self, desc, owner, amount):
        self.desc = desc
        self.owner = owner
        self.amount = amount
        self.payers = []
        print("#1 Ratata created. Owner: {0} | Description: {1} | Amount: $ {2}".format(owner.name,desc,amount))

    def assignLeader(self, leader):
        self.leader = leader
        print("Leader assigned for #1 Ratata: {0}".format(leader.name))

    def addPayer(self, payer):
        self.payers.append(payer)
        print("Payer added for #1 Ratata: {0}".format(payer.name))

    def validatePayersBalance(self):
        paymentParticipants = 1 + len(self.payers)
        self.splittedAmount = self.amount / paymentParticipants
        # Leader
        if self.leader.balance >= self.splittedAmount:
            # Payers
            for payer in self.payers:
                if payer.balance < self.splittedAmount:
                    print("Ratata #1 error, payer {0} have not enough balance".format(payer.name))
                    return False
        else:
            print("Ratata #1 error, leader {0} have not enough balance".format(self.leader.name))
            return False
        print("Ratata #1 validated, all payers have enough balance")
        return True

    def transferWealth(self):
        # Leader
        self.leader.balance -= self.splittedAmount
        self.owner.balance += self.splittedAmount

        # Payers
        for payer in self.payers:
            payer.balance -= self.splittedAmount
            self.owner.balance += self.splittedAmount

class User(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

## MOCK
# Create Users
users = []
users_name = ["Jon", "Mike", "Bob"]
balance = 80

for user in users_name:
    users.append(User(user, balance))

for i in range(len(users)):
    print("{0}'s balance: $ {1}".format(users[i].name,users[i].balance))

# Create Ratata
desc = "Table 10"
owner = users[0]
amount = 162
ratata = Ratata(desc, owner, amount)
ratata.assignLeader(users[1])
ratata.addPayer(users[2])
if ratata.validatePayersBalance():
    ratata.transferWealth()

for i in range(len(users)):
    print("{0}'s balance: $ {1}".format(users[i].name,users[i].balance))
