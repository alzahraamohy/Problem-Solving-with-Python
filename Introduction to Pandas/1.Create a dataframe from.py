# https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    columns = ["student_id", "age"]
    
    df = pd.DataFrame(student_data, columns=columns)
    
    return df
