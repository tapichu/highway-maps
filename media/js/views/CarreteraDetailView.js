define(function() {

    var CarreteraDetailView = Backbone.View.extend({

        el: $('#details'),

        template: _.template($('#details-tmpl').html()),

        events: {},

        initialize: function() {
            this.el.empty();

            _.bindAll(this, 'render');

            this.model.bind('change', this.render);
        },

        render: function() {
            this.el.append(this.template(this.model.toJSON()));
        }

    });

    return CarreteraDetailView;

});
