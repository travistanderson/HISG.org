//site_media/js/navigate2.js

var activenav = ""
var navarrayhome = new Array(0,0,50,343,450,750);			// this array spaces out the subnav on the homepage
var navarraysecond = new Array(0,0,80,50,420,500,800);		// this array spaces out the subnav on all the other pages


$(document).ready(function(){
	$('.subnav > li').hide();						// hide all the subnav groups at page load
	$('#navigation > li').each(function(i){			// find which nav is active by id 
		if($(this).children().hasClass('active')){
			activenav = $(this).attr('id').split('_')[1];
		}
	})
	function leftadjust(an){						// put left padding on active subnav group
		totwid = 0;
		$('.sub_' + an).each(function(i){
			totwid = totwid + parseInt($(this).outerWidth());
		});
		// alert(totwid);
		if(totwid<1025){						// we have 1025 pixels of total width to work with
			extra = 1025 - totwid;
			if(activenav == 1){
				center = (an * 205)-307;				
			}else{
				center = (an * 170)-85;				
			}
			leftedge = center - (totwid/2);
			rightedge = center +(totwid/2);
			if(leftedge > 50){
				if(rightedge > 975){
					lpad = 975-totwid;
				}else{
					lpad = leftedge;				
				}
			}else{
				lpad = 50;
			}
		}else{lpad = 50;}
		lpad = String(lpad) + 'px';
		$('.subnav').css({'padding-left':lpad});
	}
	leftadjust(activenav);
	$('.sub_' + activenav).show();			//show the active subnav grouping at page load
	
	$('#nav').hover(function(){
		$('.rootnav').hover(function(){
			hovernav = $(this).attr('id').split('_')[1];
			// alert(hovernav)		
			$('.subnav > li').hide();
			leftadjust(hovernav);
			$('.sub_' + hovernav).show();
		},function(){})	
	},function(){
		$('.subnav > li').hide();
		leftadjust(activenav);
		$('.sub_' + activenav).show();
	})
	
	$(".quickpick").hover(
		function(){
			$(".quickhide").css({'display':"block"});
			$(".quickpick").css({'width':'150px'});
		},
		function(){
			$(".quickhide").css({display:"none"});
			$(".quickpick").css({'width':''});
		}
	)


	// here is the function to rotate around the photos on a photopicker.html include

	function makeImage(v){
		imgstring = "<img class='gold5' src='" + v +"' />";
		return imgstring;
	}

	$('.thumbpic').click(function(){
		var place = String(this.id).split('_').shift();
		var idstring = positions[place];
		var mainstring = positions[0];
		$('.mainpic').html(makeImage(photodisplays[idstring]));
		$('.news-detail-photo > .caption').html(photocaptions[idstring]);
		$(this).html(makeImage(photothumbs[mainstring]));
		positions[place]=mainstring;
		positions[0]=idstring;
	})
});


// function tininav(){
// 	var text = $(".tini_highlight").text();
// 	var tiniArray = new Array();
// 	tiniArray = text.split(",");
// 	for (i=0;i<tiniArray.length;i++){
// 		var whichone = "#tini" + tiniArray[i];
//  		$(whichone).css({color: "#3f97ba",});
// 	}
// }


// the end
