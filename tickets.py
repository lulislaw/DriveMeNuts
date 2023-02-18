import json

class Ticket:
    def __init__(self, num, text, suc, a1,a2,a3,a4,a5, image):
        self.num = num
        self.text = text
        self.suc = suc
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.image = image


def getBilet(numBilet):
    my_list = []
    for i in range(1,21):
        with open(f'src/bilets/json/bilet{numBilet}quest{i}.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
        pathimg = f'src/bilets/img/imgs{numBilet}bilet/image{i}.jpg'
        my_list.append(Ticket(data['nubmerQuest'],data['textQuest'],data['sucAns'],data['ans1'],data['ans2'],data['ans3'],data['ans4'],data['ans5'],pathimg))

    return my_list
print(getBilet(1)[0].image)