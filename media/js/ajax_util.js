define(function() {

    // Empty function
    var noop = function() {};

    var removeLoadingImage = function(id) {
        if (id !== undefined && typeof id === 'string') {
            $('#' + id).remove();
        } else if (id instanceof $) {
            id.remove();
        }
    };

    var handleServiceSuccess = function(data) {
        removeLoadingImage(this.settings.loadingImageId);
        this.settings.success(data);
    };

    var handleServiceError = function() {
        removeLoadingImage(this.settings.loadingImageId);
        console.error(this.settings.serviceErrorMessage);
        this.settings.error();
    };

    var handleHttpError = function() {
        removeLoadingImage(this.settings.loadingImageId);
        console.error(this.settings.httpErrorMessage);
        this.settings.error()
    };

    // Default options for ajax requests
    var ajaxCallDefaults = {
        url: '',
        data: {},
        success: noop,
        error: noop,
        method: 'GET',
        timeout: 2*60*1000,
        loadingImageId: undefined,
        httpErrorMessage: 'Se produjo un error de comunicación. Por favor intente de nuevo.',
        serviceErrorMessage: 'Se produjo un error. Por favor intente de nuevo.'
    };

    var doAjaxCall = function(params) {
        var settings = _.extend({}, ajaxCallDefaults, params);
        var that = { settings: settings };
        var httpError = _.bind(handleHttpError, that);
        var serviceError = _.bind(handleServiceError, that);
        var serviceSuccess = _.bind(handleServiceSuccess, that);

        $.ajax({
            url: settings.url,
            data: settings.data,
            success: function(data, textStatus, xhr) {
                // Check textStatus
                if (textStatus !== 'success') {
                    if (xhr.status < 100 || xhr.status > 399) {
                        httpError();
                    } else {
                        serviceError();
                    }
                }
                else if (xhr.status < 100 || xhr.status > 399) {
                    httpError();
                }
                else {
                    serviceSuccess(data);
                }
            },
            error: function() {
                httpError();
            },
            method: settings.method,
            timeout: settings.timeout
        });
    };
    
    return {
        ajaxCall: function(params) {
            doAjaxCall(params);
        }
    };

});
