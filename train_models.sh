#!/bin/sh
#rm formatted_data.arff
#python read.py
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data/AmericanRiverInfo_ALL.arff > models/linear_all.model &
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data/AmericanRiv_TrainNoWaterYear.arff > models/linear_jun.model &


java -cp weka.jar weka.classifiers.functions.LinearRegression -t data/AmericanRiv_TrainThruJan.arff > models/linear_jan.model &
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data/AmericanRiv_TrainThruFeb.arff > models/linear_feb.model &
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data/AmericanRiv_TrainThruMar.arff > models/linear_mar.model & 
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data/AmericanRiv_TrainThruApr.arff > models/linear_apr.model &
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data/AmericanRiv_TrainThruMay.arff > models/linear_may.model 
echo "done"