var post_contract = function(data){
    set_ajax_token();
    var url = "/api/contract/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            noty({text: 'Thank You For Signing the Contract!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover', 'timeout'],
                  timeout: 5000,
                  type: 'success'});
        },
        error: function (data) {
            noty({text: 'Something went wrong please try again!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover'],
                  type: 'error'});
            console.log(data)
        }
    });
}

var get_contract = function(data, url){
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

var update_contract = function(data, url){
    console.log(url, data)
    set_ajax_token();
    return $.ajax({
        type: 'PUT',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify (data),
        success: function (data) {
            noty({text: 'Contract has been updated!!!',
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