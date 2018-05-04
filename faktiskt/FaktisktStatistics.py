import pandas as pd


class FaktisktStatistics(object):
    entirely_true = "helt sant"
    entirely_false = "helt fel"
    partly_true = "delvis sant"
    partly_false = "mestadels fel"

    def __init__(self, investigation_data, group):
        super(FaktisktStatistics, self).__init__()
        self.investigation_data = investigation_data
        self.group = group
        self.parse_data()

    def parse_data(self, method="records"):
        if method == "records":
            self.df = pd.DataFrame.from_records(self.investigation_data)
        else:
            raise TypeError

    @property
    def n_investigations(self):
        return self.df[self.group].value_counts()

    @property
    def n_entirely_false(self):
        is_false = self.df["check_conclusion"] == self.entirely_false
        return self.df[is_false][self.group].value_counts()

    @property
    def n_partly_false(self):
        is_partly_false = self.df["check_conclusion"] == self.partly_false
        return self.df[is_partly_false][self.group].value_counts()

    @property
    def n_entirely_true(self):
        is_partly_false = self.df["check_conclusion"] == self.entirely_true
        return self.df[is_partly_false][self.group].value_counts()

    @property
    def n_partly_true(self):
        is_partly_false = self.df["check_conclusion"] == self.partly_true
        return self.df[is_partly_false][self.group].value_counts()

