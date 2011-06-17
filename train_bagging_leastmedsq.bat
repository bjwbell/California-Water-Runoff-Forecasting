java -Xss4096k -cp weka.jar weka.filters.unsupervised.attribute.Remove -R 1 -i full_data/split_by_runoff/AmericanRiv_Train.arff > tmp\tmp.arff
java -Xss4096k -cp weka.jar weka.classifiers.meta.Bagging -P 100 -S 1 -I 10 -W weka.classifiers.functions.LeastMedSq  -t tmp\tmp.arff -d models\bagging_leastmedsq.model -- -S 10 -G 0 > models\bagging_linearmedsq.out
del tmp\tmp.arff
