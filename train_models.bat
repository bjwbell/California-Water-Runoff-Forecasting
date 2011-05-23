java -cp weka.jar weka.classifiers.functions.LinearRegression -t data\AmericanRiverInfo_ALL.arff -d models\linear_all.model > models\linear_all.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data\AmericanRiv_TrainNoWaterYear.arff -d models\linear_jun.model > models\linear_jun.out

java -cp weka.jar weka.classifiers.functions.LinearRegression -t data\AmericanRiv_TrainThruJan.arff -d models\linear_jan.model > models\linear_jan.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data\AmericanRiv_TrainThruFeb.arff -d models\linear_feb.model > models\linear_feb.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data\AmericanRiv_TrainThruMar.arff -d models\linear_mar.model > models\linear_mar.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data\AmericanRiv_TrainThruApr.arff -d models\linear_apr.model > models\linear_apr.out
java -cp weka.jar weka.classifiers.functions.LinearRegression -t data\AmericanRiv_TrainThruMay.arff -d models\linear_may.model > models\linear_may.out
echo "done"