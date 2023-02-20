import PCA
import pandas as pd
import numpy as np

def normalize(df) -> pd.DataFrame:
    df = df.copy()
    num_types = dict(X_train.dtypes != 'O')
    numbers = [var for var, is_numeric in num_types.items() if is_numeric == True]
    for num in numbers:
        num_mean = df[num].mean()
        num_std = df[num].std()
        df[num] = round((df[num] - num_mean) / num_std, 6)
    return df

X = pd.DataFrame(PCA.finalReducedDataset)
X_train = X.iloc[:, 1:101]
labels = X[0]
labels = np.array(labels)

X_train_normal = np.array(normalize(X_train))
FinalNormalizedDataset = np.concatenate((labels.reshape(42000, 1), X_train_normal), axis=1)

