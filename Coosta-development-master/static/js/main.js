var search_address = function(){
    var address = $("#address").val().trim();
    var city = $("#city").val().trim();
    if($("#city").val().trim() == ""){
        $("#city").css({"border":"1px solid #ff0000","background-color":"#ffeeee"});
//        ("Please Enter a propert address");
        return false;
    }
//    else if(is_address($("#address").val())){
//        alert("Direct Address Search is not in scope of Sprint I");
//        return false;
//    }
    else{
        var city = $("#city").val().trim().replace(", United States", "").split(',');
        if(city.length >1){
            $("#stateSelection").val(city[1].trim());
            $("#city").val(city[0]);
            return true;
        }
        else{
            return true;
        }
    }

}

var send_message_arg = function(){
    localStorage.setItem('owner', JSON.stringify($("#owner_id").val()));
    localStorage.setItem('property', JSON.stringify($("#property_id").val()));
    localStorage.setItem('owner_image', JSON.stringify($("#owner_profile_image").attr('src')));
    localStorage.setItem('owner_name', JSON.stringify($("#owner_name").html()));
    return true;
}

function is_address(address){
    address = address.split(' ');
    if(isNaN(address[0])){
        return false;
    }
    else{
        return true;
    }
}

var remove_alert_css_from_textbox = function(id){
    $("#"+id).css({"border":"","background-color":""});
}

var home_to_sign_up_page = function(){
    localStorage.setItem('name', JSON.stringify($("#sign_up_name").val()));
    localStorage.setItem('email', JSON.stringify($("#sign_up_email").val()));
    localStorage.setItem('password', JSON.stringify($("#sign_up_password").val()));
    window.location = '/account/register/';
}

var submit_message = function(sender){
    $("#message_error").html("");
    if($("#message").val() == ""){
        $("#message_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter some character</b></div>");
        return false;
    }
    else if($("#message").val().length < 10){
        $("#message_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter atleast 10 character</b></div>");
        return false;
    }
    else{
        var value1=$('#property_id').val();
        var value2=$('#owner_id').val();
        var msg_obj = {
            'message_body':$("#message").val(),
            //'property':"/api/property/3/",
            'property':"/api/property/"+value1+"/",
            'recipient':"/api/users/"+value2+"/",
            'sender': "/api/users/"+sender+"/",
        };
        var create_message_obj = create_message(msg_obj);
        if (create_message_obj){
            window.location.assign("/message/message_box/")
        }
    }

    return false;
    // confirm message
    // redirect to property detail page
}

//Anonymous user message to contact owner
var anonymous_submit_message = function(sender){
    $(".message_error").html("");
    if($("#contact_message").val().length >= 10 && $("#contact_number").val().length == 10 && isValidEmailAddress($("#contact_email").val()) == true && $("#contact_name").val() != "" && $("#contact_number").val() != "" && $("#contact_email").val() != "" && $("#contact_message").val() != "" ){
        var custom_message = "From: "+$("#contact_name").val() +"\n Contact Number: "+$("#contact_number").val() +"\n Contact Email: "+$("#contact_email").val() +"\n Messgae: "+$("#contact_message").val();
        var value1=$('#property_id').val();
        var value2=$('#owner_id').val();
        var new_msg_obj = {
            'message_body':custom_message,
            'property':"/api/property/"+value1+"/",
            'recipient':"/api/users/"+value2+"/",
        };
        create_message(new_msg_obj);
        if (create_message){
            window.location.assign("/")
        }
    }

    else{
        if($("#contact_name").val() == ""){
            $("#contact_name_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter your name</b></div>");
        }

        if($("#contact_number").val() == ""){
            $("#contact_number_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter phone number</b></div>");
        }
        else if(isNaN($("#contact_number").val())){
            $("#contact_number_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter number only</b></div>");
        }
        else if($("#contact_number").val().length < 10){
            $("#contact_number_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter 10 digit number</b></div>");
        }

        if($("#contact_email").val() == ""){
            $("#contact_email_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter your email</b></div>");
        }
        else if(! isValidEmailAddress($("#contact_email").val())){
            $("#contact_email_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter valid email</b></div>");
        }

        if($("#contact_message").val() == ""){
            $("#contact_message_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter some character</b></div>");
        }
        else if($("#contact_message").val().length < 10){
            $("#contact_message_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter atleast 10 character</b></div>");
        }
    }
    return false;
    // confirm message
    // redirect to property detail page
}

function isValidEmailAddress(emailAddress) {
    var pattern = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
    return pattern.test(emailAddress);
};


var set_ajax_token = function(){
    $.ajaxSetup({
         beforeSend: function(xhr, settings) {
             function getCookie(name) {
                 var cookieValue = null;
                 if (document.cookie && document.cookie != '') {
                     var cookies = document.cookie.split(';');
                     for (var i = 0; i < cookies.length; i++) {
                         var cookie = jQuery.trim(cookies[i]);
                         // Does this cookie string begin with the name we want?
                         if (cookie.substring(0, name.length + 1) == (name + '=')) {
                             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                             break;
                         }
                     }
                 }
                 return cookieValue;
             }
             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
             }
         }
    });
}


var add_shortlist_property = function(property_id, user_id){
    var data_obj = {
        "property": "/api/property/"+property_id+"/",
        "user": "/api/users/"+user_id+"/",
    };
    var value2=$('#owner_id').val();
    var data_obj2 = {
        "shortlisted_by": "/api/users/"+user_id+"/",
        "property_owner": "/api/users/"+value2+"/",
        "property": "/api/property/"+property_id+"/",
        "title": "Shortlisted",
        "body": "I have shortlisted your property",
    };
    var output = post_shortlist_property(data_obj);
    var output2 = post_notification(data_obj2);
    if(output.statusText == "Created"){
        window.location.reload();
    }
    else{
        alert(output.statusText)
    }
}


var remove_shortlist_property = function(id){
    var output = delete_shortlist_property(id);
    if(output.statusText == "No Content"){
        window.location.reload();
    }
    else{
        alert(output.statusText)
    }
}

var step1Validation = function(){
    if($("#address").val() == ""){
        $("#address_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Enter a valid address</b></div>");
        return false;
    }
    else{
        $("#address_error").html("");
        new_images_id = [];
        user = $("#coosta_user").val();
        user_id = $("#user_id").val();
        var address = $("#address").val().replace(/ /g, "_");
        var address2 = $("#address").val().replace(/ /g, "%20");
        var city = $("#city").val().replace(/ /g, "_");
        var city2 = $("#city").val().replace(/ /g, "%20");
        var state = $("#stateSelection").val().replace(/ /g, "_");
        var state2 = $("#stateSelection").val().replace(/ /g, "%20");
        coosta_data = get_property('/api/property/?address__icontains='+address2+'&city__icontains='+city2+'&state__icontains='+state2)['responseJSON'];
        if(coosta_data['results'][0]){
            if(coosta_data.results[0]['user']['username']=='zillow'){
                noty({
                   text: 'Property Already Listed on Coosta!',
                   layout: 'topCenter',
                   closeWith: ['click', 'hover'],
                   type: 'success'
                });
                //updating property if found in coosta database
                var property_result = coosta_data.results[0]
                property_result["user"] = "/api/users/"+user_id+"/";
                property_result["completed"] = false;
                property_result["active"] = true;
                delete update_property_data["listed_on"];
                delete update_property_data["url"];
                var response = update_property(url, property_result);
                if(response.status ==200){
                    update_property_data = response['responseJSON']
                    populate_zillow_data(update_property_data)
                    noty({
                       text: 'Property updated',
                       layout: 'topCenter',
                       closeWith: ['click', 'hover'],
                       type: 'success'
                    });
                }
                //window.location.href ="/property/my_property/edit/"+property_id+"/"
            }
            else if(coosta_data.results[0]['user']['username'] == user) {
                var property_id = coosta_data['results'][0].id;
                noty({
                   text: 'You have already listed your property on coosta!',
                   layout: 'topCenter',
                   closeWith: ['click', 'hover'],
                   type: 'success'
                });
                window.location.href ="/property/my_property/edit/"+property_id+"/"
            }
            else if(coosta_data.results[0]['user']['username']!= user) {
                noty({
                   text: 'Property is already listed on coosta and you are not the owner of the Property!',
                   layout: 'topCenter',
                   closeWith: ['click', 'hover'],
                   type: 'success'
                });
                return false;
            }
        }
        else{
            zillow_data = get_zillow_properties('/api/zillow_api/'+address+'/'+city+'/'+state)['responseJSON'];
            if(zillow_data.indexOf('Error') === -1){
                //posting property coming from zillow
                var zillow_property_result = zillow_data[0]
                zillow_property_result["user"] = "/api/users/"+user_id+"/";
                zillow_property_result["completed"] = false;
                zillow_property_result["active"] = true;
                var response = post_property(zillow_property_result);
                update_property_data = response['responseJSON'];
                populate_zillow_data(update_property_data)
            }
            else{
                var new_property_result = {};
                new_property_result["user"] = "/api/users/"+user_id+"/";
                new_property_result["address"] = $("#address").val();
                new_property_result["city"] = $("#city").val();
                new_property_result["state"] = $("#stateSelection").val();
                new_property_result["completed"] = false;
                new_property_result["active"] = true;
                //update_new_property_data = post_property(new_property_result);
                var response = post_property(new_property_result);
                update_property_data = response['responseJSON'];
            }

        }
        $("#city1").val($("#city").val())
        $("#state1").val($("#stateSelection").val())
        $("#address2").val($("#address").val())
        document.getElementById("step2").style.display = "block";
        $('#step1').hide();
        return true;
    }

}

var step2Validation = function(){
    $("#address2_error").html("");
    $("#beds_error").html("");
    $("#property_size_error").html("");
    $("#floors_error").html("");
    $("#year_built_error").html("");
    if($("#property_title").val() == "" || $("#address2").val() == "" || isNaN($("#beds").val()) || isNaN($("#property_size").val()) || isNaN($("#floors").val()) ||  $("#year_built").val() == "" || isNaN($("#year_built").val()) || $('#year_built').val().length != 4){
        if($("#address2").val() == ""){
            $("#address2_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Enter a valid address</b></div>");
            $("#address2").focus();
        }
        if(isNaN($("#beds").val())){
            $("#beds_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Only numbers</b></div>");
            $("#beds").focus();
        }
        if(isNaN($("#property_size").val())){
            $("#property_size_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>in sqft</b></div>");
            $("#property_size").focus();
        }
        if(isNaN($("#floors").val())){
            $("#floors_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Only numbers</b></div>");
            $("#floors").focus();
        }
        if($("#year_built").val() == ""){
            $("#year_built_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Enter year</b></div>");
            $("#year_built").focus();
        }
        else if(isNaN($("#year_built").val())){
            $("#year_built_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Only numbers</b></div>");
            $("#year_built").focus();
        }
        else if($('#year_built').val().length != 4){
            $("#year_built_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>4 digits only</b></div>");
            $("#year_built").focus();
        }
        if($("#property_title").val() == ""){
            $("#property_title_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Property title can't be blank</b></div>");
            $("#property_title").focus();
        }
        return false;
    }
    else{
        var span = document.getElementById("zestimate_price").innerText;
        if (span == ""){
            document.getElementById("zestimate").style.display = "none";
        }
        update_property_data["property_title"] = $('#property_title').val();
        update_property_data["address"] = $('#address2').val();
        update_property_data["city"] = $('#city1').val();
        update_property_data["state"] = $('#state1').val();
        update_property_data["zip_code"] = $('#zipcode').val();
        update_property_data["home_type"] = $('#home_type').val();
        update_property_data["beds"] = $('#beds').val();
        update_property_data["baths"] = $('#baths').val();
        update_property_data["rooms"] = $('#rooms').val();
        update_property_data["floors"] = $('#floors').val();
        update_property_data["basement"] = $('#basements').val();
        update_property_data["roof"] = $("#roof").is(":checked");
        update_property_data["year_built"] = $('#year_built').val();
        update_property_data["description"] = $('#description').val();
        update_property_data["other_features"] = $('#features').val();
        update_property_data["property_size"] = $('#property_size').val();
        update_property_data["status"] = "/api/propertystatus/2/";
        delete update_property_data["listed_on"];
        var url = update_property_data['url'];
        delete update_property_data["url"];
        delete update_property_data["id"];
        delete update_property_data["images"];
        var response = update_property(url, update_property_data);
        if(response.status == 200){
            update_property_data = response['responseJSON']
            noty({
               text: 'Property updated!',
               layout: 'topCenter',
               closeWith: ['click', 'hover'],
               timeout: 5000,
               type: 'success'
            });
            //$.each(new_images_id, function(i){
            //    post_property_images({"image": new_images_id[i], "property": update_property_data['responseJSON']['url']})
            //});
            document.getElementById("step3").style.display = "block";
            $('#step3_button').hide();
            return true;
        }
        else{
            noty({
               text: 'Property not updated!! Something went wrong.',
               layout: 'topCenter',
               closeWith: ['click', 'hover'],
               timeout: 5000,
               type: 'error'
            });
        }
    }
}

var step3Validation = function(){
    if($("#property_price").val() == "" || isNaN(parseInt($("#property_price").val().replace(/[$,]+/g,"")))){
        if($("#property_price").val() == ""){
            $("#property_price_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter price</b></div>");
        }
        else if(isNaN(parseInt($("#property_price").val().replace(/[$,]+/g,"")))){
            $("#property_price_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter valid price format</b></div>");
        }
        return false;
    }
    else{
        $("#property_price_error").html("");
        //final updation in step3 data which come from coosta database with price and completed
        property_id = update_property_data['id'];
        update_property_data["property_value"] = parseInt($("#property_price").val().replace(/[$,]+/g,""));
        update_property_data["completed"] = true;
        update_property_data["status"] = "/api/propertystatus/4/";
        delete update_property_data["listed_on"];
        delete update_property_data["id"];
        var response = update_property(update_property_data['url'], update_property_data);
        if(response.status ==200){
            update_property_data = response['responseJSON']
//            window.location.href = "/property/temp_preview/"+property_id+"/";
//            noty({
//               text: 'Property updated',
//               layout: 'topCenter',
//               closeWith: ['click', 'hover'],
//               type: 'success'
//            });
              $('#openhousemodel').modal('show');
        }
        else{
            noty({
               text: 'Property not updated!! Something went wrong.',
               layout: 'topCenter',
               closeWith: ['click', 'hover'],
               type: 'error'
            });
        }
        return true;
    }
}


function RemoveBaseUrl(url) {
    /*
     * Replace base URL in given string, if it exists, and return the result.
     *
     * e.g. "http://localhost:8000/api/v1/blah/" becomes "/api/v1/blah/"
     *      "/api/v1/blah/" stays "/api/v1/blah/"
     */
    var baseUrlPattern = /^https?:\/\/[a-z\:0-9.]+/;
    var result = "";

    var match = baseUrlPattern.exec(url);
    if (match != null) {
        result = match[0];
    }

    if (result.length > 0) {
        url = url.replace(result, "");
    }

    return url;
}




var populate_zillow_data = function(data){
    if('property_title' in data){
        $("#property_title").val(data['property_title'])
    }
    if('property_value' in data){
        $("#zestimate_price").html("$"+ data['property_value'].toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,'))
    }
    if('baths' in data){
        $("#baths").val(data['baths'])
    }
    if('beds' in data){
        $("#beds").val(data['beds'])
    }
    if('rooms' in data){
        $("#room").val(data['rooms'])
    }
    if('property_size' in data){
        $("#property_size").val(data['property_size'])
    }
    if('year_built' in data){
        $("#year_built").val(data['year_built'])
    }
    if('city' in data){
        $("#city1").val(data['city'])
    }
    if('state' in data){
        $("#state1").val(data['state'])
    }
    if('address' in data){
        $("#address2").val(data['address'])
    }
    if('zip_code' in data){
        $("#zipcode").val(data['zip_code'])
    }
}

var editPropertyValidation = function(){
    $("#property_title_error").html("");
    $("#property_price_error").html("");
    $("#address2_error").html("");
    $("#city1_error").html("");
    $("#state1_error").html("");
    $("#zipcode_error").html("");
    $("#beds_error").html("");
    $("#property_size_error").html("");
    $("#floors_error").html("");
    $("#year_built_error").html("");
    if($("#property_title").val() == "" || $("#property_price").val() == "" || $("#address2").val() == "" || $("#city1").val() == "" || $("#state1").val() == ""  || isNaN($("#zipcode").val()) || isNaN($("#beds").val()) || isNaN($("#property_size").val()) || isNaN($("#floors").val()) || $("#year_built").val() == "" || isNaN($("#year_built").val()) || $('#year_built').val().length != 4 ){
        if($("#property_title").val() == ""){
            $("#property_title_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Property title can't be blank</b></div>");
            $("#property_title").focus();
        }
        if($("#property_price").val() == ""){
            $("#property_price_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Property Price can't be blank</b></div>");
            $("#property_price").focus();
        }
        if($("#address2").val() == ""){
            $("#address2_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Enter a valid address</b></div>");
            $("#address2").focus();
        }
        if($("#city1").val() == ""){
            $("#city1_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Enter a valid city</b></div>");
            $("#city1").focus();
        }
        if($("#state1").val() == ""){
            $("#state1_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Enter a valid state</b></div>");
            $("#state1").focus();
        }
        if(isNaN($("#zipcode").val())){
            $("#zipcode_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>ZipCode should be numbers only</b></div>");
            $("#zipcode").focus();
        }
        if(isNaN($("#beds").val())){
            $("#beds_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Only numbers</b></div>");
            $("#beds").focus();
        }
        if(isNaN($("#property_size").val())){
            $("#property_size_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>in sqft</b></div>");
            $("#property_size").focus();
        }
        if(isNaN($("#floors").val())){
            $("#floors_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Only numbers</b></div>");
            $("#floors").focus();
        }
        if($("#year_built").val() == ""){
            $("#yaer_built_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Enter year</b></div>");
            $("#year_built").focus();
        }
        else if(isNaN($("#year_built").val())){
            $("#yaer_built_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Only numbers</b></div>");
            $("#year_built").focus()
        }
        else if($('#year_built').val().length != 4){
            $("#yaer_built_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>4 digits only</b></div>");
            $('#year_built').focus();
        }
        return false;
    }
    return true
}

function set_loading(flag){ 
    if(flag == true){
             $("#load_spinner").show();
    } 
    else{ 
        $("#load_spinner").hide();
    } 
}


function activateProperty(property_id){
    var activate_property = property_objects[property_id];
    activate_property["active"] = true;
    if(typeof activate_property["user"] != "string"){
        activate_property["user"] = "/api/users/"+property_objects[property_id]["user"]["id"]+"/";
        activate_property["status"] = "/api/propertystatus/"+property_objects[property_id]["status"]["id"]+"/";
    }
    var url = "/api/property/"+property_id+"/";
    var activate_property_data = update_property(url, activate_property);
    if(activate_property_data.status ==200){
        $("#status_"+property_id).html('Active');
        var html = '<a id="status_action_'+property_id+'" href="#" onclick="return deactivateProperty('+property_id+')">Deactivate Property</a>';
        $("#status_action_"+property_id).parent().html(html);
        noty({
           text: 'Property Activated',
           layout: 'topCenter',
           closeWith: ['click', 'hover'],
           type: 'success'
        });
    }
    else{
        noty({text: 'Property not Activated!',
          layout: 'topCenter',
          closeWith: ['click', 'hover'],
          type: 'error'});
    }
    return false;
}

function deactivateProperty(property_id){
    var deactivate_property = property_objects[property_id];
    deactivate_property["active"] = false;
    if(typeof deactivate_property["user"] != "string"){
        deactivate_property["user"] = "/api/users/"+property_objects[property_id]["user"]["id"]+"/";
        deactivate_property["status"] = "/api/propertystatus/"+property_objects[property_id]["status"]["id"]+"/";
    }
    var url = "/api/property/"+property_id+"/";
    var deactivate_property_data = update_property(url, deactivate_property);
    if(deactivate_property_data.status ==200){
        $("#status_"+property_id).html('Inactive');
        var html = '<a id="status_action_'+property_id+'" href="#" onclick="return activateProperty('+property_id+')">Activate Property</a>';
        $("#status_action_"+property_id).parent().html(html);
        noty({
           text: 'Property Deactivated',
           layout: 'topCenter',
           closeWith: ['click', 'hover'],
           type: 'success'
        });
    }
    else{
        noty({text: 'Property not Deactivated!',
          layout: 'topCenter',
          closeWith: ['click', 'hover'],
          type: 'error'});
    }
    return false;
}

var help_faq_message = function(sender){
    $("#message_error").html("");
    if($("#message").val() == ""){
        $("#message_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter some character</b></div>");
        return false;
    }
    else if($("#message").val().length < 10){
        $("#message_error").html("<div class='validation' style='color:red;margin-bottom:10px;font-size:16px'><b>Please enter atleast 10 character</b></div>");
        return false;
    }
    else{
        var help_faq_msg_obj = {
            'message_body':$("#message").val(),
            'recipient':"/api/users/1/",
            'sender': "/api/users/"+sender+"/",
        };
        var create_message_obj = create_message(help_faq_msg_obj);
        if(!create_message_obj){
            noty({
               text: 'Message  Not Sent',
               layout: 'topCenter',
               closeWith: ['click', 'hover'],
               type: 'error'
            });
        }
        else{
            document.getElementById('message').value = "";
        }
    }

    return false;
}