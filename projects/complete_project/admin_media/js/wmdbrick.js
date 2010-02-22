$(document).ready(function() {
	var bricksize = $('#id_size').val();
	if (bricksize){
		bs = String(bricksize);
	}
	else{
		bs='350';
	}
	var brickphotostandard = "url(/site_media/images/sections/misc/brick_blank_large.jpg)";
	var brickphoto = $('#id_photo :selected').text();
	// if (brickphoto){
	// 	
	// }
	var cssObj = {
	        background: "url(/site_media/images/sections/misc/brick_blank_large.jpg)",
			height:bs + "px"
	      }
	
	$('.wmd-preview').css(cssObj);
	$('.preview-wrap').append(brickphoto);
});