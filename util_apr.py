def load_human(filename):
    human_forecast = []
    f = open("results\\%s" % (filename))
    for l in f.readlines():
        human_forecast += [float(l.replace(",",""))]
    return human_forecast

def load_actual():
    actual = []
    f = open("results\\actual_2001_2010.txt")
    for l in f.readlines():
        actual += [float(l.replace(",",""))]
    return actual


def load_model_results(filename):
    model_results = []
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
        model_results.append(predicted)
    return model_results


def compare_model_with_human(model_name, model_results_filename):   
    human_apr1_forecast = load_human("human_ensemble_apr1_forecast_2001_2010.txt")
    human_forecast = human_apr1_forecast
    actual = load_actual()

    model_results = load_model_results(model_results_filename)
    mean_error_human = 0
    mean_error_model = 0
    total_error_human = 0
    total_error_model = 0
    idx = 0
    count_idx = 0
    i = 0
    forecast_date = "Apr 1"
    year = 1999
    for i in range(0, len(model_results)):
        year += 1
        print("Forecast Date %d, %s" % (year, forecast_date))
        print ("                Actual       Forecast       Error")
        error_human = abs(human_forecast[i] - actual[i])
        total_error_human += error_human
        print ("Human    %13d %13d %13d" % (actual[i], human_forecast[i], error_human))
        error_model = abs(model_results[i] - actual[i])
        total_error_model += error_model
        print ("%s  %13d %13d %13d" % (model_name, actual[i], model_results[i], error_model))
        count_idx += 1


        
    print("\n")
    print("Forecast Date %s" % (forecast_date))
    print("Total Error Human   %s" % (str(total_error_human)))
    print("Total Error %s %s" % (model_name, str(total_error_model)))
    print("Mean Error Human    %d" % (total_error_human / count_idx))
    print("Mean Error %s  %d" % (model_name, total_error_model / count_idx))

    print("\n")


