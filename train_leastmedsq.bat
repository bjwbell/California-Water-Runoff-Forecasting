java -Xss4096k -cp weka.jar weka.filters.unsupervised.attribute.Remove -R 1 -i full_data/split_by_runoff/AmericanRiv_Train.arff > tmp\linearmedsq.arff
java -Xss4096k -cp weka.jar weka.classifiers.functions.LeastMedSq -t tmp\linearmedsq.arff -d models\linearmedsq.model > models\linearmedsq.out
del tmp\linearmedsq.arff
