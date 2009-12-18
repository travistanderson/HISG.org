// /site_media/js/widgets.js

function pwtUpdate(allids,allnames,allurls,alltags,allorigs,allcaptions){
	var selectedhtml = '';
	var unselectedhtml = '';
	var temphtml = '';
	var selected = new Array();			// an item in this array is true if the photo is selected and false otherwise
	var highlighted = new Array();			// an item in this array is true if the photobox is highlighted
	var initial = new Array();
	var searchresults = new Array();
	$('#id_photo :selected').each(function(i, selected){    // get the list of highlighted names from the hidden box
	    initial[i] = $(selected).text();
	});
	
	for(i=0; i<allnames.length;i++){
		selected[i]=false;
		highlighted[i]=false;
		searchresults[i]=false;
	}
	
	for(i=0; i<allnames.length;i++){   // seperate the all array into selected and unselected based on the initial array names
		k = false;
		for(j=0; j<initial.length;j++){
			if(allnames[i] == initial[j]){
				selected[i]=true;
			}
		}
	}
	
	function createHtml(i){
		temphtml = "<div class='photobox' id='" + allids[i] + "_photobox'><div class='photoboxid'>" + allids[i] + "</div><div class='photoboxname'>" + allnames[i] + "</div><div class='photoboxpicture'><img src='" + allurls[i] + "'></img></div><div class='photoboxtags'><div class='photoboxtagstags'>" + alltags[i] + "</div><div class='photoboxtagsorigs'>"+ allorigs[i] + "</div></div></div><div class='clear'></div>";
		return temphtml
	}
	
	function updateBoxes(){
		selectedhtml = '';
		unselectedhtml = '';
		for(i=0; i<allnames.length;i++){
			if(selected[i] == false){
				unselectedhtml = unselectedhtml + createHtml(i); 				
			}
		}
		for(i=0; i<allnames.length;i++){
			if(selected[i] == true){
				selectedhtml = selectedhtml + createHtml(i); 				
			}
		}
		$('#photo_unselected').html(unselectedhtml);
		$('#photo_selected').html(selectedhtml);
		return true
	}
	
	function updateHidden(){
		for(i=0;i<allids.length;i++){
			if(selected[i]==true){
				$("#id_photo option[value='" + allids[i] + "']").attr('selected', 'selected');
			}
		}
		return true	
	}

	function toggleBoxes(){								// this function handles the the highlighting of boxes when they are clicked
		var idstring = String(this.id).split('_').shift();
		if(highlighted[idstring] == true){
			highlighted[idstring] =false;
			$(this).removeClass("photoboxhighlighted");
		}
		else{
			highlighted[idstring] =true;
			$(this).addClass("photoboxhighlighted");
		}
	}
	
	function bindBoxes(){								// this binds the function toggleBoxes to newly created boxes after a dump
		$('.photobox').bind("click", toggleBoxes);
	}



	$.expr[":"].containsNoCase = function(el, i, m) {		// here is a customized case insensitive search function
		var search = m[3];
		if (!search) return false;
		return eval("/" + search + "/i").test($(el).text());
	};  




	
	updateBoxes();  			// this will call it for the first time and get everything setup
	bindBoxes();

	// here are all the event handler buttons  =================================================




	$('#photo_select_add').click(function(){      // this is for when you click the add button, it should move the photos over and update the hidden real box
		$('#id_photo option').attr('selected', false);
		$('#photo_unselected > .photoboxhighlighted').each(function( intIndex ){		// find idstring in allids array and return index number
			var idstring = String(this.id).split('_').shift();
			for(i=0;i<allids.length;i++){
				if(idstring==allids[i]){
					selected[i]=true;
				}
			}			
		})
		updateHidden();
		updateBoxes();
		bindBoxes();
	})
	
	$('#photo_select_remove').click(function(){      // this is for when you click the remove button, it should move the photos over and update the hidden real box
		$('#id_photo option').attr('selected', false);
		$('#photo_selected > .photoboxhighlighted').each(function( intIndex ){		// find idstring in allids array and return index number
			var idstring = String(this.id).split('_').shift();
			for(i=0;i<allids.length;i++){
				if(idstring==allids[i]){
					selected[i]=false;
				}
			}
		})
		updateHidden();
		updateBoxes();
		bindBoxes();
	})
	
	
	$("#photosearchboxinput1").keyup(function() {
		if(this.value != ''){
			$('#photo_unselected > .photobox').addClass('hiddenPhotobox');
			$("#photo_unselected > .photobox:containsNoCase(" + this.value + ")").removeClass("hiddenPhotobox");
		}
		else{
			$("#photo_unselected > .photobox").removeClass("hiddenPhotobox");
		}

	});

	$('.photosearchboxclear').click(function(){			// this will clear the text box and bring back all the photos
		$('#photosearchboxinput1').val('');
		$("#photo_unselected > .photobox").removeClass("hiddenPhotobox");
	})
	

}





