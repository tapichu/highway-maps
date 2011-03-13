define(function() {

    var TramoView = Backbone.View.extend({

        tagName: 'tr',

        template: _.template($('#tramo-tmpl').html()),

        events: {},

        initialize: function() {},

        render: function(index) {
            $(this.el).html(this.template(this.model.toJSON()))
                .addClass((index % 2 === 0) ? 'row1' : 'row2');
            return this;
        }

    });

    return TramoView;

});
