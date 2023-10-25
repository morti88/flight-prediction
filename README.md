# flight-prediction

<h3>Introduction</h3>

The prediction of flight ticket prices has become a critical area of research and application, enabling travelers and the aviation industry to navigate the ever-changing landscape of airfares (Hahn, 2014). This academic exploration delves into predictive modeling for flight ticket prices, aiming to elucidate the methodologies and tools used to anticipate price fluctuations .

<p align='centre'>
  <img src='https://github.com/morti88/flight-prediction/assets/148899179/80091401-63ef-4f95-ad3b-264612e46ebd'>
  <br>
  Figure 1 - FlowChart
</p>

The presented flowchart illustrates the sequential steps involved in the process of gathering user data to predict flight ticket prices. Initially, the program undertakes an input validation process to verify the accuracy of the provided user credentials. In the event of validation failure, the program terminates and displays an error message to the user. Conversely, if the validation is successful, the program proceeds to retrieve a clean dataset of flight ticket information from a MongoDB database. In the event of unsuccessful retrieval from MongoDB, the program falls back to the use of local data sources. This fallback option is contingent on establishing a successful connection, facilitating the acquisition of the dataset in a structured dataframe format.

Subsequently, the user is prompted to input values that are integral for the predictive model. In the event of disparities between the user's inputs and the values within the dataset, the program will not proceed and will return the user to the initial graphical user interface (GUI) page. In contrast, when the user's input matches the dataset values, the program advances to either the decision tree model or another predictive model for ticket price forecasting.


<p align='centre'>
  <img src='https://github.com/morti88/flight-prediction/assets/148899179/34f18844-35f0-41cb-8423-197d0d06d6ab'>
  <br>
  Figure 2 - Class Diagram
</p>




# Constructing the Program
In this Python application, we are in pursuit of two distinct classes named "Prediction" and "GUI."


# Graphical User Interface (GUI)

<div>
<h3>Login</h3>
  The program offers a login interface for access to the primary window, which comprises two components: "Username" and "Password."
</div>
<div>
<h3>Main Window</h3>
  The primary window, denoted as "FLIGHT TICKET PRICE PREDICTION," showcases a frame encompassing an image along with five input fields, in addition to two buttons designed for initiating predictive and decision tree-related actions.
</div>
<h3>Input Fields</h3>
There exist five input fields for the acquisition of user-supplied values, namely "Departure Time," "Class," "Airline," "Time Duration," and "Stop."
<div>
<h3>Action Buttons</h3>
  The initial button, labeled as "DECISION TREE," is embedded to provide a visual representation of the decision tree to the user. The second button, designated as "PREDICTION," facilitates the estimation of flight ticket prices based on the user-provided input values.




# Prediction Class
The "Prediction" class is designed to predict flight ticket prices based on user input, employing an attribute called "sample" and featuring four key methods: "read data," "training data," "decision tree," and "predict price."

<h3>Data Retrieval with "read data"</h3>
The "read data" method extracts a clean dataset from MongoDB and converts it into a DataFrame. This conversion is essential for preparing the data for model training.

<h3>Model Training through "training data"</h3>
The "training data" method is responsible for training a machine learning model. It focuses on the dataset retrieved from MongoDB, splitting it into two essential parts: X (independent variables) and y (dependent variable). This division allows the data to be further divided into "X_train" and "y_train," which are crucial for model training.

<h3> Visualizing Decision Trees with "decision tree"</h3>
The "decision tree" method creates a visual representation of the decision tree used in our predictive model. It transforms the dataset, which contains interval data, into numerical data suitable for DecisionTreeRegression. Feature selection is employed to improve the accuracy of the decision tree. Specifically, five columns ('airline,' 'class,' 'departure_time,' 'duration,' and 'stops') are chosen to train the X-axis, while 'price' serves as the y-axis. The data is split, with 80% allocated to training and the rest for testing. The method concludes by plotting the decision tree.

<h3> Price Prediction via "predict price"</h3>
The "predict price" method is central to the program's objective of predicting flight ticket prices. Users provide a DataFrame with the relevant information. The method then trains a regression model using five selected columns ('airline,' 'class,' 'departure_time,' 'duration,' and 'stops'). Finally, after inputting the user's DataFrame, the method generates a ticket price estimate.


# SOURCE CODE
<img width="925" alt="1" src="https://github.com/morti88/flight-prediction/assets/148899179/500429ce-910a-4796-b1cc-58abc6cf9d35">
<img width="923" alt="2" src="https://github.com/morti88/flight-prediction/assets/148899179/c6656934-b4a1-4361-aa80-f937f82d996f">
<img width="924" alt="3" src="https://github.com/morti88/flight-prediction/assets/148899179/036b8811-4ba1-4459-9259-1ba41a69053c">
<img width="914" alt="4" src="https://github.com/morti88/flight-prediction/assets/148899179/d254b4bf-332c-48d2-b4bd-39df00634ef1">
<img width="925" alt="5" src="https://github.com/morti88/flight-prediction/assets/148899179/701c4631-08ed-4d95-b8e5-e240e9d78ace">
<img width="926" alt="6" src="https://github.com/morti88/flight-prediction/assets/148899179/9628a614-e58b-4050-b8a7-a9a0740ff615">
