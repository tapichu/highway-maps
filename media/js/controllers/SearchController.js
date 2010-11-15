define(function() {

    var SearchController = Backbone.Controller.extend({
        
        routes: {
            'search/estado/:query':     'searchEstados',
            'search/municipio/:query':  'searchMunicipios',
            'search/localidad/:query':  'searchLocalidades'
        },

        initialize: function() {},

        searchEstados: function(query) {
            console.log('Searching for estado: ' + query);
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
