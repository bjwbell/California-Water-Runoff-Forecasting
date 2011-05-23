java -cp weka.jar weka.classifiers.functions.LinearRegression -t AmericanRiverInfo_ALL.arff > linear_model.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -t AmericanRiv_TrainNoWaterYear.arff > linear_model2.out
echo "done"