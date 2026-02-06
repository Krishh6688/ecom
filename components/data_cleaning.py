class DataCleaning:

    def clean(self, books, ratings):
        books = books.drop(['Image-URL-S','Image-URL-M','Image-URL-L'],axis=1)

        df = ratings.merge(books,on='ISBN')

        # filter active users
        x = df['User-ID'].value_counts() > 200
        y = x[x].index
        df = df[df['User-ID'].isin(y)]

        return df
