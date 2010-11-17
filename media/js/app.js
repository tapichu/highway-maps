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

                var app = new AppView({
                    collection: carreterasList
                });

            });
        }
    );

})();
