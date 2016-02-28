google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart1);
function drawChart1() {
  var data = google.visualization.arrayToDataTable([
    ['Thema', 'Stimmen', { role: 'style' }],
    ['Bier-, Gasthaus und Brauereikultur',  75, 'color: #e5e4e2' ],
    ['Tourist. Sehenswürdigkeiten und Landschaft',  58, 'color: #e5e4e2' ],
    ['gutes Freizeitangebot und Veranstaltungen',  57, 'color: #e5e4e2' ],
    ['Starke Wirtschaft',  18, 'color: #e5e4e2'],
    ['gutes Angebot an Bildungseinrichtungen',  13, 'color: #e5e4e2' ],
    ['Freizeitangebote für Jugendliche',  10, 'color: #e5e4e2' ],

  ]);

  var options = {
    title: 'Anzahl der genannten Schwächen des Landkreises',
    hAxis: {title: 'Schwächen des Landkreises', titleTextStyle: {color: '#444'}
           },
    vAxis: {
          title: 'Anzahl der genannten Schwächen'
        } 
 };
  

var chart = new google.visualization.ColumnChart(document.getElementById('chart_div1'));
  chart.draw(data, options);
}

// Reminder: you need to put https://www.google.com/jsapi in the head of your document or as an external resource on codepen //
