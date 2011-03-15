import csv

monthlyPrecipReader = csv.reader(open("MonthlyPrecip.csv"))
year = str(2000)
data = { }
stationIds = []
flow_data = {}
def adddata(stationId, year, month, precip):
    data[stationId] = { (year, month) : precip }

def appenddata(stationId, year, month, precip):
    data[stationId][(year, month)] = precip

def outputdata(filename, yr):
    writer = csv.writer(open(filename, 'w'))    
    datalist = []
    for stationId in stationIds:
        for month in ['01', '02', '03', '04']:
            if (yr, month) in data[stationId]:
                datalist.append(data[stationId][(yr, month)])
            else:
                print "(%s, %s) missing from %s" % (yr, month, stationId)
                datalist.append(0)
    datalist.append(flow_data[(yr, '06')])
    writer.writerow(datalist)

def read_data():
    row_idx = 0
    for row in monthlyPrecipReader:
        row_idx = row_idx + 1
        #print "reading monthly data"
        if len(row) < 3:
            print "len(row) < 3"
            print ', '.join(row)
            print "row_idx %i" % (row_idx)
            continue
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

amf_file_name = "AMF Full Natural Flow.csv"
def read_river_flow(file_name):
    flow_data = {}
    monthly_river_flow_reader = csv.reader(open(file_name))
    row_idx = 0
    for row in monthly_river_flow_reader:
        row_idx = row_idx + 1
        if len(row) < 3:
            print "len(row) < 3"
            print ', '.join(row)
            print "row_idx %i" % (row_idx)
            continue
        stationId = row[0]
        date = row[1]
        if date.find('-') == -1:
            continue
        date_parts = date.split('-')
        yr = date_parts[0]
        month = date_parts[1]
        day = date_parts[2]
        flow = row[2]
        flow_data[(yr, month)] = flow
    return flow_data

read_data()                
flow_data = read_river_flow(amf_file_name)

outputdata('formatted_data.csv', year)
print 'finished'
    
