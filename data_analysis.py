
data_list = []

import csv
with open('/Users/sumon/TestAnalysisData.csv') as datafile:
    fh=csv.reader(datafile)
    for row in fh:
        data_list.append(row)
#print(data_list)
chart_data = [data_list[0]]
#print(chart_data)
for row in data_list[1:]:
    #print(row)
    number_of_tests = int(row[1])
    #print(number_of_tests)
    number_of_failed_tests= int(row[2])
    #print(number_of_failed_tests)
    chart_data.append([row[0], number_of_tests, number_of_failed_tests])
#print(chart_data[0])
#Create the Chart Data
# create the html for the chart
from string import Template

# first substitution is the header, the rest is the data
htmlString = Template("""<html><head><script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart(){
      var data = google.visualization.arrayToDataTable([
      $labels,
      $data
      ],
      false);

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
<div id = 'chart_div' style='width:800; height:600'><div>
</body>

</html>""")


# substitute the data into the template



chart_data_str = ''
for row in chart_data[1:]:
    #print(row)
    chart_data_str += '%s,\n'%row
#print(chart_data_str)
completed_html= htmlString.substitute(labels = chart_data[0], data = chart_data_str)
with open('/Users/sumon/Chart_test_analysis.html', 'w') as f:
    f.write(completed_html)
