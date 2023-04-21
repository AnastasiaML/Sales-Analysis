import pandas as pd
import os

path = './datasets/original'
dir_list = os.listdir(path)
 
datasets = [] 
for file in dir_list:
  datasets.append(pd.read_csv(f'{path}/{file}'))

merged_dataset = pd.concat(datasets)
merged_dataset.reset_index(inplace = True, drop = True)

merged_dataset.to_csv('./datasets/merged/merged.csv', index=False)