var get_all_flag_types = function(){
    return $.ajax({
        type: 'GET',
        async: false,
        url: "/api/flagtype/",
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

var get_all_flagged_properties = function(){
    return $.ajax({
        type: 'GET',
        async: false,
        url: "/api/flaggedproperty/",
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

var post_flagged_property = function(data){
    set_ajax_token();
    var url = "/api/flaggedproperty/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            noty({text: 'Thank You For Reporting!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover', 'timeout'],
                  timeout: 5000,
                  type: 'success'});
        },
        error: function (data) {
        if(data.responseText.indexOf('ValueError') == 0){
            noty({text: 'Cannot report same property with same issue multiple times!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover'],
                  type: 'error'});
        }
        else{
            noty({text: 'Something went wrong please try again!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover'],
                  type: 'error'});
            console.log(data)
        }
    }
    });
}
