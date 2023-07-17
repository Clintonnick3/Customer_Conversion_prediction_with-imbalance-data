# Customer_Conversion_prediction_with-imbalance-data
# **Problem Statement**:

You are working for a new-age insurance company and employ mutiple outreach plans to sell term insurance to your customers. Telephonic marketing campaigns still remain one of the most effective way to reach out to people however they incur a lot of cost. Hence, it is important to identify the customers that are most likely to convert beforehand so that they can be specifically targeted via call. We are given the historical marketing data of the insurance company and are required to build a ML model that will predict if a client will subscribe to the insurance.

# Data:

The historical sales data is available in below link

https://drive.google.com/file/d/1BJ_Q8Q-kDRisAQyLltBQggeb0QmdWGZy/view?usp=sharing

# Features:

age (numeric)

job : type of job (Object)

marital : marital status (Object)

educational_qual : education status (Object)

call_type : contact communication type (Object)

day: last contact day of the month (numeric)

mon: last contact month of year (Object)

dur: last contact duration, in seconds (numeric)

num_calls: number of contacts performed during this campaign and for this client (Object)

prev_outcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

Output variable (desired target):

y - has the client subscribed to the insurance?

# Minimum Requirements:

It is not sufficient to just fit a model - the model must be analysed to find the important factors that contribute towards the conversion rate. F1-Score must be used as a metric to evaluate the performance of the models.

# **Project Goal**:

The goal of the Customer Conversion Prediction project is to build a machine learning model that can predict whether a client will subscribe to the insurance based on their demographic and marketing data. The project aims to help the insurance company identify the customers that are most likely to convert, so that they can be targeted via call and the cost of telephonic marketing campaigns can be reduced. The historical sales data provided will be used to train and evaluate the performance of the machine learning models. The analysis of the model will be done to identify the important factors that contribute towards the conversion and the F1_Score metric will be used to evaluate the model's performance. The main objective of the project is to develop an accurate and efficient model that can aid the insurance company in improving its sales conversion rate and reducing marketing costs.

# **Project Aproach**:

For this project, I utilized Jupyter Notebook as my integrated development environment (IDE) for programming in Python. Jupyter Notebook is a robust tool provided by Anaconda that is well-suited for implementing machine learning algorithms, performing data analytics and cleaning operations, and developing data science models.

# **Explanation**

+ This was the problem given to me as part of my final project in the Master Data Science course by GUVI.

+ The data was loaded and preprocessed - cleaned.

+ Data Visualization was done and Exploratory Data Analysis was done to take some meaningful insights.

+ It was a highly imbalanced data with less than 11% of the data in the subscribed category.

+ Data was balanced using SMOTE and Combined balancing techniques.

+ Data was fitted in Logistic regression. The domain side of the data needed a decent F1 score to build a reliable model.

+ Feature importances were analysed for Decision Tree and XG-Boost classifiers.

# **About This Project**

1 Encoding, We  have used Label encoding for ['Job','education_qual','marital'] and one hot encoding for ['call_type','mon','prev_outcome'].

2 Models we used is Linear regression, Decision Tree classifier, K-Nearest Neighbours, XG-Boost and Random forest.

3 Feature importance, used for Decision Tree Classifier and XG-Boost, we can see that most important feature for Decision tree classifier is Dur(duration) and call_type_unknown for XG-Boost classifier

4 The model with Best value of f1_score is XG-Boost with a value of 0.58.

# **Results**

+ Logistic Regression classification F1_score is 0.48

+ Decision tree classification F1_score is 0.54

+ K-Nearest Neighbour classification F1_score is 0.37

+ XG-Boost classification F1_score is 0.58

+ Random forest classification F1_Score is 0.56

Hence XG-Boost is giving the good F1_Score of 0.58 Based on the results, we can see that the XG-Boost algorithm had the highest overall performance with an accuracy of 0.99 and an F1 score of 0.58.

# **Conclusion**

In conclusion, this project demonstrated how a classification model can be built to predict customer conversion for insurance. The data was cleaned, preprocessed, and visualized to gain insights into the data. Different algorithms were used to build the model, and XG-Boost classifier performed the best. The feature importance analysis provided valuable insights into the important features in predicting customer conversion. This model can be used by insurance companies to target potential customers who are likely to subscribe to their services.

# **Future Work**

In the future, the model can be further improved by using more advanced techniques such as hyperparameter tuning and ensemble methods. Additionally, new features can be added to the data to improve the performance of the model. The model can also be deployed as a web application to make it easily accessible to users.
