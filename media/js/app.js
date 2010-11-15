(function() {

    require(['views/AppView'],
        function(AppView) {
            require.ready(function() {
                var App = new AppView;
            });
        }
    );

})();
