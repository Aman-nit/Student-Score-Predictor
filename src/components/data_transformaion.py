"""
This file is responsible for performing data preprocessing and feature engineering.
Key operations include:
- Handling missing values
- Applying label encoding and one-hot encoding
- Scaling numerical features
"""

import sys
import os 
from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer # Used to apply different transformations to different columns
from sklearn.impute import SimpleImputer  # For handling missing values
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline # To build sequential transformation workflows

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    prepprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")



class DataTransformation:
    def __init__(self):
        self.data_transformation_config= DataTransformationConfig()

    def get_data_transformer_object(self):

        '''

        '''
        try:
            numrical_columns = ["writing_score","reading_score"]
            categorical_columns = ["gender",
                                   "race_ethnicity",
                                   "parental_level_of_education",
                                   "lunch",
                                   "test_preparation_course",
                                   ]
            numrical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(

                steps=[
                    ("Imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_incoder", OneHotEncoder()),
                    ("scaler", StandardScaler())
                ]
            )

            logging.info("Numrical columns standard scaling completed")
            logging.info("Categorical columns encoding completed")

            preprocessor = ColumnTransformer(
                [
                    ("numrical_pipeline",numrical_pipeline,numrical_columns),
                    ("categ_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data")
            logging.info("obtaining preprocessing objects")

            preprocessing_obj = self.get_data_transformer_object()
            target_column_name = "math_score"
            numrical_columns = ["writing_score","reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis= 1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = train_df.drop(columns=[target_column_name], axis= 1)
            target_feature_test_df = train_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)