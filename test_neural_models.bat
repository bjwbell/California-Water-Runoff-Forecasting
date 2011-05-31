java -Xss4096k -cp weka.jar weka.classifiers.functions.MultilayerPerceptron -l models\neural_1st_third.model -p last -T full_data/split_by_runoff/AmericanRiv_Forecasts3.arff > results\neural_1st_third.out
java -Xss4096k -cp weka.jar weka.classifiers.functions.MultilayerPerceptron -l models\neural_2nd_third.model -p last -T full_data/split_by_runoff/AmericanRiv_Forecasts3.arff > results\neural_2nd_third.out
java -Xss4096k -cp weka.jar weka.classifiers.functions.MultilayerPerceptron -l models\neural_3rd_third.model -p last -T full_data/split_by_runoff/AmericanRiv_Forecasts3.arff > results\neural_3rd_third.out
echo "done"


python compare_neural_with_human.py