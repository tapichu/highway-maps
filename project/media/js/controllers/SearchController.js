define(['models/CarreteraList'], function(CarreteraList) {

    var SearchController = Backbone.Controller.extend({
        
        routes: {
            'search/carretera/:query':  'searchCarreteras',
            'search/estado/:query':     'searchEstados',
            'search/municipio/:query':  'searchMunicipios',
            'search/localidad/:query':  'searchLocalidades',
            'search/ruta/:query':       'searchRutas'
        },

        initialize: function(params) {
            this.collection = params.collection;
        },

        searchCarreteras: function(query) {
            this.collection.type = 'carretera';
            this.search(query);
        },

        searchEstados: function(query) {
            this.collection.type = 'estado';
            this.search(query);
        },

        searchMunicipios: function(query) {
            this.collection.type = 'municipio';
            this.search(query);
        },

        searchLocalidades: function(query) {
            this.collection.type = 'localidad';
            this.search(query);
        },

        searchRutas: function(query) {
            this.collection.type = 'ruta';
            this.search(query);
        },

        search: function(query) {
            this.collection.filter = query;
            this.collection.fetch();
        }

    });

    return SearchController;

});
