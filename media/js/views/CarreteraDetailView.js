define(['models/Tramo', './TramoView'], function(Tramo, TramoView) {

    var CarreteraDetailView = Backbone.View.extend({

        tagName: 'div',

        id: 'details',

        template: _.template($('#details-tmpl').html()),

        events: {},

        initialize: function(params) {
            _.bindAll(this, 'render', 'renderDetails', 'calculateRoute');
            this.model.bind('change', this.render);

            this.animationSpeed = params && params.animationSpeed || 500;
            if (typeof google !== undefined) {
                this.directionDisplay = new google.maps.DirectionsRenderer();
            }
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
                if (typeof google !== "undefined") {
                    // Render map
                    var tramos = that.model.get('tramos');
                    var latlng = that.calculateMapCenter(tramos);
                    var options = {
                        zoom: 7,
                        center: latlng,
                        mapTypeId: google.maps.MapTypeId.ROADMAP
                    };
                    var map = new google.maps.Map(that.$('#map')[0], options);
                    that.directionDisplay.setMap(map);

                    _.each(tramos, function(tramo) {
                        that.addTramoMarkers(map, tramo);
                    });

                    // Add directions for the biggest route
                    var tramo = _.max(tramos, function(t) { return t.longitud; });
                    that.calculateRoute(tramo);
                }
            });
        },

        addTramo: function(element, index) {
            var tramo = new Tramo(element);
            var view = new TramoView({model: tramo});
            this.$('#tramosTable').append(view.render(index).el);
        },

        calculateMapCenter: function(tramos) {
            var latStart = _.map(tramos, function(t) { return t.latitud_inicio; });
            var latEnd = _.map(tramos, function(t) { return t.latitud_fin; });
            var lonStart = _.map(tramos, function(t) { return t.longitud_inicio; });
            var lonEnd = _.map(tramos, function(t) { return t.longitud_fin; });
            var latitudes = latStart.concat(latEnd);
            var longitudes = lonStart.concat(lonEnd);

            var latMax = _.max(latitudes);
            var latMin = _.min(latitudes);
            var lonMax = _.max(longitudes);
            var lonMin = _.min(longitudes);

            var latitude = latMin + ((latMax - latMin) / 2); 
            var longitude = lonMin + ((lonMax - lonMin) / 2);
            return new google.maps.LatLng(latitude, longitude);
        },

        addTramoMarkers: function(map, tramo) {
            var latlngStart = new google.maps.LatLng(tramo.latitud_inicio, tramo.longitud_inicio);
            var latlngEnd = new google.maps.LatLng(tramo.latitud_fin, tramo.longitud_fin);

            var start = new google.maps.Marker({
                position: latlngStart,
                map: map
            });
            var end = new google.maps.Marker({
                position: latlngEnd,
                map: map
            });
        },

        calculateRoute: function(tramo) {
            var that = this;
            var latlngStart = new google.maps.LatLng(tramo.latitud_inicio, tramo.longitud_inicio);
            var latlngEnd = new google.maps.LatLng(tramo.latitud_fin, tramo.longitud_fin);

            var request = {
                origin: latlngStart,
                destination: latlngEnd,
                travelMode: google.maps.DirectionsTravelMode.DRIVING
            };
            window.APP.directionsService.route(request, function(response, status) {
                if (status === google.maps.DirectionsStatus.OK) {
                    that.directionDisplay.setDirections(response);
                }
            });
        }

    });

    return CarreteraDetailView;

});
