import os 
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd 
from src.datascience.entity.config_entity import DataTransformationConfig



class DataTranformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        
    ## You can perform all kind of EDA in ML cycle here before passing this to model 
    # I am only interested in train_test_split 
    
    def train_test_splitting(self):
        data= pd.read_csv(self.config.data_path)
        
        # Split data into training and test sets
        train,test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False) 
        
        logger.info(f"Train and test data saved in {self.config.root_dir}. \n")   
        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)
    
    
    