google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart1);
function drawChart1() {
  var data = google.visualization.arrayToDataTable([
    ['Thema', 'Stimmen', { role: 'style' }],
    ['Tote Innenstädte',  62, 'color: #cc3333' ],
    ['ÖPNV Angebot',  41, 'color: #cc3333' ],
    ['Defizite in der  Infrastruktur (Internet, Zustand der Straßen)',  29, 'color: #cc3333' ],
    ['Kriminalität und Drogen',  27, 'color: #cc3333'],
    ['Studienmöglichkeiten und Begabtenförderung',  25, 'color: #cc3333' ],
    ['Defizite in der Wirtschaft (Arbeitsplätze)',  23, 'color: #cc3333' ],
    ['Mangel an Veranstaltungen und Kulturangeboten',  19, 'color: #cc3333' ],
    ['Defizite bei den Freizeitangeboten für Jugendliche',  14, 'color: #cc3333' ],
    ['Zustand öffentlicher Orte',  8, 'color: #cc3333' ],
    ['Brauereien schließen',  6, 'color: #cc3333' ],
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
