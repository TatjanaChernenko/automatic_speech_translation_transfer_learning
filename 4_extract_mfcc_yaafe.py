# http://yaafe.sourceforge.net/features.html#mfcc

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
    
    
import os
from yaafelib import *

def extract_mfcc_deltas_deltadeltas(folder,dataset):
    for audiofile in os.listdir(folder):
    # Build a DataFlow object using FeaturePlan:
        fp = FeaturePlan(sample_rate=8000)  #sample rate 8000 Hz

    # Extract Features:

    # 1 Feature
        fp.addFeature('mfcc_1: MFCC') # default blockSize=1024 stepSize=512')

    # 2 Feature 
        fp.addFeature('mfcc_2: MFCC CepsIgnoreFirstCoeff=0') #default 0 keeps the first cepstral coeffcient, 1 ignore it

    # 3 Feature
        fp.addFeature('mfcc_3: MFCC CepsNbCoeffs=5') #(default=13): Number of cepstral coefficient to keep.

    # 4 Feature
        fp.addFeature('mfcc_4: MFCC FFTWindow=Hamming') # (default=Hanning) Weighting window to apply before fft. Hanning|Hamming|None

    # 5 Feature
        fp.addFeature('mfcc_5: MFCC FFTWindow=None') #(default=Hanning) Weighting window to apply before fft. Hanning|Hamming|None

    # 6 Feature
        fp.addFeature('mfcc_6: MFCC MelMinFreq=10.0') # (default=130.0): Minimum frequency of the mel filter bank

    # 7 Feature
        fp.addFeature('mfcc_7: MFCC MelMaxFreq=1000.0') #(default=6854.0): Maximum frequency of the mel filter bank

    # 8 Feature
        fp.addFeature('mfcc_8: MFCC MelNbFilters=80') #(default=40): Number of mel filters

    # 9 Feature
        fp.addFeature('mfcc_9: MFCC blockSize=512 stepSize=256') # blockSize (default=1024): output frames size, stepSize (default=512): step between consecutive frames

    # 10 Feature
        fp.addFeature('mfcc_10: MFCC blockSize=512 stepSize=256 CepsIgnoreFirstCoeff=0 CepsNbCoeffs=10 FFTWindow=Hamming MelMinFreq=100.0 MelMaxFreq=6000.0 MelNbFilters=30')

    # 11 Feature
        fp.addFeature('mfcc_11: MFCC CepsNbCoeffs=10 FFTWindow=None MelMinFreq=100.0 MelMaxFreq=6000.0 MelNbFilters=30')

    # 12 Feature
        fp.addFeature('mfcc_12: MFCC blockSize=512 stepSize=256 CepsIgnoreFirstCoeff=0 FFTWindow=Hamming MelMinFreq=100.0 MelMaxFreq=6000.0')

    # 13 - Energy Feature
        fp.addFeature('energy_13: Energy') #blockSize (default=1024): output frames size, stepSize (default=512): step between consecutive frames

    # Energy Feature Deltas delta and delta-delta features (Derivate DOrder=1 and Derivate DOrder=2)

    # 14 - Feature - Delta of Energy feature - temporal derivative of input feature; Order of the derivative to compute = 1
        fp.addFeature('energy_13_d1: Energy > Derivate DOrder=1')

    # 15 Feature - Delta-delta of Energy feature - temporal derivative of input feature; Order of the derivative to compute = 2
        fp.addFeature('energy_13_d2: Energy > Derivate DOrder=2')

        df = fp.getDataFlow()

    # configure an Engine
        engine = Engine()
        engine.load(df)

    # extract features from an audio file using AudioFileProcessor
        afp = AudioFileProcessor()
        afp.processFile(engine,folder+"/"+audiofile)
       
        feats = engine.readAllOutputs()

    # extract features from an audio file and write results to csv files
        afp.setOutputFormat('csv','output_mfcc_'+dataset,{'Precision':'8'})

        afp.processFile(engine,folder+"/"+audiofile)

    # this creates folder/output/myaudio.wav.mfcc.csv,
    #              output/myaudio.wav.mfcc_d1.csv and
    #              output/myaudio.wav.mfcc_d2.csv files.

   
if __name__=="__main__":
    test_split = data["splitted"][0]
    dev1_split = data["splitted"][1]
    dev2_split = data["splitted"][2]
    train_split = data["splitted"][3]
    #test_split = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/TEST/splitted"
    #dev1_split= "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/DEV1/splitted"
    #dev2_split = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/DEV2/splitted"
    #train_split = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/TRAIN/splitted"

    extract_mfcc_deltas_deltadeltas(train_split, "train")
    extract_mfcc_deltas_deltadeltas(dev1_split, "dev1")
    extract_mfcc_deltas_deltadeltas(dev2_split, "dev2")
    extract_mfcc_deltas_deltadeltas(test_split, "test")
