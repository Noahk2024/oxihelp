import pandas as pd
import math


class find_bp:
    def get_bp(bp, bmi):
        dataframe = pd.read_excel('PPG-BP-dataset.xlsx')

        curr_best = 0 
        best_dist = math.pow(10, 10)

        bmi_col = dataframe["Unnamed: 9"].values.tolist()
        systolic_blood_pressure_col = dataframe["Unnamed: 6"].values.tolist()

        bp_col = dataframe["Unnamed: 8"].values.tolist()

        for i in range(1, len(bmi_col)):
            iter_bp = bp_col[i]
            iter_bmi = bmi_col[i]

            sqr_diff = (bp - iter_bp)**2 + (bmi - iter_bmi)**2
            if (sqr_diff < best_dist):
                best_dist = sqr_diff
                curr_best = i

        return systolic_blood_pressure_col[curr_best]