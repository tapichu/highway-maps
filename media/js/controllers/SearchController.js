define(['ajax_util'], function(ajax_util) {

    var SearchController = Backbone.Controller.extend({
        
        routes: {
            'search/estado/:query':     'searchEstados',
            'search/municipio/:query':  'searchMunicipios',
            'search/localidad/:query':  'searchLocalidades'
        },

        initialize: function() {},

        searchEstados: function(query) {
            console.log('Searching for estado: ' + query);
            ajax_util.ajaxCall({
                url: 'search/estado/' + query,
                data: {},
                success: function(data) {
                    console.log(data);
                }
            });
        },

        searchMunicipios: function(query) {
            console.log('Searching for municipios: ' + query);
        },

        searchLocalidades: function(query) {
            console.log('Searching for localidades: ' + query);
        }

    });

    return SearchController;

});
