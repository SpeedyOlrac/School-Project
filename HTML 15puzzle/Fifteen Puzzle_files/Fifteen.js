/*
	Author: Carlo Gonzalez
	Class: CS 366
	Secion: 1
	Description: CSS Page for Rancid Tomatoes.
		With centered contect box and HTML/CSS checkers. 

-*/
var idx = 1
$('#puzzlearea > div').each(function(idx){ 
	$(this).attr('id', 'sq-'+idx);
	console.log('sq-'+idx);
});

//make a fuction that goes though each row and another on that goes though each collum

function pos_incr(xpos, ypos){
	xpos += 25;
	if (xpos == 100){
		xpos = 0;
		ypos += 25;
	}
}

var xPos = 0;
var yPos = 0;
$('#puzzlearea > div').each(function(xPos, yPos){
	var pos = xPos + "% " + yPos + "%"
	$(this).attr('background-position', pos );
	pos_incr(xPos, ypos);
});