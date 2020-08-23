# ML-app 
## Housing prediction app for deployment in Heroku cloud platform
Data science project to predict the housing prices using a linear regression model.
There are multiple steps involved which are also called as pipelines. Few of the pipelines used during this project are:
>1. Preprocessing of data using numpy, pandas.
>2. Visualizing of data to find correlation between features using matplotlib.
>3. Hyperparameter tuning using scikit learn
>4. Serialization of model using pickle
>5. Creation of a web app using flask
>6. Configuration of Heroku account and connecting it with Github
>7. Preparing the necessary configuration files and finally deployment of web app in Heroku platform

### The app can be launched by clicking the link [here](https://house-price-pred-app.herokuapp.com/)
The app takes 4 inputs:
1. `Desired Sqft`
2. `Location` (The list of location can be got from this [link](https://house-price-pred-app.herokuapp.com/get_location_names))
3. `Bedrooms`
4. `Bathrooms`

Upon clicking on the `Predict` button, the app can make a price prediction of the house in currency (INR)

#### *Coding Language used: Python 3.8.3 (Pandas, Numpy, Matplotlib, Scikit Learn, Flask)*
#### *IDE used: Jupyter Notebook, Pycharm Edu*
References - 
*Youtube Channels (Corey Schafer, Tech with Tim, Codebasics & Krish Naik)

*Books (Handson Machine Learning with Scikit Learn)
