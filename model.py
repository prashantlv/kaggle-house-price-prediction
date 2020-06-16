
def train_model(X,Y):
    import tensorflow as tf 
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Input, Dense, Dropout, Activation
    from tensorflow.keras.optimizers import Adam
    from tensorflow.keras.losses import MSE
    import pandas as pd

    # from sklearn.preprocessing import StandardScaler
    # sc=StandardScaler()

    # X = sc.fit_transform(X)
    # Y = sc.fit_transform(Y)
    # print('before dummies')
    X = pd.get_dummies(X)
    print('Printing dummies shape....', X.shape)

    model =Sequential([
        Dense(124, input_shape =(838,)),
        Dense(124, activation = 'relu'),
        Dropout(0.3),
        Dense(62, activation = 'relu'),
        Dropout(0.3),
        Dense(32, activation = 'relu'),
        Dropout(0.2),
        Dense(1)
        ])

    model.compile(
        optimizer='adam',  
        loss = 'mse',
        metrics= ['accuracy']
    )

    r = model.fit(X, Y, epochs = 140, validation_split=0.2)
