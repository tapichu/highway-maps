(function() {

    require(
        ['views/AppView', 'controllers/SearchController', 'models/CarreteraList'],
        function(AppView, SearchController, CarreteraList) {
            require.ready(function() {

                var carreterasList = new CarreteraList;

                // Handle the application's searches
                var controller = new SearchController({
                    collection: carreterasList
                });
                Backbone.history.start();

                window.APP = new AppView({
                    collection: carreterasList
                });

                APP.directionsService = new google.maps.DirectionsService();

            });
        }
    );

})();
