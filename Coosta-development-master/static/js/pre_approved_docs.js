
// Function for checking PreApproved or NonPreApproved User
function checkPreApprovedorNonPreApprovedUser(user_id){
    var non_pre_approved_user_url = "/api/non_pre_approved_user/?user__id=" + user_id;
    var pre_approved_user_url = "/api/pre_approved_user/?user__id=" + user_id;

    var non_pre_approved_user = get_non_pre_approved_user(data='', non_pre_approved_user_url).responseJSON;
    var pre_approved_user = get_pre_approved_user(data='', pre_approved_user_url).responseJSON;

    var result = {};

    if(non_pre_approved_user.count>0){
        result['non_pre_approved_user'] = 'True'
    }
    else{
        result['non_pre_approved_user'] = 'False'
    }
    if(pre_approved_user.count>0){
        result['pre_approved_user'] = 'True'
        result['pre_approved_user_id'] = pre_approved_user.results[0].id;
        result['pre_approved_user_obj'] = pre_approved_user.results[0];
    }
    else{
        result['pre_approved_user'] = 'False'
    }

    return result;
}

//Function to post entry of non-pre-approved user
function nonPreApprovedUser(user_id){
    var non_pre_approved_user_data = {};
    non_pre_approved_user_data["user"] = "/api/users/"+user_id+"/";
    var post_non_pre_approved_user_data = post_non_pre_approved_user(non_pre_approved_user_data);
    return post_non_pre_approved_user_data;
}

//Function to post entry of pre-approved user
function preApprovedUser(user_id){
    var pre_approved_user_data = {};
    pre_approved_user_data["user"] = "/api/users/"+user_id+"/";
    var post_pre_approved_user_data = post_pre_approved_user(pre_approved_user_data);
    return post_pre_approved_user_data ;
}
