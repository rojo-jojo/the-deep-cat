# import the libs
import math
import logging
logging.getLogger().setLevel(logging.INFO)
# init the vars
import numpy as np


def create_data(filepath):
    with open(filepath, 'r') as f:
        data_list = f.read().splitlines()
    x, y = [], []
    for record in data_list:
        x.append(record.split(', ')[:2])
        y.append(float(record.split(', ')[2]))
    return x,y, len(y)


def sigmoid(x):
    return 1/(1+math.exp(-x))

def loss(y, y_hat):
    return (y*math.log(y_hat) + (1-y)*math.log(1-y_hat))

def training(w1=0, w2=0, b=0):
    lr = 0.000003
    x, y, m = create_data('dataset_inp.txt')

    #x = np.array(x).reshape(m,-1)
    #y = np.array(x).reshape(m,-1)
    j = 0
    z = [0]*m #np.zeros(m)
    a = [0]*m #np.zeros(m)
    dz = [0]*m
    dw1, dw2, db = 0,0,0
    loss_term = 0
    print("m is: ",m)
    for i in range(0, m):
        z[i] = w1*float(x[i][0]) + w2*float(x[i][1]) + b
        a[i] = sigmoid(z[i])
        try:
            loss_term = loss(y[i], a[i])
        except ValueError as e:
            logging.info(f'log error was raised at index: {i}')
            break
        j += (-loss_term)

        dz[i] = a[i] - y[i]
        dw1 += dz[i] * float(x[i][0])
        dw2 += dz[i] * float(x[i][1])
        db += dz[i]
    
    j /= m
    dw1 /= m
    dw2 /= m
    db /= m
    # Gradient descent
    w1 = w1 - lr*dw1
    w2 = w2 - lr*dw2
    b = b - lr*db
    return w1, w2, b

def main():
    epochs = 100000
    w1, w2, b = 0,0,0
    for i in range(0,epochs):
        w1, w2, b = training(w1, w2, b)
        logging.info(f"{w1},{w2},{b}")

if __name__ == '__main__':
    main()



