import os

path=f'{os.path.dirname(os.path.realpath(__file__))}/data'

def readData():
    with open(path+'/card.csv', 'r') as f:
        data = f.readline()
        return data

def updateData(dataaa):
    with open(path+'/card.csv', 'w') as f:
        f.writelines(f'{dataaa}')

def dataMatch(dataaa):
    with open(path+'/card.csv', 'w') as f:
        if (dataaa != readData):
            f.writelines(f'{dataaa}')

# updateData('247 162 130 203')
# print(readData())