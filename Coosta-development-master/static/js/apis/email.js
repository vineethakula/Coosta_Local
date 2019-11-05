var reset_password = function(email){
    return $.ajax({
        type: 'POST',
        async: false,
        url: "/api/email/password/reset/",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        email: email,
        success: function (email) {
        },
        error: function (email) {
            console.log(email)
        }
    });
}