import pandas as pd

class DataLoader:

    def load_data(self, config):
        books = pd.read_csv(config.data_path+"BX-Books.csv", sep=";", encoding="latin-1")
        ratings = pd.read_csv(config.data_path+"BX-Book-Ratings.csv", sep=";", encoding="latin-1")
        users = pd.read_csv(config.data_path+"BX-Users.csv", sep=";", encoding="latin-1")
        return books, ratings, users
