var get_user_for_id = function(id, token){
    return $.ajax({
        type: 'GET',
        async: false,
        url: "/api/users/" + id +"/",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        data: { "X-CSRFToken": token},
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}

var register_user = function(data){
    return $.ajax({
        type: 'POST',
        async: false,
        url: "/api/users/",
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


var update_user = function(url, data){
    set_ajax_token();
    return $.ajax({
        type: 'PUT',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify (data),
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}


var get_userprofile_images = function(url){
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

var get_non_pre_approved_user = function(data, url){
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

var post_non_pre_approved_user = function(data){
    set_ajax_token();
    var url = "/api/non_pre_approved_user/";
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

var get_pre_approved_user = function(data, url){
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

var post_pre_approved_user = function(data){
    set_ajax_token();
    var url = "/api/pre_approved_user/";
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

var post_pre_approved_document = function(data){
    set_ajax_token();
    var url = "/api/pre_approved_document/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            noty({text: 'New Document Added!',
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

var delete_document = function(url){
    return $.ajax({
        type: 'DELETE',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        success: function (data) {
            noty({text: 'Document Deleted',
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
