#!/bin/sh
#rm formatted_data.arff
#python read.py
java -cp weka.jar weka.classifiers.functions.LinearRegression -t /home/bjwbell/California-Water-Runoff-Forecasting/AmericanRiverInfo_ALL.arff > linear_model.out
cat linear_model.out

java -cp weka.jar weka.classifiers.functions.LinearRegression -t /home/bjwbell/California-Water-Runoff-Forecasting/AmericanRiv_Train.arff > linear_model2.out
cat linear_model2.out