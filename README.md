# Dataset Augmentation by Negative Harmony Theory for Music Generation
## 1. Environment
A conda environment is provided in ```environment.yml```.  
Load it with<br>
```conda env create -f environment.yml```  
Then you can activate it with<br>
```conda activate public_transformer_bach```  
## 2. Datasets
On the first run, you need to create datasets(xml/midi/etc.) in `$HOME/Data/xmlDatasets` folder.  
## 3. Dataset Augmentation
Run<br>
```python NegativeHarmony/negative.py $HOME/Data/xmlDatasets -r -m <MODE CLASS> ```  
(# MODE CLASS =  N | N+ | N+part1 | N+part2 | prepare, Please refer to [sohoelf/NegativeHarmony](https://github.com/sohoelf/NegativeHarmony) for details.)  
Then the expanded data will be added `$HOME/Data/negative_pieces`, then you can put them into `$HOME/Data/xmlDatasets` folder.  
## 4. Training
Before training, modify the hyperparameters in ```transformer_bach/bach_decoder_config.py```, then run  
```python main.py --train --config=transformer_bach/bach_decoder_config.py``` for training.  
When prompted for the creation of the index table of the dataset, enter `index`.  
After building the dataset training should start.  
Models are saved in the `models/` folder.  
## 5. Generating
When the training is completed, target pieces will be automatically generated in the `models/model_id/generations` folder.  
You also can generate from a trained model with  
`python main.py --load --config=models/model_id/config.py -o`.  
You choose to reharmonize different melodies by changing the `melody_constraint` variable at the end of `main.py`.
