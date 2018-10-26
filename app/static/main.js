var width = $('.g-recaptcha').parent().width();
if (width < 302) {
	var scale = width / 200;
	$('.g-recaptcha').css('transform', 'scale(' + scale + ')');
	$('.g-recaptcha').css('-webkit-transform', 'scale(' + scale + ')');
	$('.g-recaptcha').css('transform-origin', '10 10');
	$('.g-recaptcha').css('-webkit-transform-origin', '10 10');
}

$(window).load(function() {
    // Animate loader off screen
    $("#overlay").fadeOut("slow");;
});

