class PivotBuilder:

    def build(self, df):
        pivot = df.pivot_table(
            index='Book-Title',
            columns='User-ID',
            values='Book-Rating'
        ).fillna(0)

        return pivot
