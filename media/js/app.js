(function() {

    require(
        ['views/AppView', 'controllers/SearchController'],
        function(AppView, SearchController) {
            require.ready(function() {

                // Handle the application's searches
                var controller = new SearchController;
                Backbone.history.start();

                var app = new AppView;

            });
        }
    );

})();
