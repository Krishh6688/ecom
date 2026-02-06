# import pickle
# import numpy as np

# class Recommender:

#     def recommend(self, book_name, config):

#         model = pickle.load(open(config.model_path,'rb'))
#         pivot = pickle.load(open(config.pivot_path,'rb'))

#         book_id = np.where(pivot.index==book_name)[0][0]

#         distance, suggestion = model.kneighbors(
#             pivot.iloc[book_id,:].values.reshape(1,-1),
#             n_neighbors=6
#         )

#         return pivot.index[suggestion[0]]

import pickle
import numpy as np


class Recommender:

    def recommend(self, book_name, config):

        # ---------------- LOAD ARTIFACTS ----------------
        model = pickle.load(open(config.model_path,'rb'))
        pivot = pickle.load(open(config.pivot_path,'rb'))
        final_rating = pickle.load(open(config.rating_path,'rb'))

        # ---------------- FIND BOOK INDEX ----------------
        book_id = np.where(pivot.index == book_name)[0][0]

        # ---------------- GET NEIGHBORS ----------------
        distance, suggestion = model.kneighbors(
            pivot.iloc[book_id,:].values.reshape(1,-1),
            n_neighbors=6
        )

        recommended_books = []
        poster_urls = []

        # suggestion shape → (1,6)
        for idx in suggestion[0]:

            title = pivot.index[idx]
            recommended_books.append(title)

            # fetch image url from final_rating
            img_index = np.where(final_rating['title']==title)[0][0]
            poster_urls.append(final_rating.iloc[img_index]['image_url'])

        return recommended_books, poster_urls
