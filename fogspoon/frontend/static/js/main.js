
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) {
      return typeof args[number] != "undefined"
        ? args[number]
        : match
      ;
    });
  };
}

var Map;
var Markers_Layer;
var Default_Location = [37.761234,-122.445566]
var Film_List;

var marker_colors = ["red", "blue", "green", "purple", "orange", "beige", "pink", "gray", "black"];

function marker_color() {
    return marker_colors[Math.floor(Math.random()*marker_colors.length)];
}

function clear_map() {
    Markers_Layer.clearLayers();
    $("#filter").val("");
}

function add_film(film_id) {
    $.getJSON("/api/film/"+ film_id +"?format=geo_json", function(data) {
        var color = marker_color();
        var geojson = L.geoJson(data.data, {
            onEachFeature: function (feature, layer) {
                layer.bindPopup(
                    "<b>{0}</b><br/>{1}<br/>{2}".format(
                        feature.properties.film,
                        feature.properties.place_name,
                        feature.properties.fun_fact));
            },
            style: function (feature) {
                return {color: color};
            },
            pointToLayer: function (feature, latlng) {
                var icon = L.AwesomeMarkers.icon({icon: "dot", markerColor: color});
                return L.marker(latlng, {icon: icon});
            },
        });
        //geojson.addTo(Map);
        Markers_Layer.addLayer(geojson);
    });
}

function init_search() {
    $("#filter").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/api/films",
                dataType: "json",
                data: {
                    q: request.term
                },
                success: function(data) {
                    response(data.data);
                }
            });
        },
        minLength: 2,
        select: function(event, ui) {
            add_film(ui.item.id);
        },
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
            $("#filter").val("");
        }
    });
}

function init_map() {
    map_center = Default_Location;
    Map = L.map("map",{
        "attributionControl": false,
    }).setView(map_center, 13);

    L.control.attribution({
        prefix: '<a href="http://github.com/tkalus/fog-spoon">FogSpoon</a> | <a href="http://leafletjs.com" title="A JS Library for interactive maps.">Leaflet</a>',
    }).addTo(Map);

    mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
    mapquestLink = '<a href="http://www.mapquest.com">MapQuest</a>';
    mapquestPic = '<img src="http://developer.mapquest.com/content/osm/mq_logo.png">';
    L.tileLayer(
        'http://otile{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
        attribution: '&copy; '+mapLink+'. Tiles courtesy of '+mapquestLink+mapquestPic,
        maxZoom: 18,
        subdomains: "1234",
    }).addTo(Map);

    Markers_Layer = new L.LayerGroup();
    Markers_Layer.addTo(Map);

}

$(window).load(function() {
    init_map();
    init_search();
    $("#clear-map").click(function() {
        clear_map();
    });
});

