# Dataset Augmentation by Negative Harmony Theory for Music Generation
## 1. Environment
A conda environment is provided in environment.yml.<br>
Load it with<br>
```conda env create -f environment.yml```<br>
Then you can activate it with<br>
```conda activate public_transformer_bach```<br>
## 2. Datasets
On the first run, you need to create datasets(xml/midi/etc.) in `$HOME/Data/xmlDatasets` folder.  <br>
## 3. Dataset Augmentation
Run<br>
```python NegativeHarmony/negative.py $HOME/Data/xmlDatasets -r -m <MODE CLASS> ```
(# MODE CLASS =  N | N+ | N+part1 | N+part2 | prepare, Please refer to [sohoelf/NegativeHarmony](https://github.com/sohoelf/NegativeHarmony) for details.)
Then the expanded data will be added `$HOME/Data/negative_pieces`, then you can put them into `$HOME/Data/xmlDatasets` folder.<br>
## 4. Training
Before training, modify the hyperparameters in ```transformer_bach/bach_decoder_config.py```, then run<br>
```python main.py --train --config=transformer_bach/bach_decoder_config.py``` for training.<br>
When prompted for the creation of the index table of the dataset, enter `index`.<br>
After building the dataset training should start.<br>
Models are saved in the `models/` folder.<br>
## 5. Generating
When the training is completed, target pieces will be automatically generated in the `models/model_id/generations` folder.<br>
You also can generate from a trained model with<br>
`python main.py --load --config=models/model_id/config.py -o`.<br>
You choose to reharmonize different melodies by changing the `melody_constraint` variable at the end of `main.py`.
