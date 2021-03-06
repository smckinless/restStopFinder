// check for Geolocation support
if (navigator.geolocation) {
  console.log('Geolocation is supported!');
}
else {
  console.log('Geolocation is not supported for this Browser/OS version yet.');
}

data = {};

window.onload = function() {
  var startPos;
  var geoOptions = {
     timeout: 10 * 1000
  }

  var geoSuccess = function(position) {
    startPos = position;
    console.log(startPos.coords.latitude);
    //document.getElementById('startLat').innerHTML = startPos.coords.latitude;
    //document.getElementById('startLon').innerHTML = startPos.coords.longitude;

    
    data['lat'] = startPos.coords.latitude;
    data['lon'] = startPos.coords.longitude;

    $.ajax({
          type : "POST",
          url : "{{ url_for('find_stop') }}",
          data: JSON.stringify(data, null, '\t'),
          contentType: 'application/json;charset=UTF-8',
          success: function(result) {
              console.log(result);
          }

      });
    return result;

  };

  var geoError = function(error) {
    console.log('Error occurred. Error code: ' + error.code);
    // error.code can be:
    //   0: unknown error
    //   1: permission denied
    //   2: position unavailable (error response from location provider)
    //   3: timed out
  };

  navigator.geolocation.getCurrentPosition(geoSuccess, geoError, geoOptions);
  return data;
  //$(function() {
    //$('a#calculate').bind('click', function() {
    //$.getJSON('/_result', {
      //  lat: startPos.coords.latitude,
        //lon: startPos.coords.longitude
      //}/*, function(data) {
        //$("#result").text(data.result);
      //});*/
      //return false;
    //});


  //return false;
};