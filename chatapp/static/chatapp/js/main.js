socket = new WebSocket("ws://" + window.location.host + "/chat/?"+SESS_ID);
socket.onmessage = function(e) {
    //alert(e.data);
            $("#field_chat").append('Your message:  ')

            $("#field_chat").append(e.data)
            $("#field_chat").append('<br>')
}
socket.onopen = function() {
//    socket.send("hello world");
}
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();

jQuery(document).ready(function ($) {

    $('#send_message').click(function() {
        var text = $("#message").val()
        console.log(text);
        socket.send(text);

        /*$.ajax({
            url: '/chatapp//',
            data: {

            },
            dataType: 'json',
            success: function (data) {
            }
        });*/
    });
    });