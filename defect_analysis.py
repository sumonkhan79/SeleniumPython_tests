'''import requests
url = 'jira.<company Name>/rest/api/atest/search?jql=reporter=dwestervelid'
response = requests.get(url)'''
import json
json_data = open('/Users/sumon/JiraJsonData.json')
#print(json_data)
data = json.load(json_data)
status_count = {}
for project in data['projects']:
    for issue in project['issues']:
        #print(issue)
        status = issue['status']
        if not status in status_count.keys():
            status_count[status] = 1
        else:
            status_count[status]=status_count[status] + 1
#print(status_count)

from string import Template

template_string = Template("""<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Status', 'Number of Issues'],
          $my_data
        ]);

        var options = {
          title: 'Issues by Status'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart" style="width: 900px; height: 500px;"></div>
  </body>
</html>""")

formatted_data = ''

for stat in status_count.keys():
    formatted_data += "['%s',%s],\n"%(stat,status_count[stat])

html_string = template_string.substitute(my_data=formatted_data)

with open('/Users/sumon/desktop/DefectChart.html','w') as f:
    f.write(html_string)