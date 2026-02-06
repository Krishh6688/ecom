import os

class AppConfiguration:

    def __init__(self):
        self.data_path = "data/"
        self.model_path = "artifacts/model.pkl"
        self.pivot_path = "artifacts/book_pivot.pkl"
        self.rating_path = "artifacts/final_rating.pkl"
