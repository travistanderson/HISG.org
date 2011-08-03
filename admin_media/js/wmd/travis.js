$(document).ready(function() {
	// $('#id_content ~ label').hide();
	$('label[for="id_content"]').hide();
	i=0;
	$('.wmd-preview > *').each(function(i){
		$(this).attr('tabindex',i+1000);
		i+=1;
	})
});