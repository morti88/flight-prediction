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
  <img src='https://github.com/morti88/flight-prediction/assets/148899179/ccf7a015-9771-45ab-828c-b0f077148309'>
  <br>
  Figure 2 - Class Diagram
</p>


