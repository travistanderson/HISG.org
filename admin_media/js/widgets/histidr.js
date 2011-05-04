$(document).ready(function() {
	var value = $('#id_histidr_set-0-histidr :selected').text();

	var $histkids = $('.hist1')
		.add('.hist2')
		.add('.hist3')
		.add('.hist4')
		.add('.hist5')
		.add('.hist6')
		.add('.hist7')
		.add('.hist8')
		.add('.hist9')
		.add('.hist10')
		.add('.hist11')
		.add('.hist12'); 


	var $idrkids = $('.idr1')
		.add('.idr2')
		.add('.idr3')      
		.add('.idr4')      
		.add('.idr5')      
		.add('.idr6')      
		.add('.idr7')      
		.add('.idr8')      
		.add('.idr9')      
		.add('.idr10')
		.add('.idr11')
		.add('.idr12')
		.add('.idr13')
		.add('.idr14');
		
	// var $histkids = $histkids.parent();
	// var $idrkids = $idrkids.parent();


	function hidehistidr(value){
		if(value=="HIST"){
			$histkids.css({"display":""});
			$idrkids.css({"display":"none"});
		}
		if(value=="IDR"){
			$idrkids.css({"display":""});
			$histkids.css({"display":"none"});
		}
	}
	// hidehistidr(value);
	
	$("#id_histidr_set-0-histidr").bind("change", function(){
		var value = $("#id_histidr_set-0-histidr :selected").text();
		// hidehistidr(value);
	})
});







