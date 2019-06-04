
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];
    var entries_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        //maintain a list of ten numbers
        if (numbers_received.length >= 10){
            numbers_received.shift()
        }
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        }
        $('#log').html(numbers_string);
    });

    //receive details from server
    socket.on('newsingin', function(msg) {
        console.log("Received name " + msg.name + " " + msg.datetime);

        // maintain a list of ten numbers
        if (entries_received.length >= 10){
            entries_received.shift()
        }

        entries_received.push(msg.name + " (" + msg.datetime + ")");
        entries_string = '';
        for (var i = 0; i < entries_received.length; i++){
            entries_string = entries_string + '<p>' + entries_received[i] + '</p>';
        }
        $('#log').html(entries_string);
    });

});
