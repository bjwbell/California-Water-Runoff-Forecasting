#!/bin/sh
rm formatted_data.arff
python read.py
java -cp weka.jar weka.classifiers.functions.LinearRegression -t /home/bjwbell/California-Water-Runoff-Forecasting/formatted_data.arff > linear_model.out
cat linear_model.out

java -cp weka.jar weka.classifiers.functions.LinearRegression -t /home/bjwbell/California-Water-Runoff-Forecasting/American.arff > linear_model.out
cat linear_model.out