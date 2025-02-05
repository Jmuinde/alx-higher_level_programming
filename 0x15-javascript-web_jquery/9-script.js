// Script that fethches a key from a url and displays the value.
$('document').ready(function () {
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
		$('DIV#hello').text(data.hello);
	});
});
