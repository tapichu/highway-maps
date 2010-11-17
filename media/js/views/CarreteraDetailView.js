define(['models/Tramo', './TramoView'], function(Tramo, TramoView) {

    var CarreteraDetailView = Backbone.View.extend({

        tagName: 'div',

        id: 'details',

        template: _.template($('#details-tmpl').html()),

        events: {},

        initialize: function(params) {
            _.bindAll(this, 'render', 'renderTramos');

            this.model.bind('change', this.render);

            this.animationSpeed = params && params.animationSpeed || 500;
        },

        render: function() {
            var previousDetails = $('#details');
            if (previousDetails != undefined && previousDetails.length > 0) {
                var that = this;
                previousDetails.slideUp(this.animationSpeed, function() {
                    previousDetails.remove();
                    that.renderTramos();
                });
            } else {
                this.renderTramos();
            }
        },

        renderTramos: function() {
            var $this = $(this.el)
                .append(this.template(this.model.toJSON()))
                .css({display: 'none'})
                .appendTo($('#searchResults'));
            _.each(this.model.get('tramos'), this.addTramo, this);
            $this.slideDown(this.animationSpeed);
        },

        addTramo: function(element, index) {
            var tramo = new Tramo(element);
            var view = new TramoView({model: tramo});
            this.$('#tramosTable').append(view.render(index).el);
        }

    });

    return CarreteraDetailView;

});
