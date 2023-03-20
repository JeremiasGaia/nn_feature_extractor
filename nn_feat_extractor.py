#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:46:09 2023

@author: jeremias
"""

import pandas as pd
import numpy as np
import os
import glob
# from keras.models import Sequential
# from my_classes import DataGenerator
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

# # Parameters
# params = {'batch_size': 2,
#           'shuffle': True}
# 
# # Generators
# training_generator = DataGenerator(train_files, **params)
# validation_generator = DataGenerator(valid_files, **params)
# 
# # Design model
# model = Sequential()
# [...] # Architecture
# model.compile()

# # Train model on dataset
# model.fit_generator(generator=training_generator,
#                     validation_data=validation_generator,
#                     use_multiprocessing=True,
#                     workers=6)























# im_dir=  '/media/jeremias/JereViejo/Dataset/KITTIDataset/gray/dataset/sequences'#para KITTI

# im_dir=  '/media/jeremias/JereViejo/Dataset/EuRoC'#para EuRoC

# im_dir=  '/media/jeremias/JereViejo/Dataset/TUMdataset'#para EuRoC


# x_train=[]
# y_train=[]

# for folder in os.listdir(im_dir):
    
#     if os.path.isdir(os.path.join(im_dir, folder)):
#         img_path = os.path.join(im_dir, folder,"undistorted","*.jpg")
    
#         if 'KITTI' in im_dir:
            
#             label_file_path = os.path.join(os.curdir, "output","KITTI_Haralick_d6_GLRLM_" + folder + ".xlsx")
#         if 'EuRoC' in im_dir:
            
#             label_file_path = os.path.join(os.curdir, "output","EUROC_Haralick_d6_GLRLM_" + folder + ".xlsx")
        
#         if 'TUM' in im_dir:
#             label_file_path = os.path.join(os.curdir, "output","TUM_Haralick_d6_GLRLM_" + folder + ".xlsx")
         
        
#         filenames=glob.glob(img_path)
        
#         i=0
#         for img_file in filenames:
            
#             img = cv2.imread(img_file,0)
#             df = pd.read_excel(label_file_path,index_col=0)
#             x_train.append(img)
#             y_train.append(list(df.iloc[i,:-1]))



"""
Lo que hay que hacer ahora es ver como metemos esta funcion dentro del generador en el archivo
untitled cero en la parte de data generation.
Luego de eso adaptar la función
luego probarla

"""
                
            
            
            
            
            
            
            
            
            
            