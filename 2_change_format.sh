#!/bin/sh

mkdir "$PWD"+/TEST
mkdir "$PWD"+/TEST/splitted

mkdir "$PWD"+/DEV1
mkdir "$PWD"+/DEV1/splitted

mkdir "$PWD"+/DEV2
mkdir "$PWD"+/DEV2/splitted

mkdir "$PWD"+/TRAIN
mkdir "$PWD"+/TRAIN/splitted

for i in $(ls $PWD/TEST/*.sph)
do 
    chmod +x $i
    echo $i
    ~/MyPython/Other/sph2pipe/sph2pipe_v2.5/sph2pipe -f wav $i ${i%.*}.wav
done

for i in $(ls $PWD/DEV1/*.sph)
do 
    chmod +x $i
    echo $i
    ~/MyPython/Other/sph2pipe/sph2pipe_v2.5/sph2pipe -f wav $i ${i%.*}.wav
done

for i in $(ls mkdir "$PWD"+/TRAIN/DEV2/*.sph)
do 
    chmod +x $i
    echo $i
    ~/MyPython/Other/sph2pipe/sph2pipe_v2.5/sph2pipe -f wav $i ${i%.*}.wav
done

for i in $(ls mkdir "$PWD"+/TRAIN/*.sph)
do 
    chmod +x $i
    echo $i
    ~/MyPython/Other/sph2pipe/sph2pipe_v2.5/sph2pipe -f wav $i ${i%.*}.wav
done
