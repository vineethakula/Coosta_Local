var get_message = function(id){
    return $.ajax({
        type: 'GET',
        async: false,
        url: "/api/message/"+id +"/",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}

var create_message = function(data){
    set_ajax_token();
    return $.ajax({
        type: 'POST',
        async: false,
        url: "/api/message/",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        data: JSON.stringify (data),
        success: function (data) {
            noty({text: 'Message has been sent.',
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

var get_my_message = function(url){
    return $.ajax({
        type: 'GET',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}
