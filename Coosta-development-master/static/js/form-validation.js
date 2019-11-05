// Wait for the DOM to be ready
$(function() {

    /*
    *****
    Refer this to add Form Validations in this script
    Validation rules list can be find here: https://jqueryvalidation.org/documentation/
    *****

    $("form[name='name_of_the_form']").validate({
        // Specify validation rules
        rules: {
            // The key name on the left side is the name attribute
            // of an input field. Validation rules are defined
            // on the right side
            key_name: {
                required: true,
            }
        },
        // Specify validation error messages
        messages: {
            key_name: {
                required: "Please provide a username",
        },
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function(form) {
            form.submit();
        }
    });
    */

    // Initialize form validation on the login form.
    $("form[name='login']").validate({
        rules: {
            username: {
                required: true,
                minlength: 4,
                maxlength: 30
            },
            password: {
                required: true,
                minlength: 7
            }
        },
        messages: {
            username: {
                required: "Please provide a username",
                minlength: "Minimum 4 characters",
                maxlength: "Maximum 30 characters"
            },
            password: {
                required: "Please enter your password",
                minlength: "Your password must contain more than 6 characters"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });

    // Initialize form validation on the registration form.
    $("form[name='registration']").validate({
        rules: {
            username: {
                required: true,
                minlength: 4,
                maxlength: 30
            },
            password1: {
                required: true,
                minlength: 7,
            },
            password2: {
                required: true,
                minlength: 7,
                passwordMatch: true
            },
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            username: {
                required: "Please provide a username",
                minlength: "Minimum 4 characters",
                maxlength: "Maximum 30 characters"
            },
            password1: {
                required: "What is your password?",
                minlength: "Your password must contain more than 6 characters"
            },
            password2: {
                required: "You must confirm your password",
                minlength: "Your password must contain more than 6 characters",
                passwordMatch: "Your Passwords Must Match" // custom message for mismatched passwords
            },
            email: {
                required: "Please enter your email",
                email: "Please enter a valid email"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });

    // Initialize form validation on the reset_password form.
    $("form[name='reset_password']").validate({
        rules: {
            new_password1: {
                required: true,
                minlength: 7,
            },
            new_password2: {
                required: true,
                minlength: 7,
                password2Match: true
            }
        },
        messages: {
            new_password1: {
                required: "What is your new password?",
                minlength: "Your password must contain more than 6 characters"
            },
            new_password2: {
                required: "You must confirm your password",
                minlength: "Your password must contain more than 6 characters",
                password2Match: "Your Passwords Must Match"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });

    // Initialize form validation on the reset form.
    $("form[name='reset']").validate({
        rules: {
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            email: {
                required: "Please enter your email",
                email: "Please enter a valid email"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });

 // Initialize form validation on the Profile settings form.
    $("form[name='profile_settings']").validate({
        rules: {
            firstname: {
                minlength: 2,
            },
            lastname: {
                minlength: 2,
            },
            areacode: {
                number: true
            },
            phnumber: {
                number: true,
                phoneUS : true
            },
            city: {
                minlength: 3,
            },
            state: {
                minlength: 3,
            },
            zipcode: {
                number: true,
                rangelength: [6,6]
            }
        },
        messages: {
            firstname: {
                minlength: "Minimum 2 characters",
            },
            lastname: {
                minlength: "Minimum 2 characters",
            },
            areacode: {
                number: "Characters not allowed"
            },
            phnumber: {
                number: "Characters not allowed",
                phoneUS: "Please enter valid phone number"
            },
            city: {
                minlength: "Minimum 3 characters",
            },
            state: {
                minlength: "Minimum 3 characters",
            },
            zipcode: {
                number: "Characters not allowed",
                rangelength: "Length should be 6"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });

    // Initialize form validation on the home_signup form.
    $("form[name='home_signup']").validate({
        rules: {
            sign_up_name: {
                required: true,
                minlength: 4
            },
            sign_up_password: {
                required: true,
                minlength: 7,
            },
            sign_up_email: {
                required: true,
                email: true
            }
        },
        messages: {
            sign_up_name: {
                required: "Please provide a name",
                minlength: "Minimum 4 characters"
            },
            sign_up_password: {
                required: "What is your password?",
                minlength: "Your password must contain more than 6 characters"
            },
            sign_up_email: {
                required: "Please enter your email",
                email: "Please enter a valid email"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });

    // Initialize form validation on the Contact owner page(without auth) form.
    $("form[name='contact_the_owner']").validate({
        rules: {
            contact_name: {
                required: true,
                minlength: 4,
            },
            contact_number: {
                required: true,
                number: "Characters not allowed",
                minlength: 10,
            },
            contact_email: {
                required: true,
                email: true,
            }
        },
        messages: {
            contact_name: {
                required: "Please provide a name",
                minlength: "Minimum 4 characters",
            },
            contact_number: {
                required: "Please provide a contact number?",
                number: "Must be a number",
                minlength: "Number must contain more than 10 characters",
            },
            sign_up_email: {
                required: "Please enter your email",
                email: "Please enter a valid email",
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });

    // Issue Reported Form
    $("form[name='issue_reporter_form']").validate({
        rules: {
            issuetypesdropdown: {
                required: true
            },
            reportmessage : {
                required: true
            },
        },
        messages: {
            issuetypesdropdown: {
                required: "Select Issue Type",
            },
            reportmessage: {
                required: "Enter a message",
            },
        }
    });



});
try{
    jQuery.validator.addMethod( 'passwordMatch', function(value, element) {

        // The two password inputs
        var password = $("#id_password1").val();
        var confirmPassword = $("#id_password2").val();

        // Check for equality with the password inputs
        if (password != confirmPassword ) {
            return false;
        } else {
            return true;
        }

    }, "Your Passwords Must Match");
}
catch(e){
    console.log(e);
}

try{
    $.validator.addMethod( 'password2Match', function(value, element) {

        // The two password inputs
        var password1 = $("#id_new_password1").val();
        var confirmPassword1 = $("#id_new_password2").val();
        // Check for equality with the password inputs
        if (password1 != confirmPassword1 ) {
            return false;
        } else {
            return true;
        }

    }, "Your Passwords Must Match");

}
catch(e){
    console.log(e);
}


var remove_error_message = function(){
    $("#not_match").html("");
}

var remove_user_exist_error = function(){
    $("#user_exist_error").html("");
    $("#email_exist_error").html("");
}

var remove_error_message2 = function(){
    $("#not_match2").html("");
}