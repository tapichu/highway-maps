define(['./CarreteraView'], function(CarreteraView) {

    var SEARCH_TYPE = {
        ESTADO: 'porEstado',
        MUNICIPIO: 'porMunicipio',
        LOCALIDAD: 'porLocalidad',
        CARRETERA: 'porCarretera'
    };

    var AppView = Backbone.View.extend({

        el: $('#buscadorApp'),

        template: _.template($('#carretera-table-tmpl').html()),

        events: {
            'click input[name="searchType"]': 'searchTypeChanged',
            'click #searchButton': 'search'
        },

        initialize: function(params) {
            this.collection = params.collection;
            
            _.bindAll(this, 'render', 'addOne', 'addAll', 'getSearchType');

            // Listen for changes in the model
            this.collection.bind('refresh', this.addAll);
            
            // Cache useful query results
            this.searchTypeGroup = this.$('input[name="searchType"]');
            this.estadosSelect = this.$('#estadoOptions');
            this.searchTextInput = this.$('#searchText');
            this.searchResults = this.$('#searchResults');

            // Hide the search input, the default search type is estados
            this.searchTextInput.hide();
        },
        
        render: function() {
            this.searchResults.empty().html(this.template({}));
        },

        addOne: function(carretera, index) {
            var view = new CarreteraView({model: carretera});
            this.$('#carreteraTable').append(view.render(index).el);
        },

        addAll: function() {
            this.render();
            this.collection.each(this.addOne);
        },

        getSearchType: function() {
            return this.searchTypeGroup.filter(':checked').attr('value');
        },

        searchTypeChanged: function() {
            var searchType = this.getSearchType();
            switch(searchType) {
            case SEARCH_TYPE.ESTADO:
                this.searchTextInput.hide();
                this.estadosSelect.show();
                break;
            case SEARCH_TYPE.MUNICIPIO:
            case SEARCH_TYPE.LOCALIDAD:
            case SEARCH_TYPE.CARRETERA:
            case SEARCH_TYPE.CARRETERA:
                this.estadosSelect.hide();
                this.searchTextInput.show();
                break;
            }
        },

        search: function(e) {
            e.preventDefault();
            var searchType = this.getSearchType();
            switch(searchType) {
            case SEARCH_TYPE.ESTADO:
                var estado = this.estadosSelect.find(':selected').attr('value');
                window.location.hash = 'search/estado/' + estado;
                break;
            case SEARCH_TYPE.MUNICIPIO:
                var municipio = this.searchTextInput.val();
                window.location.hash = 'search/municipio/' + municipio;
                break;
            case SEARCH_TYPE.LOCALIDAD:
                var localidad = this.searchTextInput.val();
                window.location.hash = 'search/localidad/' + localidad;
                break;
            case SEARCH_TYPE.CARRETERA:
                var carretera = this.searchTextInput.val();
                window.location.hash = 'search/carretera/' + carretera;
                break;
            }
        }

    });

    return AppView;

});
