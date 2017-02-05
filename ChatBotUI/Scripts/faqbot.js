/// <reference path="jquery-1.12.4.min.js" />

var serverurl = "http://localhost:8000"
//var serverurl = "http://127.0.0.1:8000"

var userrequest = function () {
    var input_text = $("#btn-input").val();
    if (input_text != "") {
        sendTextToModelClassifier(input_text);
        $("#btn-input").val('');
    }
};

var sendTextToModelClassifier = function (user_text) {
    var data_tosend = { "input-request": user_text };
    addUserRequestToChat(user_text);
    $.ajax({
        url: serverurl + "/userrequest",
        method: "POST",
        type: "POST",
        data: JSON.stringify(data_tosend),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (result) {
            result.class
            addResponseToChat(result);
        }
    });
}

var userLinkClick = function (user_text) {
    sendTextToModelClassifier(user_text);
}

var addUserRequestToChat = function (user_input) {
    var js_template = '<li class="right clearfix">';
    js_template += '<span class="chat-img pull-right">';
    js_template += '<img src="images/me.png" alt="User Avatar" class="img-circle" />';
    js_template += '</span>';
    js_template += '<div class="chat-body chat-body-user clearfix">';
    js_template += '<div class="header">';
    js_template += '<small class="text-muted"></span></small>';
    js_template += '<strong class="pull-right primary-font"></strong>';
    js_template += '</div>';
    js_template += '<p>' + user_input + '</p>';
    js_template += ' </div>';
    js_template += ' </li>';
    var chat_body = $("#chat-main-box");
    chat_body.append(js_template);
};

var addResponseToChat = function (response_data) {
    if (response_data.class != undefined) {
        /* class structure 
        {
            "class" : "FDInfo",
            "responsePrefix" : "",
            "responseLink" : "",
            "responseSuffix" : "",
            "responseSuffixLinks" : [
                "",
                ""
            ]
        }
        */
        var response_text = '<p>' + response_data.responsePrefix + '</p>'
        if (response_data.responseLink != "") {
            response_text += '<p><a class="response-prefix-link" target="_blank" href="' + response_data.responseLink + '" >' + response_data.responseLinkText + '</a></p>';
        }
        response_text += response_data.responseSuffix;
        if (response_data.responseSuffixLinks.length > 0) {
            response_text += '<p><ul>';
            $(response_data.responseSuffixLinks).each(function (index, item) {
                response_text += '<li><span class="response-suffix-link" onclick="userLinkClick(\'' + item + '\');" >' + item + '</span></li>';
            });
            response_text += '</ul></p>';
        }

        var js_template = '<li class="left clearfix">';
        js_template += '<span class="chat-img pull-left">';
        js_template += '<img src="images/faq.PNG" alt="User Avatar" class="img-circle" />';
        js_template += '</span>';
        js_template += '<div class="chat-body clearfix">';
        js_template += '<div class="header">';
        js_template += '<strong class="primary-font">FAQ Bot</strong> <small class="pull-right text-muted">';
        js_template += '<span class="glyphicon glyphicon-time"></span>';
        js_template += '</small></div>';
        js_template += '<p>' + response_text + '</p>';
        js_template += '</div>';
        js_template += '</li>';
        var chat_body = $("#chat-main-box");
        chat_body.append(js_template);
        $("#scroll-to-div").scrollTop();
        var chatBox = $("#chat-box-scroll-panel").focusin();
        var elem = document.getElementById('chat-box-scroll-panel');
        elem.scrollTop = elem.scrollHeight;
        chatBox.scrollTop(elem.scrollHeight);
    }
};