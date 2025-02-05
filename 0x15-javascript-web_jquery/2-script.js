/* updates the text color of the <header> element. 
   When the user clicks DIV#red_header
   Uses the JQuery API
*/
$('DIV#red_header').click(function () {
	$('header').css({
		'color': 'blue'});
});
