java -cp weka.jar weka.classifiers.functions.LinearRegression -l models\linear_all.model -p last -T test_data\AmericanRiverInfo_ALL_Test.arff > results\linear_all.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -l models\linear_jun.model -p last -T test_data\AmericanRiv_TrainNoWaterYear_Test.arff > results\linear_jun.out

java -cp weka.jar weka.classifiers.functions.LinearRegression -l models\linear_jan.model -p last -T test_data\AmericanRiv_TrainThruJan_Test.arff > results\linear_jan.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -l models\linear_feb.model -p last -T test_data\AmericanRiv_TrainThruFeb_Test.arff > results\linear_feb.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -l models\linear_mar.model -p last -T test_data\AmericanRiv_TrainThruMar_Test.arff > results\linear_mar.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -l models\linear_apr.model -p last -T test_data\AmericanRiv_TrainThruApr_Test.arff > results\linear_apr.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -l models\linear_may.model -p last -T test_data\AmericanRiv_TrainThruMay_Test.arff > results\linear_may.out
echo "done"
