// $(document).ready(function(){
// 	// focustb = 0;
// 	$textbox = $('.wmd-preview').prev();
// 	$preview = $('.wmd-preview');
// 	// $preview.html(String($textbox.val()));
// 	words = String($textbox.val());
// 	// alert(words);
// 	// $preview.html(words);
// 	$(window).keydown(function(event){
// 		$preview.append('a');
// 	})
// });


$(document).ready(function(){
	$textbox = $('.wmd-preview').prev();		// this is defined because it has a different name for each application
	$preview = $('.wmd-preview');
	var words = ''
	var option = 0;
	function update(){
		words = String($textbox.val());
		$preview.html(words);
	}
	$(window).keydown(function(event){
		if(event.which==18){
			option = 1;
		}
	})
	$(window).keydown(function(event){
		if(event.which==9 && option==1){
			event.preventDefault();
			var pos = $textbox.getCursorPosition();
			$textbox.val($textbox.val().substring(0, pos) + "\t" + $textbox.val().substring(pos));
			$textbox.selectRange(pos +1,pos +1);
		}
	})
	$(window).keyup(function(event){
		if(event.which==18){
			option = 0;
		}
	})
	$textbox.keyup(function(event){
		update();
	})
	update();
});
(function($){			// this one finds the cursor position so the tab can be inserted there
	$.fn.getCursorPosition = function(){
	    var pos = 0;
	    var el = $(this).get(0);
	    // IE Support
	    if (document.selection) {
	        el.focus();
	        var Sel = document.selection.createRange();
	        var SelLength = document.selection.createRange().text.length;
	        Sel.moveStart('character', -el.value.length);
	        pos = Sel.text.length - SelLength;
	    }
	    // Firefox support
	    else if (el.selectionStart || el.selectionStart == '0')
	        pos = el.selectionStart;

	    return pos;
	}
})(jQuery);
(function($){			// this is for moving the cursor after the tab is inserted
	$.fn.selectRange = function(start, end) {
	    return this.each(function() {
	        if (this.setSelectionRange) {
	            this.focus();
	            this.setSelectionRange(start, end);
	        } else if (this.createTextRange) {
	            var range = this.createTextRange();
	            range.collapse(true);
	            range.moveEnd('character', end);
	            range.moveStart('character', start);
	            range.select();
	        }
	    });
	};	
})(jQuery);
