import os
#import sh
import sox #https://github.com/rabitt/pysox

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
    
def split_files(folder,mapping):

    with open(mapping, "r") as m:
        mapping = m.readlines()
        mapp = {}
        for i in range(len(mapping)):
            if mapping[i].split()[0] not in mapp.keys():
                mapp[mapping[i].split()[0]] = []
            mapp[mapping[i].split()[0]].append(mapping[i].split()[-1])
    print(mapp)   

    files = {}
    for key in mapp:
        for fi in os.listdir(folder):
            if key == fi.split(".")[0] and fi.split(".")[-1] == "tdf":
                with open(folder+"/"+fi, "r") as f:
                    info = f.readlines()[3:]
                    files[key] = []
                    for li in info:
                        one = []
                        tup = []
                        tup.append(li.split()[2])
                        tup.append(li.split()[3])
                        one.append(li.split()[1])  
                        one.append(tup)
                        files[key].append(one) 
        

    print(files)
    
    new_map = {}
    for key in mapp:
        new_map[key] = []
        for el in mapp[key]:
            a = el.split("_")
            ele_list = []
            for ele in a:
                try: 
                    x = files[key][int(ele)]
                    if len(ele_list) == 0:
                        ele_list.append(x)
                    else:
                        ele_list[0][1][1] = x[1][1]
        
                except:
                    pass 
            if ele_list != []:
                new_map[key].append(ele_list)  

    print(new_map)                

    for key in new_map:
        for fi in os.listdir(folder):
            print("here ", key,  fi.split(".")[0])
            if key == fi.split(".")[0] and fi.split(".")[-1] == "wav":
                for i in range(len(new_map[key])):
                    a = float(new_map[key][i][0][1][0])*0.1
                    b = float(new_map[key][i][0][1][1])*0.1
                    print(a,b)
                    out = fi.split(".")[0]+"_"+ str(i)+".wav"
                    print("out: ", out) 
                    tfm = sox.Transformer()
                    if a<b:
                        tfm.trim(a,b)
                        tfm.build(folder+"/"+fi, folder+"/splitted/"+out)


if __name__ == "__main__":
    n_test = data["datasets_devide"][0]
    n_dev1 = data["datasets_devide"][1]
    n_dev2 = data["datasets_devide"][2]
    n_train = data["datasets_devide"][3]
    #n_test = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/TEST"
    #n_dev1 = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/DEV1"
    #n_dev2 = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/DEV2"
    #n_train = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/TRAIN"
    map_test = data["mapping"][0]
    map_dev1 = data["mapping"][1]
    map_dev2 = data["mapping"][2]
    map_train = data["mapping"][3]
    
    #map_test = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_test"
    #map_dev1 = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_dev"
    #map_dev2 = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_dev2"
    #map_train = "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/mapping/fisher_train"
    #pro =  "/home/tatiana/Desktop/5_Semester/Speech_Recognition/ueb_3/pro"
    split_files(n_test,map_test)
    split_files(n_dev1,map_dev1)
    split_files(n_dev2,map_dev2)
    split_files(n_train,map_train)

