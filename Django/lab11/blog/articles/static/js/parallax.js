$(document).ready(function(){
	var yPosition;
	scrolled = 0;
	var $parallaxElements = $('.parallax img');
	$(window).scroll(function() {
		scrolled = $(window).scrollTop();
		for (var i = 0; i < $parallaxElements.length; i++){
			yPosition = (scrolled *0.5*(i + 1));
			$parallaxElements.eq(i).css({ top: yPosition });
		}
	});
});
