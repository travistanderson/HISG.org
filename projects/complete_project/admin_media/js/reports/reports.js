var students = new Array();				// this holds all the original info
var newstudents = students;			// this will be a copy of the original only sorted or filtered or both

function student(uid,namer,email,badgephoto,country,organization,job,credentials){
	this.uid=uid;
	this.namer=namer;
	this.email=email;
	this.badgephoto=badgephoto;
	this.country=country;
	this.organization=organization;
	this.job=job;
	this.credentials=credentials;
}

function createhtml(i){						// this writes on row of html at a time for a given student
	stu = newstudents[i];
	return "<div class='rp-student'><div class='rp-st-checker'><input type='checkbox' name='dude_list' value='" + String(stu.uid) + "' /></div><div class='rp-st-badge'><img src='" + String(stu.badgephoto) + "' class='pic' alt='pic'></img></div><div class='rp-st-name'>" + stu.namer + "<br/>" + stu.email + "<br/>" + String(stu.uid) + "</div><div class='rp-st-country'>" + stu.country + "</div><div class='rp-st-org'>" + stu.organization + "</div><div class='rp-st-job'>" + stu.job + "</div><div class='rp-st-cred'>" + stu.credentials + "</div></div><div class='clearer'></div>";
}
function inithtml(){						// this sets up all the rows of html in the main window
	$('.rp-student-box').html('');
	for(i=0;i<newstudents.length;i++){
		var thehtml = createhtml(i);
		$('.rp-student-box').append(thehtml);
	}
}

var cursort = 'id';
var cursortud = 'down';

// wwc == what was clicked for the sort tools

$(document).ready(function() {
	
	// this is the click handler for the sorting controls
	$('.rp-controls > div').click(function(){
		var wwc = String(this.id).split('-').pop();
		
		if($(this).hasClass('rphl')){		// is it highlighted?
			if($(this).hasClass('arrowup')){	// is it sorted ascending?
				// resort it to sorted descending
				sortit(attr,updown);
				$(this).removeClass('arrowup').addClass('arrowdown');
			}else{								// it is not sorted ascending
				$(this).removeClass('arrowdown').addClass('arrowup');
				// resort it to sorted ascending
				sortit(attr,updown);
			}
		}else{								// it is not highlighted
			$('.rp-controls > div').removeClass('rphl').removeClass('arrowup').removeClass('arrowdown');
			$(this).addClass('rphl').addClass('arrowdown');
			// resort it to this and sorted descending
			sortit(attr,updown);
		}
		
		
		$('.somediv').append(wwc);
	})
	
	// this is my sorting function  -- it takes two parameters, attr -> attirbute to sort by and updown -> whether it is up or down
	function sortit(attr,updown){
		newstudents = students;
		// uid
		// namer
		// email
		// badgephoto
		// country
		// organization
		// job
		// credentials
		if (attr=='namer'){
			newstudents.sort(function(a,b){
				var compA = $(a).namer.toUpperCase();
				var compB = $(b).namer.toUpperCase();
				if(updown=='up'){
					return (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
				}else{
					return (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
				}
				
			})
		}
		
	}
	
	
	
	
	$('.somediv').append('hello');
	
	
});

	
