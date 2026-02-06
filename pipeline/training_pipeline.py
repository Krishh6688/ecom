from config.configuration import AppConfiguration
from components.data_loader import DataLoader
from components.data_cleaning import DataCleaning
from components.pivot_builder import PivotBuilder
from components.model_trainer import ModelTrainer

class TrainingPipeline:

    def start(self):

        config = AppConfiguration()

        books, ratings, users = DataLoader().load_data(config)
        df = DataCleaning().clean(books, ratings)
        pivot = PivotBuilder().build(df)
        ModelTrainer().train(pivot, config)
