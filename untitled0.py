#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:09:01 2023

@author: jeremias
"""
import cv2
import pandas as pd
import numpy as np
import keras

import os
import glob

class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self, list_IDs, batch_size=32, shuffle=True):
        'Initialization'
        self.batch_size = batch_size
        self.list_IDs = list_IDs
        self.shuffle = shuffle
        self.on_epoch_end()

    def __len__(self):
        'Denotes the number of batches per epoch'
        return int(np.floor(len(self.list_IDs) / self.batch_size))

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]

        # Find list of IDs
        list_IDs_temp = [self.list_IDs[k] for k in indexes]

        # Generate data
        X, y = self.__data_generation(list_IDs_temp)

        return X, y

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, list_IDs_temp):
        'Generates data containing batch_size samples' # X : (n_samples, *dim, n_channels)
       
        
        x_train = []
        y_train = []
        
        for file in list_IDs_temp:
            
            if 'KITTI' in file:
                 
                  folder = file[file.rindex("s"+os.sep) + 2: file.rindex("s"+os.sep) + 4 ]
                  label_file_path = os.path.join(os.curdir, "output","KITTI_Haralick_d6_GLRLM_" + folder + ".xlsx")
                  img_Nmbr=int(file[file.rindex(os.sep)+1:-4])
                  
            if 'EuRoC' in file:
                
                folder = file[file.rindex("C"+os.sep) + 2: file.rindex("C"+os.sep) + 7 ]
                label_file_path = os.path.join(os.curdir, "output","EUROC_Haralick_d6_GLRLM_" + folder + ".xlsx")
                img_Nmbr=int(file[file.rindex(os.sep)+1:-4])
                
               
            if 'TUM' in file:
                idx = file.find("sequence")        
                l=len("sequence_xx")
                folder = file[idx: idx+l]
                label_file_path = os.path.join(os.curdir, "output","TUM_Haralick_d6_GLRLM_" + folder + ".xlsx")
                img_Nmbr=int(file[file.rindex(os.sep)+1:-4])
                
                
            img = cv2.imread(file,0)
            df = pd.read_excel(label_file_path,index_col=0)
            x_train.append(img)
            y_train.append(list(df.iloc[img_Nmbr,:-1]))
            

        return x_train, y_train




if __name__ == "__main__":
    
    import miscFunctions as mf

    im_dir1=  '/media/jeremias/JereViejo/Dataset/KITTIDataset/gray/dataset/sequences'#para KITTI
    
    im_dir2=  '/media/jeremias/JereViejo/Dataset/EuRoC'#para EuRoC
    
    im_dir3=  '/media/jeremias/JereViejo/Dataset/TUMdataset'#para EuRoC
    
    directories=[im_dir1, im_dir2, im_dir3]
    
    
    all_filenames = []
    for direc in directories:
        for folder in os.listdir(direc):
            if os.path.isdir(os.path.join(direc, folder)):
                img_path = os.path.join(direc, folder,"undistorted","*.jpg")
                all_filenames += glob.glob(img_path)
    
    
    
    [train_files, valid_files, test_files] = mf.splitDatasetCustom(all_filenames,0.7, 0.15, 0.15)




























