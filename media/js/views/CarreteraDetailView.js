define(['models/Tramo', './TramoView'], function(Tramo, TramoView) {

    var CarreteraDetailView = Backbone.View.extend({

        tagName: 'div',

        id: 'details',

        template: _.template($('#details-tmpl').html()),

        events: {},

        initialize: function() {
            $('#details').remove();

            _.bindAll(this, 'render');

            this.model.bind('change', this.render);
        },

        render: function() {
            $(this.el)
                .append(this.template(this.model.toJSON()))
                .appendTo($('#searchResults'));
            _.each(this.model.get('tramos'), this.addTramo, this);
        },

        addTramo: function(element, index) {
            var tramo = new Tramo(element);
            var view = new TramoView({model: tramo});
            this.$('#tramosTable').append(view.render(index).el);
        }

    });

    return CarreteraDetailView;

});
