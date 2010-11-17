define(['models/Tramo', './TramoView'], function(Tramo, TramoView) {

    var CarreteraDetailView = Backbone.View.extend({

        tagName: 'div',

        id: 'details',

        template: _.template($('#details-tmpl').html()),

        events: {},

        initialize: function(params) {
            _.bindAll(this, 'render', 'renderDetails');

            this.model.bind('change', this.render);

            this.animationSpeed = params && params.animationSpeed || 500;
        },

        render: function() {
            var previousDetails = $('#details');
            if (previousDetails != undefined && previousDetails.length > 0) {
                var that = this;
                previousDetails.slideUp(this.animationSpeed, function() {
                    previousDetails.remove();
                    that.renderDetails();
                });
            } else {
                this.renderDetails();
            }
        },

        renderDetails: function() {
            var that = this;
            var $this = $(this.el)
                .append(this.template(this.model.toJSON()))
                .css({display: 'none'})
                .appendTo($('#searchResults'));
            _.each(this.model.get('tramos'), this.addTramo, this);
            // Show section
            $this.slideDown(this.animationSpeed, function() {
                // Render map
                var tramo = that.model.get('tramos')[0];
                var latlng = that.calculateMapCenter(tramo.latitud_inicio, tramo.longitud_inicio,
                        tramo.latitud_fin, tramo.longitud_fin);
                var options = {
                    zoom: 8,
                    center: latlng,
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                };
                var map = new google.maps.Map(that.$('#map')[0], options);
                var directionDisplay = new google.maps.DirectionsRenderer();
                directionDisplay.setMap(map);
                that.addTramoMarkers(map, directionDisplay, tramo);
            });
        },

        addTramo: function(element, index) {
            var tramo = new Tramo(element);
            var view = new TramoView({model: tramo});
            this.$('#tramosTable').append(view.render(index).el);
        },

        calculateMapCenter: function(latStart, lonStart, latEnd, lonEnd) {
            var dLat = Math.abs(latStart - latEnd) / 2.0;
            var latitude = latStart > latEnd ? latStart - dLat : latStart + dLat;
            var dLon = Math.abs(lonStart - lonEnd) / 2.0;
            var longitude = lonStart > lonEnd ? lonStart - dLon : lonEnd + dLon;
            return new google.maps.LatLng(latitude, longitude);
        },

        addTramoMarkers: function(map, directionDisplay, tramo) {
            var latlngStart = new google.maps.LatLng(tramo.latitud_inicio, tramo.longitud_inicio);
            var latlngEnd = new google.maps.LatLng(tramo.latitud_fin, tramo.longitud_fin);

            var request = {
                origin: latlngStart,
                destination: latlngEnd,
                travelMode: google.maps.DirectionsTravelMode.DRIVING
            };
            window.APP.directionsService.route(request, function(response, status) {
                if (status === google.maps.DirectionsStatus.OK) {
                    directionDisplay.setDirections(response);
                } else {
                    // Fallback to markers
                    var start = new google.maps.Marker({
                        position: latlngStart,
                        map: map
                    });
                    var end = new google.maps.Marker({
                        position: latlngEnd,
                        map: map
                    });
                }
            });
        }

    });

    return CarreteraDetailView;

});
