var get_escrow_property = function(data, url){
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