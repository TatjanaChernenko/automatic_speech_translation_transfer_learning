# AST with Transfer Learning (playground)

```
Attention-based sequence to sequence AST System. The model uses ASR and MT Systems for initialization (Transfer Learning).

The project is based on the code of Alexandre Bérard https://github.com/eske/seq2seq

## Getting Started

### Prerequisites and Installing

1. Follow the instructions https://github.com/eske/seq2seq to install the dependencies and the seq2seq system.
2. Download the folder cluster/home/proj/speechrecognition/TRANSFER_LEARNING_AST 

### Input Data

* Used Input Data (given):

```
cluster/home/proj/speech_data_models/data
```

* Used pre-trained ASR and MT Models (given)

ASR ("best-276000" was used for initialisation): 

```
cluster/home/proj/speechrecognition/TRANSFER_LEARNING_AST/models/ASR
```
MT ("best-98000" was used for initialisation): 
```
cluster/home/proj/speechrecognition/TRANSFER_LEARNING_AST/models/MT
```

## Learn the system
## READY-TO-USE MODEL:

 **Our ready-to-use best model:** 
 ```
 /home/proj/speechrecognition/TRANSFER_LEARNING_AST/models2/best.index
```
* Other checkpoints and log files: 

--- First 220000 steps (srarting from 98000 step):
```
cluster/home/proj/speechrecognition/TRANSFER_LEARNING_AST/models
```
--- Next steps:
```
/home/proj/speechrecognition/TRANSFER_LEARNING_AST/models2/
```
* Configuration files:

--- First 220000 steps (starting from step 98000):
```
cluster/home/proj/speechrecognition/TRANSFER_LEARNING_AST/transfer_1.yaml
```
--- Next steps:
```
cluster/home/proj/speechrecognition/TRANSFER_LEARNING_AST/transfer_2.yaml
```
## TRAIN YOUR OWN MODEL:

- Create new output folder, change directions/hyperparameters/checkpoints in transfer_1.yaml configuration file.

- Change to your seq2seq folder, run the following script:
```
./seq2seq.sh CONFIG --train -v 
```
...where CONFIG is the direction to the transfer_1.yaml file on your computer.


## Other possobilities:

* Input Data produced by our group:
tar audio files:
```
cluster/home/proj/speechrecognition/archiv
```
npz, vocab und spain textfiles:
```
cluster/home/students/chernenko/speech_recognition/features
```
* To generate your own input Data with scripts of our group:
cluster/home/proj/speechrecognition/seq2seq

```
1_dataset_devide.py
2_change_format.sh
3_split_files.py
4_extract.py  (original script - seq2seq/scripts/speech/extract.py)
```

* Use other versions of pre-trained ASR and MT Models (new ones):

```
cluster/home/proj/speech_data_models/models/
```

## Built With

* [Alexandre Bérard] https://github.com/eske/seq2seq) 

## Authors

* **Chernenko Tetyana (Tatjana)** 
* **Liang Siting**
{chernenko/liang}@cl.uni-heidelberg.de

