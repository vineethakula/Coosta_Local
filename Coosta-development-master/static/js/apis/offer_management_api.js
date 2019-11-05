var get_offers_on_properties = function(data, url){
    return $.ajax({
        type: 'GET',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        data: data,
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}

var update_offers_on_properties = function(data, url){
    console.log(url, data)
    set_ajax_token();
    return $.ajax({
        type: 'PUT',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify (data),
        success: function (data) {
            noty({text: 'You accepted the offer!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover', 'timeout'],
                  timeout: 5000,
                  type: 'success'});
            console.log(data)
        },
        error: function (data) {
            noty({text: 'Something went wrong!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover'],
                  type: 'error'});
            console.log(data)
        }
    });
}

var post_counter_offer_on_properties = function(data){
    set_ajax_token();
    var url = "/api/counteroffers/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            noty({text: 'You counter the offer!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover', 'timeout'],
                  timeout: 5000,
                  type: 'success'});
        },
        error: function (data) {
            console.log(data)
        }
    });
}

var get_counter_offers_on_properties = function(data, url){
    return $.ajax({
        type: 'GET',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        data: data,
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}

var update_counter_offers_on_properties_offers = function(data, url){
    //console.log(url, data)
    set_ajax_token();
    return $.ajax({
        type: 'PUT',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify (data),
        success: function (data) {
            noty({text: 'You have accepted the counter offer!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover', 'timeout'],
                  timeout: 5000,
                  type: 'success'});
            console.log(data)
        },
        error: function (data) {
            noty({text: 'something went wrong!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover'],
                  type: 'error'});
            console.log(data)
        }
    });
}

var post_offer_on_property = function(data){
    set_ajax_token();
    var url = "/api/offers/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            window.location.href = '/offers/';
        },
        error: function (data) {
            console.log(data)
        }
    });
}
