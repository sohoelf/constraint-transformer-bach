import music21

from transformer_bach.DatasetManager.chorale_dataset import ChoraleDataset, ChoraleBeatsDataset
from transformer_bach.DatasetManager.helpers import ShortChoraleIteratorGen

from tqdm import tqdm
import os

def get_local_datasets():
    print("Loading datasets...")
    xmlDatasets = []
    path_ = f'{os.path.expanduser("~")}/Data/xmlDatasets'
    for file_ in tqdm(os.listdir(path_)):
        if not os.path.isdir(file_):
            xmlDatasets.append(music21.converter.parse(path_+"/"+file_))
    return xmlDatasets

xmlDatasets=get_local_datasets()

def get_all_datasets():
    return {

        'bach_chorales':
            {
                'dataset_class_name': ChoraleDataset,
                'corpus_it_gen':      xmlDatasets
            },
        'bach_chorales_beats':
            {
                'dataset_class_name': ChoraleBeatsDataset,
                'corpus_it_gen':      xmlDatasets
            },
        'bach_chorales_beats_test':
            {
                'dataset_class_name': ChoraleBeatsDataset,
                'corpus_it_gen':      ShortChoraleIteratorGen()
            },
        'bach_chorales_test':
            {
                'dataset_class_name': ChoraleDataset,
                'corpus_it_gen':      ShortChoraleIteratorGen()
            },

    }
