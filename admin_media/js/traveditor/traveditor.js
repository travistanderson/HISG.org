$(document).ready(function(){
	// focustb = 0;
	$textbox = $('.wmd-preview').prev();
	$preview = $('.wmd-preview');
	// $preview.html(String($textbox.val()));
	words = String($textbox.val());
	// alert(words);
	// $preview.html(words);
	$(window).keydown(function(event){
		$preview.append('a');
	})
});