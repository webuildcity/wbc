google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart1);
function drawChart1() {
  var data = google.visualization.arrayToDataTable([
    ['Thema', 'Stimmen', { role: 'style' }],
    ['Es gibt mehr (jugendgerechte) Freizeitangebote',  69, 'color: #ffff00' ],
    ['Der Landkreis verfügt über eine gute Infrastruktur',  68, 'color: #ffff00' ],
    ['Die Schul- und Unterrichtssituation ist verbessert',  24, 'color: #ffff00' ],
    ['Die öffentlichen Verkehrsmittel sind ausgebaut',  22, 'color: #ffff00'],
    ['Es stehen bessere Aus- und Weiterbildungsmöglichkeiten zur Verfügung',  21, 'color: #ffff00' ],
    ['Die Innenstädte sind belebt mit einer Vielfalt von Geschäften',  17, 'color: #ffff00' ],
    ['Der Landkreis ist familienfreundlich',  16, 'color: #ffff00' ],
    ['Es gibt ausreichend attraktive Arbeitsplätze',  15, 'color: #ffff00' ],
    ['Der Landkreis ist attraktiv für die BewohnerInnen',  9, 'color: #ffff00' ],
    ['Die Kinderbetreuungsangebote sind ausgebaut',  8, 'color: #ffff00' ],

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