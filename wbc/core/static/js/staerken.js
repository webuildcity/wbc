google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart1);
function drawChart1() {
  var data = google.visualization.arrayToDataTable([
    ['Thema', 'Stimmen', { role: 'style' }],
    ['Bier-, Gasthaus und Brauereikultur',  75, 'color: #264ec4' ],
    ['Tourist. Sehenswürdigkeiten und Landschaft',  58, 'color: #264ec4' ],
    ['gutes Freizeitangebot und Veranstaltungen',  57, 'color: #264ec4' ],
    ['Starke Wirtschaft',  18, 'color: #264ec4'],
    ['gutes Angebot an Bildungseinrichtungen',  13, 'color: #264ec4' ],
    ['Freizeitangebote für Jugendliche',  10, 'color: #264ec4' ],

/*    
    ['ÖPNV und Zuganbindung',  10],
    ['Niedrige Lebenshaltungskosten',  8],
    ['Einkaufsmöglichkeiten',  7],
    ['Freundliche Menschen und ein gutes Miteinander',  5],
    ['Gute Außenanbindung',  4],
    ['Attraktive Kreisstadt',  3],
    ['Gute medizinische Versorgung',  2],
    ['Bürgernahe Kommunalpolitik',  1],
    ['Rotlicht',  1],
    ['Ruhige Wohngebiete',  1],
    ['Regionalradio',  0],
    ['Ausreichend Nutzflächen vorhanden',  0],
    ['Krankenhaus als gute Investition',  0],
    ['Stetiger Wandel',  0],
    ['Attraktiv für Ältere',  0],
 */

  ]);

  var options = {
    title: 'Anzahl der genannten Stärken des Landkreises',
    hAxis: {title: 'Stärken des Landkreises', titleTextStyle: {color: '#444'}
           },
    vAxis: {
          title: 'Anzahl der genannten Stärken'
        } 
 };
  

var chart = new google.visualization.ColumnChart(document.getElementById('chart_div1'));
  chart.draw(data, options);
}

// Reminder: you need to put https://www.google.com/jsapi in the head of your document or as an external resource on codepen //
