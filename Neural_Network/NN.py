import matplotlib.pyplot as plt
import numpy as np
import Normalize

#INTIALIZE DATASET
data = Normalize.FinalNormalizedDataset.astype(int)
m, n = data.shape
data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]

#RELU ACTIVATION
def ReLU(Z):
    return np.maximum(Z,0)

#ReLU DERIVATIVE
def derivative_ReLU(Z):
    return Z > 0

#SOFTMAX ACTIVATION
def softmax(Z):
    exp = np.exp(Z - np.max(Z))
    return exp / exp.sum(axis=0)

#INITIALIZE 2 WEIGHT AND BIAS MATRICES
def init_params():
    W1 = np.random.rand(10,100) - 0.5
    b1 = np.random.rand(10,1) - 0.5
    W2 = np.random.rand(10,10) - 0.5
    b2 = np.random.rand(10,1) - 0.5
    return W1,b1,W2,b2

#COMPUTE VALUES FOR FORWARD PROPAGATION
def forward_propagation(X,W1,b1,W2,b2):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

#CREATE A 0 MATRIX with 1 when position corresponds to the ground truth
def one_hot(Y):
    one_hot_Y = np.zeros((Y.max()+1, Y.size))
    one_hot_Y[Y,np.arange(Y.size)] = 1
    return one_hot_Y

def backward_propagation(X, Y, A1, A2, W2, Z1, m):
    one_hot_Y = one_hot(Y)
    dZ2 = (A2 - one_hot_Y)
    dW2 = 1/m * (dZ2.dot(A1.T))
    db2 = 1/m * np.sum(dZ2,1)
    dZ1 = W2.T.dot(dZ2)*derivative_ReLU(Z1)
    dW1 = 1/m * (dZ1.dot(X.T))
    db1 = 1/m * np.sum(dZ1,1)

    return dW1, db1, dW2, db2

def update_params(alpha, W1, b1, W2, b2, dW1, db1, dW2, db2):
    W1 -= alpha * dW1
    b1 -= alpha * np.reshape(db1, (10,1))
    W2 -= alpha * dW2
    b2 -= alpha * np.reshape(db2, (10,1))

    return W1, b1, W2, b2

def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    return np.sum(predictions == Y)/Y.size

def gradient_descent(X, Y, alpha, iterations):
    size , m = X.shape

    W1, b1, W2, b2 = init_params()
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_propagation(X, W1, b1, W2, b2)
        dW1, db1, dW2, db2 = backward_propagation(X, Y, A1, A2, W2, Z1, m)

        W1, b1, W2, b2 = update_params(alpha, W1, b1, W2, b2, dW1, db1, dW2, db2)

        if (i+1) % int(iterations/10) == 0:
            print(f"Iteration: {i+1} / {iterations}")
            prediction = get_predictions(A2)
            print(f'{get_accuracy(prediction, Y):.3%}')
    return W1, b1, W2, b2

W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 0.5, 500)


###VISUALIZE RESULTS AND CHECK ACCURACY

def predict(X, W1, b1, W2, b2):
    _, _, _, A2 = forward_propagation(X, W1, b1, W2, b2)
    predictions_test = get_predictions(A2)
    return predictions_test

def get_predictionAccuracy(index, W1, b1, W2, b2):
    image = X_train[:, index, None]
    prediction = predict(image, W1, b1, W2, b2)
    label = Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)

    image = image.reshape((10, 10))
    plt.gray()
    plt.imshow(image, interpolation='nearest')
    plt.show()

get_predictionAccuracy(300, W1, b1, W2, b2)
get_predictionAccuracy(250, W1, b1, W2, b2)
get_predictionAccuracy(7, W1, b1, W2, b2)
get_predictionAccuracy(77, W1, b1, W2, b2)



