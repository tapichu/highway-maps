define(function() {

    var AppView = Backbone.View.extend({

        el: $('#buscadorApp'),

        events: {
            'click input[name="tipo"]': 'typeChanged'
        },

        initialize: function() {
            this.searchTypeGroup = this.$('input[name="tipo"]');
            this.estadosSelect = this.$('#estadoOptions');
            this.searchTextInput = this.$('#searchText');
            this.searchTextInput.hide();
        },
        
        render: function() {

        },

        typeChanged: function() {
            var selected = this.searchTypeGroup.filter(':checked');
            if (selected.attr('value') === 'porEstado') {
                this.searchTextInput.hide();
                this.estadosSelect.show();
            } else {
                this.estadosSelect.hide();
                this.searchTextInput.show();
            }
        }

    });

    return AppView;

});
