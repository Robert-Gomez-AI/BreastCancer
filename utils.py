import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split


def get_images(size,directorio,label_list):
    images=[]
    labels=[]
    label_num=0
    for label in label_list:
        plotted=True
        for nombre_archivo in os.listdir(directorio+label):
            image= cv2.imread(directorio+label+'/'+nombre_archivo)
            if plotted:
                plt.imshow(image.astype(np.uint8))
                plt.axis('off')
                plt.title(label.capitalize())
                plotted= False
            resized_image=cv2.resize(image,size)
            images.append(resized_image)
            labels.append(label_num)

        plotted=False
        label_num+=1
    return np.array(images)/225.,np.array(labels) 


def train_validation_test_split(X, y, test_size=0.2, val_size=0.25, random_state=42):

     # Dividir dataset en conjunto de entrenamiento + validación y conjunto de test
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Dividir conjunto de entrenamiento + validación en conjunto de entrenamiento y conjunto de validación
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=val_size/(1-test_size), random_state=random_state)
    
    return X_train, X_val, X_test, y_train, y_val, y_test




        
