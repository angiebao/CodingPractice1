import numpy as np
import random
def split(data, ratio):

    #randomNumber = np.rand(1, len(data))
    random.shuffle(data)
    split = int(len(data) * ratio)

    data = np.array(data)

    train = data[:split, :]
    test =  data[split:, :]
    return train, test, data

data = [ [1,2,3,4,5],
        [5,6,7,8,9],
        [1,2,3,4,5],
        [5,6,7,8,9],
        [1,2,3,4,5],
        [5,6,7,8,9],
        [1,2,3,4,5],
        [5,6,7,8,9]]

train, test, data = split(data,0.7)
print(data, '\n')
print(train, '\n')
print(test, '\n')

randomNumber0 = np.random.randint(8, size=(8,1))
print('random0',randomNumber0,'\n')
data0 = np.concatenate((data, randomNumber0), axis=1)
print('data0',data0, '\n')

randomNumber1 = np.random.randint(8, size=8)
print('random1',randomNumber1)

randomNumber2 = np.random.randint(8, size=(1,8))
print('random2',randomNumber2)

randomNumber3 = [2,3,4,5,6,7,8,1]
randomNumber3 = np.expand_dims(randomNumber3, axis=1)
print('random3',randomNumber3, '\n')
data2 = np.concatenate((data, randomNumber3), 1)
print('data2',data2, '\n')


