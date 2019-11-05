var get_my_notification = function(url){
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

var post_notification = function(data){
    set_ajax_token();
    var url = "/api/notification/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}