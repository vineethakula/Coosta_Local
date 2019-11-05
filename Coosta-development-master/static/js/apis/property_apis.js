var search_properties = function(data, url){
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

var get_shortlisted_properties_obj = function(url){
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


var get_shortlisted_properties = function(data, url){
     var sp_obj = get_shortlisted_properties_obj(url).responseJSON;
     output = [];
     for(var i=0; i<sp_obj.count; i++){
         output.push(sp_obj.results[i].property);
     }
     return output;
}

var get_shortlisted_properties_raw = function(data, url){
     var sp_obj = get_shortlisted_properties_obj(url).responseJSON;
     return sp_obj;
}


var post_shortlist_property = function(data){
    set_ajax_token();
    var url = "/api/shortlisted_property/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            noty({text: 'Property added to Favourites!',
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

var delete_shortlist_property = function(id){
    set_ajax_token();
    var url = url;
    return $.ajax({
        type: 'DELETE',
        async: false,
        url: '/api/shortlisted_property/'+id+'/',
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        success: function (data) {
            noty({text: 'Property Removed from Favourites',
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


var get_properties_images_obj = function(url){
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

var delete_properties_images_obj = function(url){
    return $.ajax({
        type: 'DELETE',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        success: function (data) {
            noty({text: 'Image Deleted',
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

var get_properties_images = function(images){
    output = [];
    for(var i=0; i<images.length; i++){
        var image = get_properties_images_obj(images[i]).responseJSON.image;
        output.push(image);
    }
    return output;
}

var get_property = function(url){
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


var get_recommended_properties = function(url){
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


var get_zillow_properties = function(url){
    set_ajax_token();
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

var post_property = function(data){
    set_ajax_token();
    var url = "/api/property/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            noty({text: 'New Property Listed!',
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

var post_property_images = function(data){
    set_ajax_token();
    var url = "/api/property_images/";
    return $.ajax({
        type: 'POST',
        async: false,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify (data),
        crossDomain: true,
        success: function (data) {
            noty({text: 'New Image Added!',
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

var update_property = function(url, data){
    set_ajax_token();
    return $.ajax({
        type: 'PUT',
        async: false,
        url: url,
        headers: {
                    'X-CSRFToken': csrftoken
                },
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify (data),
        success: function (data) {
        },
        error: function (data) {
            console.log(data)
        }
    });
}