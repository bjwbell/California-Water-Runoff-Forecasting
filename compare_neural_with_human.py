def load_human(filename):
    human_forecast = []
    f = open("results\\%s" % (filename))
    for l in f.readlines():
        human_forecast += [float(l.replace(",",""))]
    return human_forecast
             
def load_neural(filename):
    neural = []
    f = open("results\\%s" % (filename))
    in_data = False
    for l in f.readlines():
        if l.count("inst#") > 0:
            in_data = True
            continue
        if not in_data:
            continue
        d = l.split()
        if len(d) == 0:
            break
        actual = float(d[1].replace(",", ""))
        predicted = float(d[2].replace(",", ""))
        neural.append(predicted)
    return neural


def load_neural_1st_third():
    return load_neural("neural_1st_third.out")

def load_neural_2nd_third():
    return load_neural("neural_2nd_third.out")

def load_neural_3rd_third():
    return load_neural("neural_3rd_third.out")

def load_actual():
    actual = []
    f = open("results\\actual_2000_2008.txt")
    for l in f.readlines():
        actual += [float(l.replace(",",""))]
    return actual
    
             
human_feb1_forecast = load_human("human_ensemble_feb1_forecast_2000_2008.txt")
human_mar1_forecast = load_human("human_ensemble_mar1_forecast_2000_2008.txt")
human_apr1_forecast = load_human("human_ensemble_apr1_forecast_2000_2008.txt")
human_forecast = [human_feb1_forecast, human_mar1_forecast, human_apr1_forecast]
actual = load_actual()

neural_1st_third = load_neural_1st_third()
neural_2nd_third = load_neural_2nd_third()
neural_3rd_third = load_neural_3rd_third()

mean_error_human = [0, 0, 0]
mean_error_neural = [0, 0, 0, 0]
total_error_human = [0, 0, 0]
total_error_neural = [0, 0, 0, 0]

total_error_1st_neural = [0, 0, 0, 0]
total_error_2nd_neural = [0, 0, 0, 0]
total_error_3rd_neural = [0, 0, 0, 0]
idx = 0
count_idx = [0, 0, 0, 0]
i = 0
for i in range(0, len(neural_1st_third)):
    idx = i % 4
    if idx < 3:
        total_error_human[idx] += abs(human_forecast[idx][int(i / 4)] - actual[int(i/4)])
    total_error_neural[idx] += abs((neural_3rd_third[i] + neural_2nd_third[i] + neural_1st_third[i])/3.0 - actual[int(i/4)])
    total_error_1st_neural[idx] += abs(neural_1st_third[i] - actual[int(i/4)])
    total_error_2nd_neural[idx] += abs(neural_2nd_third[i] - actual[int(i/4)])
    total_error_3rd_neural[idx] += abs(neural_3rd_third[i] - actual[int(i/4)])
    count_idx[idx] += 1

forecast_date = ["Feb 1", "Mar 1", "Apr 1", "May 1"]
for idx in range(0, 4):
    print("\n")
    print("Forecast Date %s" % (forecast_date[idx]))
    if idx < 3: print("Total Error Human %s" % (str(total_error_human[idx])))
    print("Total Error Neural %s" % (str(total_error_neural[idx])))
    print("Total Error 1st Neural %s" % (str(total_error_1st_neural[idx])))
    print("Total Error 2nd Neural %s" % (str(total_error_2nd_neural[idx])))
    print("Total Error 3rd Neural %s" % (str(total_error_3rd_neural[idx])))
    if idx < 3: print("Mean Error Human %d" % (total_error_human[idx] / count_idx[idx]))
    print("Mean Error Neural %d" % (total_error_neural[idx] / count_idx[idx]))
    print("Mean Error 1st Neural %d" % (total_error_1st_neural[idx] / count_idx[idx]))
    print("Mean Error 2nd Neural %d" % (total_error_2nd_neural[idx] / count_idx[idx]))
    print("Mean Error 3rd Neural %d" % (total_error_3rd_neural[idx] / count_idx[idx]))
    print("\n")



