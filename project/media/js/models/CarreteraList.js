define(['./Carretera'], function(Carretera) {

    var CarreteraList = Backbone.Collection.extend({
        
        model: Carretera,

        initialize: function(params) {
            params = params || {};
            this.entity = params.type || 'estado';
            this.filter = params.filter || '';
        },

        url: function() {
            return 'search/' + this.removeSpace(this.type) + '/' + this.removeSpace(this.filter);
        },

        parse: function(response) {
            return response.carreteras;
        },

        removeSpace: function(text) {
            return text.replace(/\s/g, '__');
        }

    });

    return CarreteraList;

});
