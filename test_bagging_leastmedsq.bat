REM the model was generated using the weka gui and the following model options
REM Bagging -P 100 -S 1 -I 10 -W weka.classifiers.functions.LeastMedSq -- -S 10 -G 0
REM with the .\data\AmericanRiv_Train.arff file (the water year attribute was removed).

java -Xss4096k -cp weka.jar weka.classifiers.meta.Bagging -l models\bagging_leastmedsq.model -p last -T full_data/split_by_runoff/AmericanRiv_Forecasts3.arff > results\bagging_leastmedsq.out

python compare_bagging_leastmedsq_with_human.py