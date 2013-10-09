$.extend({
  						reAjaxed : function(inurl,inlocation){
							$.ajax({
							type: "GET",
							url: inurl,
							data: { },
							success: function(data, textStatus) {
        					if (data.redirect) {
            				window.location.href = data.redirect;
            				alert("Please Log in");
        					}
        					else {
        					}
    						}
    						
							})
							.done(function( msg ) {
							$(inlocation).replaceWith(msg);
							});	
						},
						});