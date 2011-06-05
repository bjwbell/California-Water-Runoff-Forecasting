java -Xss4096k -cp weka.jar weka.classifiers.functions.LeastMedSq -l models\linearmedsq.model -p last -T full_data/split_by_runoff/AmericanRiv_Forecasts3.arff > results\leastmedsq.out

python compare_leastmedsq_with_human.py