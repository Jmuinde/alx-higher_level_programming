// Script to fetch data from a url.

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
	$('DIV#character').text(data.name);
});
