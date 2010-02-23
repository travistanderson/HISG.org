
	
function pwtUpdate(allids,allnames,allurls,alltags,allorigs,allburls){
	var selectedhtml = '';
	var unselectedhtml = '';
	var temphtml = '';
	var initid = new String();			// shows the id of the selected photo
	var initpos = new String();			// shows the position in the array allids of the selected photo
	var unselected = new Array();		// this array will hold all ids except the selected one
	var searchresults = new Array();	// this is for picture which match what was typed

	initid = $(fieldname).val();	// get the value of selected photo from the hidden box
	initpos = '0';
	// $('.somediv').append(fieldname);
	
	function setup(){
		for(i=0; i<allids.length;i++){
			if(initid==String(allids[i])){
				initpos = i;
				// $('.somediv').append('when setup is run i = ' + initpos + '<br/>');
			}
		}
		// $('.somediv').append('allids.length = ' + String(allids.length) + ', initpos = ' + initpos + '<br/>');
	
		for(i=0; i<allnames.length;i++){
			searchresults[i]=false;
			if(parseInt(initpos)==i){
				unselected[i]=false;
			}else{
				unselected[i]=true;
			}
		}
	}

	function createHtml(i){
		temphtml = "<div class='photobox' id='" + allids[i] + "_photobox'><div class='photoboxid'>" + allids[i] + "</div><div class='photoboxname'>" + allnames[i] + "</div><div class='photoboxpicture'><img src='" + allurls[i] + "'></img></div><div class='photoboxtags'><div class='photoboxtagstags'>" + alltags[i] + "</div><div class='photoboxtagsorigs'>"+ allorigs[i] + "</div></div></div><div class='clear'></div>";
		return temphtml
	}
	
	// function createBlankHtml(i){
	// 	temphtml = "<div class='photobox' id='0_photobox'><div class='photoboxid'>-</div><div class='photoboxname'>Select None</div><div class='photoboxpicture'><div class='blankphoto'></div></div><div class='photoboxtags'><div class='photoboxtagstags'></div><div class='photoboxtagsorigs'></div></div></div><div class='clear'></div>";
	// 	return temphtml
	// }

	function createHtmlSelected(i){
		temphtml = "<div class='bigphotobox'><div class='bigphotoboxid'>" + allids[i] + "</div><div class='bigphotoboxname'>" + allnames[i] + "</div><div class='bigphotoboxtags'>" + alltags[i] + "</div><div class='bigphotoboxorig'>" + allorigs[i] + "</div><img src='" + allburls[i] + "'></img></div><div class='clearer'></div>";
		return temphtml		
	}

	function updateBoxes(){
		selectedhtml = '';
		unselectedhtml = '';
		// unselectedhtml = unselectedhtml + createBlankHtml(0);
		for(i=0; i<allnames.length;i++){
			if(unselected[i] == true){
				unselectedhtml = unselectedhtml + createHtml(i); 				
			}
		}
		selectedhtml = selectedhtml + createHtmlSelected(parseInt(initpos));
		// selectedhtml = initial
		$('#photo_unselected').html(unselectedhtml);
		$('#photo_selected').html(selectedhtml);
		// $('#photo_selected').html('selectedhtml');
		return true
	}

	function updateHidden(){
		$(fieldname + " option[value='" + allids[parseInt(initpos)] + "']").attr('selected', 'selected');
		return true	
	}

	function selectBoxes(){								// this function handles the swapping when you click a photobox
		initid = String(this.id).split('_').shift();
		// $('.somediv').append('clicked id = ' + initid + '<br/>');
		setup();
		updateHidden();
		updateBoxes();
		bindBoxes();
	}
	
	function bindBoxes(){								// this binds the function toggleBoxes to newly created boxes after a dump
		$('.photobox').bind("click", selectBoxes);
	}

	$.expr[":"].containsNoCase = function(el, i, m) {		// here is a customized case insensitive search function
		var search = m[3];
		if (!search) return false;
		return eval("/" + search + "/i").test($(el).text());
	};  

	setup();
	updateBoxes();  			// this will call it for the first time and get everything setup
	bindBoxes();

	// here are all the event handler buttons  =================================================

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


	


















