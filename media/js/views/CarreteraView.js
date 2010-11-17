define(
    ['models/CarreteraDetail', 'views/CarreteraDetailView'],
    function(CarreteraDetail, CarreteraDetailView) {

        var CarreteraView = Backbone.View.extend({

            tagName: 'tr',

            template: _.template($('#carretera-tmpl').html()),

            events: {
                'click': 'showDetail'
            },

            initialize: function() {
                _.bindAll(this, 'showDetail');
            },

            render: function(index) {
                $(this.el).html(this.template(this.model.toJSON()))
                    .addClass((index % 2 === 0) ? 'row1' : 'row2');
                return this;
            },

            showDetail: function() {
                var carreteraDetail = new CarreteraDetail({id: this.model.id});
                var detailView = new CarreteraDetailView({model: carreteraDetail});
                carreteraDetail.fetch();
            }

        });

        return CarreteraView;

    }
);
