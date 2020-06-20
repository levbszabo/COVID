import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
data = pd.read_csv("coronavirus_data/coronavirus2.csv")
import pickle
def poly_reg(location):     #simple poly regression to implement on flask and heroku
    if location == "All":
        dat = data
    else:
        dat = data[(data["Province/State"] == location)|
                   (data["Country/Region"]==location) |
                   (data["City"]==location)]
    time_series= np.sum(dat)[5:].astype(int)
    n = len(time_series)
    x = np.arange(n).reshape(n,1)
    x_test = np.arange(14).reshape(14,1)+n
    model = make_pipeline(PolynomialFeatures(degree=2),LinearRegression(fit_intercept=False))
    model.fit(x,time_series)
    #print(model.named_steps.linearregression.coef_)
    predict = model.predict(x_test)
    return predict[-1]
    #plt.figure(figsize=(4,4))
    #plt.plot(x,time_series,'ro')
    #plt.plot(x_test,predict)
    #plt.savefig("fig1")