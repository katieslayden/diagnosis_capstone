'''
Contains the class Reduce_Features. This is step 3 of 4 in modeling to predict
suicide ideation using the ICPSR dataset on mental health.
All four steps are run from and return output to the COORDINATOR.py file.
'''
import pandas as pd

class Reduce_Features():

    def __init__(self, data_file, full_dict):
        self.full_dict = full_dict
        self.universal_features = self.get_universals()
        self.messy_df = pd.read_csv(data_file, sep='\t', low_memory=False)
        self.features_max5 = self.get_feat_max5()

    def get_universals(self):
        universals = {}
        nonuniversals = {}
        for akey, avalue in self.full_dict.items():
            for ckey, cvalue in avalue.items():
                if 'broken' not in ckey:
                    if cvalue[1] == True:
                        universals[ckey] = cvalue
                    else:
                        nonuniversals[ckey] = cvalue
        return universals

    def get_feat_max5(self):
        def feature_max(feature):
            x = feature_uniques[feature]
            sorted_x = sorted(x, reverse=True)
            no_space = sorted_x[0:-1]
            range_list = []
            for i in no_space:
                range_list.append(float(i))
            return max(range_list)

        features_max5 = []
        feature_uniques = {}
        good_features = list(self.universal_features.keys())
        for feature in good_features:
            feature_uniques[feature] = list(pd.unique(self.messy_df[feature]))
            if feature_max(feature) <= 5.0:
                features_max5.append(feature)

        return features_max5

    def execute_reduce(self):
        reduced_df = pd.DataFrame()
        for feature in self.features_max5:
            reduced_df[feature] = self.messy_df[feature]
        return reduced_df

    # def execute_reduce(self):
    #     reduced_df = pd.DataFrame()
    #     for feature in self.universal_features:
    #         reduced_df[feature] = self.messy_df[feature]
    #     return reduced_df
