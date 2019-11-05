var get_openhousersvp_data = function(url){
    return $.ajax({
        type: 'GET',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        success: function (data) {
            console.log(data)
        },
        error: function (data) {
            console.log(data)
        }
    });
}

var post_openhouse_data = function(data){
    set_ajax_token();
    var url = "/api/openhouse/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            noty({
               text: 'New Open House set.',
               layout: 'topCenter',
               closeWith: ['click', 'hover', 'timeout'],
               timeout: 5000,
               type: 'success'
            });
        },
        error: function (data) {
            console.log(data);
            noty({
               text: 'Open house Creation failed!!',
               layout: 'topCenter',
               closeWith: ['click', 'hover'],
               type: 'error'
            });
        }
    });
}

var post_owner_availability_data = function(data){
    set_ajax_token();
    var url = "/api/owneravailability/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            noty({
               text: 'Owner Availability Set.',
               layout: 'topCenter',
               closeWith: ['click', 'hover', 'timeout'],
               timeout: 5000,
               type: 'success'
            });
        },
        error: function (data) {
            console.log(data);
            noty({
               text: 'Owner Availability Set failed!!',
               layout: 'topCenter',
               closeWith: ['click', 'hover'],
               type: 'error'
            });
        }
    });
}