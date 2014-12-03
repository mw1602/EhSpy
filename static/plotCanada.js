// var map;

function initialize() {
  var mapOptions = {
    zoom: 4,
    center: { lat: 40.789574, lng: -99.225230},
    mapTypeId: google.maps.MapTypeId.TERRAIN
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

 var contentString = '<div id="content">'+
     '<div id="siteNotice">'+
     '</div>'+
     '<h1 id="firstHeading" class="firstHeading">Spot the Canadian!</h1>'+
     '<div id="bodyContent">'+
     '<p>Every time someone in the US' +
     ' tweets a sentence-final <i>eh</i>, ' +
     'feel a little bit of Canadian pride.</p>'+

     '</div>'+
     '</div>';

  var infowindow = new google.maps.InfoWindow({
      content: contentString,
      position: { lat: 51.716896, lng: -43.807132},


      draggable: true,
      maxWidth: 200
  });

  infowindow.open(map)
  var infowindow = new google.maps.InfoWindow({
      // content: childSnapshot.child(2).val()
    })
  // Set the firebase reference
  var coordsRef = new Firebase('https://expat-finder.firebaseio.com/coordinates/');

  coordsRef.on('child_added', function(childSnapshot) {
    // code to handle new child.
    var lng = childSnapshot.child(1).val()
    var lat = childSnapshot.child(0).val()
    

    var icon = new google.maps.MarkerImage(
        'images/canadaflag.png',
        new google.maps.Size(40,40),    // size of the image
        new google.maps.Point(0,0), // origin, in this case top-left corner
        new google.maps.Point(5, 52)    // anchor, i.e. the point half-way along the bottom of the image
    );
    // var icon = 'images/canadaflag.png'
    var marker = new google.maps.Marker({
      position: {lat: lat, lng: lng},
      icon: icon,
      map: map,
    });

    google.maps.event.addListener(marker,'click', function() {
      infowindow.setContent(childSnapshot.child(2).val())
      infowindow.open(map,this);})
  });
}

google.maps.event.addDomListener(window, 'load', initialize);