function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}
$('document').ready(function(){
    var activation_code = getParameterByName('ac');
    var email_ac = getParameterByName('email');
    if((activation_code !== undefined) && (activation_code !== null)){
        $("#activation_code").html(activation_code);
        $('#form-email').val(email_ac);
    }
    else{
        $("#activation_code").html("Code Not Found");
        $('input').prop("disabled", true);
        $('button').prop("disabled", true);
    }

    var password = document.getElementById("form-password");
    var confirm_password = document.getElementById("form-cnf-password");

    function validatePassword(){
        if(password.value != confirm_password.value) {
            confirm_password.setCustomValidity("Passwords Don't Match");
        } else {
            confirm_password.setCustomValidity('');
        }
    }

    password.onchange = validatePassword;
    confirm_password.onkeyup = validatePassword;
});

function signup(){
    var data = {};
    data['username'] = $('#form-email').val();
    data['firstname'] = $('#form-first-name').val();
    data['lastname'] = $('#form-last-name').val();
//    data['contact'] = $('#form-mobile').val();
    data['password'] = $('#form-password').val();
    data['activation_code'] = $('#activation_code').text();
    data['email'] = $('#form-email').val();
    data['pincode'] = '000000';
    data['contact'] = '000000';
    console.log(data);
    $.ajax({
        type: 'post',
        url: '/register/',
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function (response) {
            $('input').prop("disabled", true);
            $('button').prop("disabled", true);
            alert('Thanks You for registering with us. We will keep you posted on development.');
            window.location.href = '/';
        },
        error: function(response){
//            alert("Ops! Something went wrong. Please try again.");
            alert(response['responseText']);
        }
    });
}