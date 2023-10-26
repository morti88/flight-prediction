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

In the initial stage of program preparation, it is essential to ensure the availability of all necessary libraries to enable seamless execution. Some of these libraries hold critical significance, including "pandas" for the transformation of data into dataframes, "pymongo" for dataset retrieval, "matplotlib" for the generation of graphical representations, "sklearn" for the integration of linear and decision models, and lastly, "tkinter" for the development of a graphical user interface. Subsequently, the program is structured through the utilization of class-based design principles, aligning with the tenets of Object-Oriented Programming.
In this Python application, we are in pursuit of two distinct classes named "Prediction" and "GUI" are elucidated as follows:


# Graphical User Interface (GUI)

This class has been purposefully designed to create a graphical user interface (GUI) framework for users. It encompasses an attribute named "base" and four methods: "create_login_page," "login," "demonstrate_decision_tree," and "result." The "base" attribute comprises five labels and five corresponding entry sections, each of which is associated with a specific label. Furthermore, the interface includes two buttons, each with distinct functions responsible for executing code.

Upon instantiation of an instance from the GUI class, the following code is used to generate labels, entry fields, and buttons, as elaborated in the subsequent discussion:

As an illustrative example, when employing the code "self.class_airline = tk.Label(self.base, text='Class:')," a label with the text "Class:" is added to the main window. To gather user input, the program necessitates an entry field, which is established using the code "self.class_airline_entry = tk.Entry(self.base)" ,resulting in the creation of an input field within the main window. Additionally, for the precise positioning of each label and entry element, code such as "self.class_airline_entry.grid(row=2, column=1)" is implemented.
Lastly, to create buttons with labeled descriptions and designated actions, the following code suffices: "self.predict_button = tk.Button(self.base, text='PREDICTION', command=self.result)."

<div>
<h3>Login</h3>
  The program offers a login interface for access to the primary window, which comprises two components: "Username" and "Password".
To enable this functionality, a fundamental function is essential. This function, denoted as "login", incorporates a conditional statement. This statement verifies whether users have entered the exact value "admin" as both the username and password. When this condition is satisfied, the program permits user access to the main interface. Conversely, if the condition is not met, the program generates an error message for the user.





</div>
<div>
<h3>Main Window</h3>
  The primary window, denoted as "FLIGHT TICKET PRICE PREDICTION" ,showcases a frame encompassing an image along with five input fields, in addition to two buttons designed for initiating predictive and decision tree-related actions.
</div>
<h3>Input Fields</h3>
There exist five input fields for the acquisition of user-supplied values, namely "Departure Time" ,"Class" ,"Airline" ,"Time Duration" and "Stop".
To collect user input, a code snippet such as "class_flight = self.class_airline_entry.get()" is required within the "result" function. This function is responsible for passing the acquired value to the "predict_price" function within the "Prediction" class. For this reason, the program necessitates an instance of the "Prediction" class, which can be instantiated with the code "predict = Prediction('sample')".This instantiation enables the program to make predictions by calling the "Prediction" class. Subsequently, by utilizing the code "messagebox.showinfo("Price Prediction", f"Predicted Price: {predicted_price[0]:.2f}")",the program can present the prediction in a messagebox.
<div>
<h3>Action Buttons</h3>
  The initial button, labeled as "DECISION TREE," is embedded to provide a visual representation of the decision tree to the user.To achieve this objective, the program is required to invoke the "demonstrate_decision_tree" function through the utilization of the subsequent code: "self.decision_tree_button = tk.Button(self.base, text='DECISION TREE', command=self.demonstrate_decision_tree)".The second button, designated as "PREDICTION",facilitates the estimation of flight ticket prices based on the user-provided input values.




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



# LOGIN
<img width="172" alt="login_picture" src="https://github.com/morti88/flight-prediction/assets/148899179/85dcf9b3-b299-4085-8dfc-35b373ef9024">


# MAIN WINDOW
<img width="244" alt="main frame" src="https://github.com/morti88/flight-prediction/assets/148899179/8cc72bfb-9e1f-4d4b-84bb-c8bceb0669bb">


# DECISION TREE
<img width="750" alt="decision tree" src="https://github.com/morti88/flight-prediction/assets/148899179/7b9dcb82-0053-44a5-b071-c6ddf064f0f6">
