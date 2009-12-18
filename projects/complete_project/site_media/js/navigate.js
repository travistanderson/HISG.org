//site_media/js/navigate.js

var page = ""
var pageperm = ""
var activenav = ""
var activesub = ""
var showernav = ""
var showersub = ""
var navarrayhome = new Array(0,0,50,343,450,750);
var navarraysecond = new Array(0,0,80,100,420,500,800);
var switcharray = new Array();

function showsecond(shower,subshower){
	$(document).ready(function(){
		clas = ".sub" + shower;
		$(clas).css({display: "inline"});
		padder = "0 0 0 " + navarraysecond[shower] + "px";
		namfirst = clas + ":first"; 
		$(namfirst).css({padding:padder});
		if (subshower != 0){	
			sub = "#sub" + shower + subshower + " > a";
			$(sub).css({color: "#238fb0"});
		}	
	})
}

function hoversecond(shower){
	$(document).ready(function(){
		$("#navigation > li").mouseover(function(){
			for(i = 1; i < navarraysecond.length; ++i){
				clas = ".sub" + i;
				$(clas).css({display: "none"});
			}
			$(".sub0,.inyes").css({display:"none"});
			clas = $(this).attr("id");
			num = clas.slice(2,3);  //this chops the "id" off the front and leaves only the number
			nam = ".sub" + num;  //this contructs the name off the appropriate submenu
			namfirst = nam + ":first";
			padder = "0 0 0 " + navarraysecond[num] + "px";
			$(nam).css({display:"inline"});
			$(namfirst).css({padding:padder});
		})
	})
}

function quickpick(){
	$(document).ready(function(){
		$(".quickpick").hover(
			function(){$(".quickhide").css({display:"block"});},
			function(){$(".quickhide").css({display:"none"});}
		)
		
	})
}

function shower(){
	$(document).ready(function(){
		$("#navigation > li").mouseover(function(){
			for(i = 1; i < navarrayhome.length; ++i){
				clas = ".sub" + i;
				$(clas).css({display: "none"});
			}
			$(".sub0,.inyes").css({display:"none"});
			clas = $(this).attr("id");
			num = clas.slice(2,3);  //this chops the "id" off the front and leaves only the number
			nam = ".sub" + num;  //this contructs the name off the appropriate submenu
			namfirst = nam + ":first";
			padder = "0 0 0 " + navarrayhome[num] + "px";
			$(nam).css({display:"inline"});
			$(namfirst).css({padding:padder});
		})
	})
}

function hider(){
	$(document).ready(function(){
		$(".subnav").mouseout(function(){
			for(i = 1; i < navarrayhome.length; ++i){
				clas = ".sub" + i;
				$(clas).css({display: "none"});
				$(".sub0,.inyes").css({display:"inline"});
			}
		})
	})
}

function initial(){
	$(document).ready(function(){
		$(".sub0").css({display: "inline",padding:"0 0 0 200px"});		
		$(".inyes").css({display: "inline",});	
	})
}

function tininav(){
	$(document).ready(function(){
		var text = $(".tini_highlight").text();
		var tiniArray = new Array();
		tiniArray = text.split(",");
		for (i=0;i<tiniArray.length;i++){
			var whichone = "#tini" + tiniArray[i];
	 		$(whichone).css({color: "#3f97ba",});
		}
	})
}

// here is the function to rotate around the photos on a photopicker.html include
$(document).ready(function() {
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


// these are the arrays with the photo data
// var photoids = new Array();
// var photodisplays = new Array();
// var photothumbs = new Array();		
// var photocaptions = new Array();





// the end
