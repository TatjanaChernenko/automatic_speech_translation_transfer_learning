import json
# mapping: /resources/corpora/multilingual/fisher_ch_spa-eng/data/mapping/fisher_*
# spain_audio: /resources/corpora/monolingual/annotated/fisher_spa
# spain_tr: /resources/corpora/monolingual/annotated/fisher_spa_tr/
# datasets_devide: your output_direction

data = {"mapping":["/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_test",
                 "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_dev",
                 "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_dev2",
                 "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_train"],
        "spain_audio":"/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/fisher_spa/data/speech",
        "spain_tr":"/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/fisher_spa_tr/data/transcripts",
        "datasets_devide":["/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/TEST",
                         "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/DEV1",
                         "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/DEV2",
                         "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/TRAIN"]
        }

s1 = data["datasets_devide"][0]+"/splitted"
s2 = data["datasets_devide"][1]+"/splitted"
s3 = data["datasets_devide"][2]+"/splitted"
s4 = data["datasets_devide"][3]+"/splitted"

data["splitted"] = []
data["splitted"].append(s1)
data["splitted"].append(s2)
data["splitted"].append(s3)
data["splitted"].append(s4)


with open('config.json', 'w') as outfile:
    json.dump(data, outfile)