$(document).ready(function(){
	$('.header>img').hover(function(event){ 
		var NeeWidth=parseInt($(this).css('width').replace('px',''))+100+'px'
		$(this).animate({width: NeeWidth}, 600); 
	}, function(event){ 
		var NeeWidth=parseInt($(this).css('width').replace('px',''))-100+'px' 
		$(this).animate({width: NeeWidth}, 600); 
	}); 
});