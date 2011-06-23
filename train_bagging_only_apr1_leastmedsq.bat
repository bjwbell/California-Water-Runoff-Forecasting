java -cp weka.jar weka.classifiers.meta.Bagging -P 100 -S 1 -I 10 -W weka.classifiers.functions.LeastMedSq -t data\AmericanRiv_TrainThruApr.arff -d models\bagging_only_apr1_leastmedsq.model > models\bagging_only_apr1_leastmedsq.out

