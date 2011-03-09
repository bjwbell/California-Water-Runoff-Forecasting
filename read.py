import csv

monthlyPrecipReader = csv.reader(open("MonthlyPrecip.csv"))
year = str(2000)
data = { }
stationIds = []

def adddata(stationId, year, month, precip):
    data[stationId] = { (year, month) : precip }

def appenddata(stationId, year, month, precip):
    data[stationId][(year, month)] = precip

def outputdata(filename, yr):
    writer = csv.writer(open(filename, 'w'))    
    datalist = []
    for stationId in stationIds:
        for month in ['01', '02', '03', '04']:
            datalist.append(data[stationId][(yr, month)])
    writer.writerow(datalist)

for row in monthlyPrecipReader:
    if len(row) < 3:
        print "len(row) < 3"
        print ', '.join(row)
        break
    stationId = row[2]
    date = row[4]
    if date.find('-') == -1:
        continue
    date_parts = date.split('-')
    yr = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]
    precip = row[5]
    if not stationId in stationIds:
        stationIds.append(stationId)
    if not (stationId in data.keys()):
        adddata(stationId, yr, month, precip)
    else:
        appenddata(stationId, yr, month, precip)
outputdata('formatted_data.csv', year)

    
