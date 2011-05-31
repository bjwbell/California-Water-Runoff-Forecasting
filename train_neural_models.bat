REM java -Xss4096k -cp weka.jar weka.filters.unsupervised.attribute.Remove -R 1 -i full_data/split_by_runoff/AmericanRiv_Train_1st_third.arff > tmp\1st_third.arff
REM java -Xss4096k -cp weka.jar weka.classifiers.functions.MultilayerPerceptron -L 0.03 -M 0.1 -N 3000 -V 0 -S 0 -E 20 -H "180, 150, 100" -R -t tmp\1st_third.arff -d models\neural_1st_third.model > models\neural_1st_third.out
REM del tmp\1st_third.arff


REM java -Xss4096k -cp weka.jar weka.filters.unsupervised.attribute.Remove -R 1 -i full_data/split_by_runoff/AmericanRiv_Train_2nd_third.arff > tmp\2nd_third.arff
REM java -Xss4096k -cp weka.jar weka.classifiers.functions.MultilayerPerceptron -L 0.03 -M 0.1 -N 3000 -V 0 -S 0 -E 20 -H "180, 150, 100" -R -t tmp\2nd_third.arff -d models\neural_2nd_third.model > models\neural_2nd_third.out
REM del tmp\2nd_third.arff

java -Xss4096k -cp weka.jar weka.filters.unsupervised.attribute.Remove -R 1 -i full_data/split_by_runoff/AmericanRiv_Train_3rd_third.arff > tmp\3rd_third.arff
java -Xss4096k -cp weka.jar weka.classifiers.functions.MultilayerPerceptron -L 0.03 -M 0.1 -N 3000 -V 0 -S 0 -E 20 -H "180, 150, 100" -R -t tmp\3rd_third.arff -d models\neural_3rd_third.model > models\neural_3rd_third.out
del tmp\3rd_third.arff
