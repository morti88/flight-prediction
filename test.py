from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.linear_model import LinearRegression
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
from sklearn.impute import SimpleImputer

class Prediction:
    def __init__(self, sample):
        self.sample = sample
        self.data_frame = self.read_data()

    def train_data(self):
        features = ['airline', 'class', 'departure_time','duration','stops']
        X = self.data_frame[features]
        Y = self.data_frame['price']

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        return X_train.join(Y_train)

    def read_data(self):
        connection = MongoClient('localhost')
        my_database = connection['flight']
        collection = my_database['flights']
        my_data = collection.find()
        data_frame = pd.DataFrame(list(my_data))

        a = {'SpiceJet': 0, 'AirAsia': 1, 'Vistara': 2, 'GO_FIRST': 3, 'Indigo': 4, 'Air_India': 5}
        data_frame['airline'] = data_frame['airline'].map(a)

        c = {'Economy': 0, 'Business': 1}
        data_frame['class'] = data_frame['class'].map(c)

        d = {'Early_Morning': 0, 'Morning': 1, 'Afternoon': 2, 'Evening': 3, 'Night': 4}
        data_frame['departure_time'] = data_frame['departure_time'].map(d)

        e={'zero': 0,'one': 1,'two_or_more':2}
        data_frame['stops']=data_frame['stops'].map(e)

        return data_frame

    def decision_tree(self):
        features = ['airline', 'class', 'departure_time','duration','stops']
        X = self.data_frame[features]
        Y = self.data_frame['price']

        dtree = DecisionTreeRegressor()
        dtree = dtree.fit(X, Y)

        plt.figure(figsize=(10, 6))
        plot_tree(dtree, feature_names=features, filled=True, rounded=True)
        plt.show()

    def predict_price(self, departure_time, class_flight, airline,time_duration,stops):
        features = ['airline', 'class', 'departure_time','duration','stops']
        a = {'SpiceJet': 0, 'AirAsia': 1, 'Vistara': 2, 'GO_FIRST': 3, 'Indigo': 4, 'Air_India': 5}
        airline = a.get(airline, 0)

        c = {'Economy': 0, 'Business': 1}
        class_flight = c.get(class_flight, 0)

        d = {'Early_Morning': 0, 'Morning': 1, 'Afternoon': 2, 'Evening': 3, 'Night': 4}
        departure_time = d.get(departure_time, 0)

        e = {'zero': 0,'one': 1,'two_or_more':2}
        stops = e.get(stops , 0)


        user_input = {
            'departure_time': departure_time, 
            'class': class_flight, 
            'airline': airline,
            'duration': time_duration,
            'stops': stops
        }
        user_input = pd.DataFrame([user_input], columns=features)
        self.data_frame = self.read_data()
        self.data_frame = self.data_frame.dropna()
        X = self.data_frame[features]
        Y = self.data_frame['price']

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        sample = LinearRegression()
        sample = sample.fit(X_train, Y_train)

        return sample.predict(user_input)

class GUI:
    def __init__(self, base):
        self.base = base
        self.base.title("FLIGHT TICKET PRICE PREDICTION")

        self.image = Image.open('dataset-card.jpg')
        self.image = self.image.resize((300, 200))
        self.image = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(base, width=300, height=300)
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        self.departure_time = tk.Label(self.base, text="Departure Time:")
        self.departure_time.grid(row=1, column=0)
        self.departure_time_entry = tk.Entry(self.base)
        self.departure_time_entry.grid(row=1, column=1)
        self.class_airline = tk.Label(self.base, text="Class:")
        self.class_airline_entry = tk.Entry(self.base)
        self.class_airline_entry.grid(row=2, column=1)
        self.class_airline.grid(row=2, column=0)
        self.airline = tk.Label(self.base, text="Airline:")
        self.airline.grid(row=3, column=0)
        self.airline_entry = tk.Entry(self.base)
        self.airline_entry.grid(row=3, column=1)
        self.time_duration=tk.Label(self.base, text='Time_duration :')
        self.time_duration.grid(row=4,column=0)
        self.time_duration_entry = tk.Entry(self.base)
        self.time_duration_entry.grid(row=4, column=1)
        self.stops=tk.Label(self.base,text='Stop :')
        self.stops.grid(row=5,column=0)
        self.stops_entry=tk.Entry(self.base)
        self.stops_entry.grid(row=5,column=1)
        # self.your_price=tk.Label(text='YOUR PRICE IS :')
        # self.your_price.grid(row=6,column=0)
        # self.your_price_result=tk.Label(self.base, textvariable=self.result)
        # self.your_price_result.grid(row=6, column=2)

        self.predict_button = tk.Button(self.base, text="PREDICTION", command=self.result)
        self.predict_button.grid(row=6, column=1, padx=10, pady=10)
        self.decision_tree_button = tk.Button(self.base, text="DECISION TREE", command=self.demonstrate_decision_tree)
        self.decision_tree_button.grid(row=6, column=0, padx=10, pady=10)

    def demonstrate_decision_tree(self):
        tree = Prediction('sample')
        tree.decision_tree()

    def result(self):
        departure_time = self.departure_time_entry.get()
        class_flight = self.class_airline_entry.get()
        airline = self.airline_entry.get()
        time_duration = float(self.time_duration_entry.get())
        stops = self.stops_entry.get()

        predict = Prediction('sample')
        predicted_price = predict.predict_price(departure_time, class_flight, airline,time_duration,stops)
        #return predicted_price
        messagebox.showinfo("Price Prediction", f"Predicted Price: {predicted_price[0]:.2f}")

def main():
    my_frame = tk.Tk()
    gui = GUI(my_frame)
    my_frame.mainloop()

if __name__ == '__main__':
    main()
