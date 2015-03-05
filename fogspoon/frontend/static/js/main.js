
function init_map() {
    var map_center = [37.761234,-122.445566]
    var map = L.map('map').setView(map_center, 13);
    mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
    mapquestLink = '<a href="http://www.mapquest.com//">MapQuest</a>';
    mapquestPic = '<img src="http://developer.mapquest.com/content/osm/mq_logo.png">';
    L.tileLayer(
        'http://otile{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
        attribution: '&copy; '+mapLink+'. Tiles courtesy of '+mapquestLink+mapquestPic,
        maxZoom: 18,
        subdomains: '1234',
    }).addTo(map);
}
