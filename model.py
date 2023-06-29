import http_request
import pandas
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error


def get_prediction():
    params = http_request.get_response()

    wind_speed=params['current']['wind_speed']
    temperature = params['current']['temperature']
    precip = params['current']['precip']
    humidity = params['current']['humidity']


    sample = [[temperature,humidity,wind_speed,precip]]
    df = pandas.read_csv("forestfirex.csv")
    df1 = pandas.read_csv("forestfirex1.csv")


    features = ['temp', 'RH', 'wind', 'rain']

    X = df[features]
    y = df1['area']


    extratree = ExtraTreesRegressor()
    extratree = extratree.fit(X,y)
    pred = extratree.predict(X)
    
    
    output = extratree.predict(sample)
    if (output[0]<=10):
        return (["nil",temperature,wind_speed,precip,humidity])


    elif(output[0]>10 and output<60):
        return (["Mild",temperature,wind_speed,precip,humidity])

    elif (output[0]>60 and output[0]<120):
        return (["Good",temperature,wind_speed,precip,humidity])

    else:
        return (["high",temperature,wind_speed,precip,humidity])

