$(document).ready(function () {
    // Animate the main text with bounce effects
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn"
        },
        out: {
            effect: "bounceOut"
        }
    });

    // Animate the Siri intro message
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp"
        },
        out: {
            effect: "fadeOutUp"
        }
    });

    // Initialize SiriWave (using jQuery selector for container)
    var siriContainer = $("#siri-container")[0]; // jQuery returns an array-like object, so we get the DOM node
    var siriWave = new SiriWave({
        container: siriContainer,
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: 1,
        speed: 0.30,
        autostart: true
    });

    // Mic button click - switch view to Siri wave
    $("#MicBtn").on("click", function () {
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });
});
