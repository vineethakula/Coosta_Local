var post_page_view_for_property = function(data){
    set_ajax_token();
    return $.ajax({
        type: 'POST',
        async: false,
        //url: "/api/statistic/",
        url: property_statistic_base_url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        data: JSON.stringify (data),
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}