import os
import shutil
import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
#print(data)


def dataset_split(map_list, n_map_list, fisher_spa, fisher_spa_tr):
    # Read mappings: 
    test = map_list[0]
    dev1 =  map_list[1]
    dev2 =  map_list[2]
    train = map_list[3]
    with open(test, "r") as t:
        test = t.readlines()
    with open(dev1, "r") as d1:
        dev1 = d1.readlines()
    with open(dev2, "r") as d2:
        dev2 = d2.readlines()
    with open(train, "r") as tr:
        train = tr.readlines()

    # TEST:
    for sp in os.listdir(fisher_spa):
        for line in test:
            if sp.split(".")[0] == line.split(" ")[0]:
                #print(transcr.split(".")[0], line.split(" ")[0])
                #print("war: ", fisher_spa+sp+"\n")
                #print("w: ", n_map_list[0]+"/"+sp+"\n")
                #print("wird: ", transcr,"\n")
                shutil.copyfile(fisher_spa+"/"+sp, n_map_list[0]+"/"+sp)
    for transcr in os.listdir(fisher_spa_tr):
        for line in test:
            if transcr.split(".")[0] == line.split(" ")[0]:
                #print(transcr.split(".")[0], line.split(" ")[0])
                #print("war: ", fisher_spa+stranscr+"\n")
                #print("w: ", n_map_list[0]+"/"+transcr+"\n")
                #print("wird: ", transcr,"\n")
                shutil.copyfile(fisher_spa_tr+"/"+transcr, n_map_list[0]+"/"+transcr)

    # DEV1:
    for sp in os.listdir(fisher_spa):
        for line in dev1:
            if sp.split(".")[0] == line.split(" ")[0]:
                #print(transcr.split(".")[0], line.split(" ")[0])
                #print("war: ", fisher_spa+sp+"\n")
                #print("w: ", n_map_list[0]+"/"+sp+"\n")
                #print("wird: ", transcr,"\n")
                shutil.copyfile(fisher_spa+"/"+sp, n_map_list[1]+"/"+sp)
    for transcr in os.listdir(fisher_spa_tr):
        for line in dev1:
            if transcr.split(".")[0] == line.split(" ")[0]:
                #print(transcr.split(".")[0], line.split(" ")[0])
                #print("war: ", fisher_spa+stranscr+"\n")
                #print("w: ", n_map_list[0]+"/"+transcr+"\n")
                #print("wird: ", transcr,"\n")
                shutil.copyfile(fisher_spa_tr+"/"+transcr, n_map_list[1]+"/"+transcr)

    # DEV2:
    for sp in os.listdir(fisher_spa):
        for line in dev2:
            if sp.split(".")[0] == line.split(" ")[0]:
                #print(transcr.split(".")[0], line.split(" ")[0])
                #print("war: ", fisher_spa+sp+"\n")
                #print("w: ", n_map_list[0]+"/"+sp+"\n")
                #print("wird: ", transcr,"\n")
                shutil.copyfile(fisher_spa+"/"+sp, n_map_list[2]+"/"+sp)
    for transcr in os.listdir(fisher_spa_tr):
        for line in dev2:
            if transcr.split(".")[0] == line.split(" ")[0]:
                #print(transcr.split(".")[0], line.split(" ")[0])
                #print("war: ", fisher_spa+stranscr+"\n")
                #print("w: ", n_map_list[0]+"/"+transcr+"\n")
                #print("wird: ", transcr,"\n")
                shutil.copyfile(fisher_spa_tr+"/"+transcr, n_map_list[2]+"/"+transcr)

    # TRAIN:
    for sp in os.listdir(fisher_spa):
        for line in train:
            if sp.split(".")[0] == line.split(" ")[0]:
                #print(transcr.split(".")[0], line.split(" ")[0])
                #print("war: ", fisher_spa+sp+"\n")
                #print("w: ", n_map_list[0]+"/"+sp+"\n")
                #print("wird: ", transcr,"\n")
                shutil.copyfile(fisher_spa+"/"+sp, n_map_list[3]+"/"+sp)
    for transcr in os.listdir(fisher_spa_tr):
        for line in train:
            if transcr.split(".")[0] == line.split(" ")[0]:
                #print(transcr.split(".")[0], line.split(" ")[0])
                #print("war: ", fisher_spa+stranscr+"\n")
                #print("w: ", n_map_list[0]+"/"+transcr+"\n")
                #print("wird: ", transcr,"\n")
                shutil.copyfile(fisher_spa_tr+"/"+transcr, n_map_list[3]+"/"+transcr)


if __name__ == "__main__":
    map_list = data["mapping"]
    n_map_list = data["datasets_devide"]
    fisher_spa = data["spain_audio"]
    fisher_spa_tr = data["spain_tr"]

    #map_test = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_test"
    #map_dev1 = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_dev"
    #map_dev2 = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_dev2"
    #map_train = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_train"
    #map_list = []
    #map_list.append(map_test)
    #map_list.append(map_dev1)
    #map_list.append(map_dev2)
    #map_list.append(map_train)    

    #n_test = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/TEST"
    #n_dev1 = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/DEV1"
    #n_dev2 = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/DEV2"
    #n_train = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/TRAIN"
    #n_map_list = []
    #n_map_list.append(n_test)
    #n_map_list.append(n_dev1)
    #n_map_list.append(n_dev2)
    #n_map_list.append(n_train)    

    #fisher_spa = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/fisher_spa/data/speech"
    #fisher_spa_tr = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/fisher_spa_tr/data/transcripts"
    #eng = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/"

    dataset_split(map_list, n_map_list, fisher_spa, fisher_spa_tr)




