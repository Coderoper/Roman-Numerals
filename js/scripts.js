function roman(number) {

  var number_maps = {M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1};

  var roman_value = "" // string to store the roman number_maps
  for(var roman_char in number_maps) {
    while( number >= number_maps[roman_char]) { // search for number in the list that is less than the user input number

      roman_value += roman_char; // append the character in the string
      number -= number_maps[roman_char]; // decrement the number_maps
    }
  }
  return  roman_value; // return the string
}

$(document).ready(function() {

  $("form#convert").submit(function(event) {
    event.preventDefault();

    $("span.result").text(roman($("input#romanNumeral").val()));
    $(".output").show();
  });

});
