define(function() {

    var CarreteraDetail = Backbone.Model.extend({

        initialize: function(params) {
            this.id = params.id;
        },

        url: function() {
            return 'carretera/' + this.id;
        }

    });

    return CarreteraDetail;

});
