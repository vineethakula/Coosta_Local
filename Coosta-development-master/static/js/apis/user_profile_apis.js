var get_user_profile_data_from_id = function(user_id, url){
    return $.ajax({
        type: 'GET',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        data: user_id,
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}

var update_user_profile = function(url, data){
    set_ajax_token();
    return $.ajax({
        type: 'PUT',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify (data),
        success: function (data) {
            noty({text: 'Profile Saved!',
                  layout: 'topCenter',
                  closeWith: ['click', 'hover'],
                  type: 'success'});
        },
        error: function (data) {
            console.log(data)
        }
    });
}