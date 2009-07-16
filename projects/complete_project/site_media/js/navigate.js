//site_media/js/navigate.js

var page = ""
var pageperm = ""
var activenav = ""
var activesub = ""
var showernav = ""
var showersub = ""
var navarrayhome = new Array(0,0,50,300,450,750);
var navarraysecond = new Array(0,0,80,100,400,520,800);
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



// 
// function restore(event){
// 	if(event.relatedTarget.tagName == "LI"){return;}
// 	if(event.relatedTarget.tagName == "UL"){return;}
// 	if(event.relatedTarget.tagName == "A"){return;}
// 	else{
// 	//alert(event.relatedTarget.tagName);
// 	showernav = "nav" + pageperm
// 		//hide the activenav
// 		blank = document.getElementById(activenav);
// 		blank.style.background = "#FFF";
// 		// hide the activesub;
// 		for(i = 0; i < navarray[page]; i++){
// 			e = "sub" + page + (i + 1);
// 			f = document.getElementById(e);
// 			f.style.display = "none";
// 		}
// 		// show the showernav
// 		color = document.getElementById(showernav);
// 		color.style.background = "#75ba39";
// 		// show the showersub;
// 		for(i = 0; i < navarray[pageperm]; i++){
// 			g = "sub" + pageperm + (i + 1);
// 			h = document.getElementById(g);
// 			h.style.display = "inline";
// 		}
// 		activenav = showernav;
// 		page = pageperm;}
// }





// function show(shower){
// 	// showernav = "nav" + shower
// 	//hide all
// 	for(i = 0; i < navarray.length - 1; i++){
// 		for(j = 0; j < navarray[i + 1]; j++){
// 			a = "sub" + (i + 1) + (j + 1);
// 			b = document.getElementById(a);
// 			b.style.display = "none";
// 		}
// 	}
// 	// show the showersub;
// 	for(i = 0; i < navarray[shower]; i++){
// 		c = "sub" + shower + (i + 1);
// 		d = document.getElementById(c);
// 		d.style.display = "inline";
// 	}	
// 	// activenav = showernav;
// 	// page = shower;
// }


// the end
