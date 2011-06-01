def load_human(filename):
    human_forecast = []
    f = open("results\\%s" % (filename))
    for l in f.readlines():
        human_forecast += [float(l.replace(",",""))]
    return human_forecast
             
def load_dagging_neural():
    filename = "dagging_neural.out"
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

dagging_neural = load_dagging_neural()
mean_error_human = [0, 0, 0]
mean_error_dagging = [0, 0, 0, 0]
total_error_human = [0, 0, 0]
total_error_dagging = [0, 0, 0, 0]
idx = 0
count_idx = [0, 0, 0, 0]
i = 0
forecast_date = ["Feb 1", "Mar 1", "Apr 1", "May 1"]
year = 1999
for i in range(0, len(dagging_neural)):
    idx = i % 4
    if (i % 4 == 0): year += 1
    print("Forecast Date %d, %s" % (year, forecast_date[idx]))
    print ("                Actual       Forecast       Error")
    if idx < 3:
        error_human = abs(human_forecast[idx][int(i / 4)] - actual[int(i/4)])
        total_error_human[idx] += error_human
        print ("Human    %13d %13d %13d" % (actual[int(i/4)], human_forecast[idx][int(i / 4)], error_human))
    error_dagging = abs(dagging_neural[i] - actual[int(i/4)])
    total_error_dagging[idx] += error_dagging
    print ("Dagging  %13d %13d %13d" % (actual[int(i/4)], dagging_neural[i], error_dagging))
    count_idx[idx] += 1


for idx in range(0, 4):
    print("\n")
    print("Forecast Date %s" % (forecast_date[idx]))
    if idx < 3: print("Total Error Human   %s" % (str(total_error_human[idx])))
    print("Total Error Dagging %s" % (str(total_error_dagging[idx])))
    if idx < 3: print("Mean Error Human    %d" % (total_error_human[idx] / count_idx[idx]))
    print("Mean Error Dagging  %d" % (total_error_dagging[idx] / count_idx[idx]))

    print("\n")



