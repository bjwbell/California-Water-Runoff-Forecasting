java -Xss4096k -cp weka.jar weka.classifiers.meta.Dagging -l models\dagging_neural_net.model -p last -T full_data/split_by_runoff/AmericanRiv_Forecasts3.arff > results\dagging_neural.out

python compare_dagging_with_human.py