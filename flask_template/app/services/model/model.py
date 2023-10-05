import pickle
from dotenv import dotenv_values,load_dotenv
import os
import pandas as pd

ENV = dotenv_values(".env")
load_dotenv(override=True)
print("Env: ",ENV)
pickle_file_pca = 'pca_model_integrador.pkl'
pickle_file_kmeans = 'kmeans_model_integrador.pkl'
pickle_file_svm = 'svm_model_integrador.pkl'
pickle_path = os.environ['PROJECT_PATH']
dataset_path = os.environ['PROJECT_PATH']+'/archive'+'/marketing_campaign.csv'
dataset_path_save = os.environ['PROJECT_PATH']+'/archive' 
class model:
    def __init__(self):
        print("This is my constructor")

    def load_dataset(self,data_path):
        fileName = data_path
        df_mark = pd.read_csv(fileName,sep='\t')
        print("dataset loaded")
        df = df_mark
        #Make it legible 
        df['Education']=df['Education'].replace({'Basic':0,'2n Cycle':1,'Graduation':2,'Master':3,'PhD':4})
        df['Marital_Status']=df['Marital_Status'].replace({'YOLO':0,'Absurd':0,'Alone':0,'Single':0,'Widow':0,'Divorced':0,'Together':1,'Married':1})
        df['Age']=2023-df['Year_Birth']
        #Clean DataFrame from useless data
        df = df.drop(["Dt_Customer"], axis='columns')
        df = df.drop(["ID"], axis='columns')
        df = df.drop(["Z_CostContact"], axis='columns')
        df = df.drop(["Z_Revenue"], axis='columns')
        df = df.drop(["Year_Birth"], axis='columns')
        df = df.dropna()
        return df


    def load_pkl(self,pickle_path,pkl_name):
        pickle_file = pickle.load(open(pickle_path+"/"+pkl_name, 'rb'))
        print("pkl file loaded")
        return pickle_file

    def apply_PCA(self,pickle_pca,dataset):
        PCA = pickle_pca.transform(dataset)
        print("Dataframe transformed")
        return PCA
    
    def apply_SVM(self,pickle_svm,pca_df):
        SVM = pickle_svm.predict(pca_df)
        print("Dataframe predicted")
        return SVM
    
    def df_labeled_save(self,Dataset_path_save,dataframe,labels):
        dataframe['labels'] = labels
        Dataset_path_save = Dataset_path_save+'/marketing_campaign_api_labeled'
        dataframe.to_csv(Dataset_path_save+".csv")
        print("Labels added and data saved")
        return dataframe

    def Run(self):
        """ 
        pickle_file_pca = 'pca_model_integrador.pkl'
        pickle_file_kmeans = 'kmeans_model_integrador.pkl'
        pickle_file_svm = 'svm_model_integrador.pkl'
        pickle_path = os.environ['PROJECT_PATH']
        dataset_path = os.environ['PROJECT_PATH']+'/archive'+'/marketing_campaign.csv'
        dataset_path_save = os.environ['PROJECT_PATH']+'/archive' """
        pkl_file = self.load_pkl(pickle_path,pickle_file_pca)
        dataframe = self.load_dataset(dataset_path)
        X_PCA = self.apply_PCA(pkl_file,dataframe)
        pkl_file = self.load_pkl(pickle_path,pickle_file_svm)
        X_SVM = self.apply_SVM(pkl_file,X_PCA)
        labeled_dataframe = self.df_labeled_save(dataset_path_save,dataframe,X_SVM)
        return 'Model Applied, csv generated'
