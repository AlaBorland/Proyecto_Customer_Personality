from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from dotenv import dotenv_values,load_dotenv
from app.services.model.model import model
import os
import pickle
m=model
ENV = dotenv_values(".env")
load_dotenv(override=True)
print("Env: ",ENV)

pickle_file_pca = 'pca_model_integrador.pkl'
pickle_file_kmeans = 'kmeans_model_integrador.pkl'
pickle_file_svm = 'svm_model_integrador.pkl'
pickle_path = os.environ['PROJECT_PATH']


#load the pickle model
#pkl_model  = pickle.load(open(pickle_path+"/"+pickle_file_pca, "rb"))

customer_blueprint = Blueprint("customer", __name__, url_prefix="/Customer_classify")


@customer_blueprint.route("/", methods=["GET", "POST"])
def Run():
    pickle_file_pca = 'pca_model_integrador.pkl'
    pickle_file_kmeans = 'kmeans_model_integrador.pkl'
    pickle_file_svm = 'svm_model_integrador.pkl'
    pickle_path = os.environ['PROJECT_PATH']
    dataset_path = os.environ['PROJECT_PATH']+'/archive'+'/marketing_campaign.csv'
    dataset_path_save = os.environ['PROJECT_PATH']+'/archive'
    m=model
    pkl_file = m.load_pkl(pickle_path,pickle_file_pca)
    dataframe = m.load_dataset(dataset_path)
    X_PCA = m.apply_PCA(pkl_file,dataframe)
    pkl_file = m.load_pkl(pickle_path,pickle_file_svm)
    X_SVM = m.apply_SVM(pkl_file,X_PCA)
    labeled_dataframe = m.df_labeled_save(dataset_path_save,dataframe,X_SVM)
    #return labeled_dataframe
    return 'Model applied'