define(function() {

    var SEARCH_TYPE = {
        ESTADO: 'porEstado',
        MUNICIPIO: 'porMunicipio',
        LOCALIDAD: 'porLocalidad'
    };

    var AppView = Backbone.View.extend({

        el: $('#buscadorApp'),

        events: {
            'click input[name="searchType"]': 'searchTypeChanged',
            'click #searchButton': 'search'
        },

        initialize: function() {
            _.bindAll(this, 'render', 'getSearchType');

            // Cache useful query results
            this.searchTypeGroup = this.$('input[name="searchType"]');
            this.estadosSelect = this.$('#estadoOptions');
            this.searchTextInput = this.$('#searchText');

            // Hide the search input, the default search type is estados
            this.searchTextInput.hide();
        },
        
        render: function() {

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
            }
        }

    });

    return AppView;

});
