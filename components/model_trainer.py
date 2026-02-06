import pickle
from sklearn.neighbors import NearestNeighbors

class ModelTrainer:

    def train(self, pivot, config):
        model = NearestNeighbors(metric='cosine')
        model.fit(pivot)

        pickle.dump(model, open(config.model_path,'wb'))
        pickle.dump(pivot, open(config.pivot_path,'wb'))
