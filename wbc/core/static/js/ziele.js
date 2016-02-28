google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart1);
function drawChart1() {
  var data = google.visualization.arrayToDataTable([
    ['Thema', 'Stimmen', { role: 'style' }],
    ['Bier-, Gasthaus und Brauereikultur',  75, 'color: #444' ],
    ['Tourist. Sehenswürdigkeiten und Landschaft',  58, 'color: #444' ],
    ['gutes Freizeitangebot und Veranstaltungen',  57, 'color: #444' ],
    ['Starke Wirtschaft',  18, 'color: #444'],
    ['gutes Angebot an Bildungseinrichtungen',  13, 'color: #444' ],
    ['Freizeitangebote für Jugendliche',  10, 'color: #444' ],

  ]);

  var options = {
    title: 'Anzahl der genannten Ziele des Landkreises',
    hAxis: {title: 'Ziele des Landkreises', 
            titleTextStyle: {color: '#444'},
            },
    vAxis: {
          title: 'Anzahl der genannten Ziele'
        } 
 };
  

var chart = new google.visualization.ColumnChart(document.getElementById('chart_div1'));
  chart.draw(data, options);
}

// Reminder: you need to put https://www.google.com/jsapi in the head of your document or as an external resource on codepen //