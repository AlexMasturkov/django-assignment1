$("#my_font").on("mouseover",function(){
    $("body").css("font-family", "Impact"); 
})

$("button").on("mouseover",function(){
    $(this).css("color","yellow");
});

$("button").on("mouseout",function(){
    $(this).css("color","white");
});

$("#my_theme").on("mouseover",function(){
    $("h3").css("color","white");
    $("body").css("background-color","teal");
    $("form").css("color","white");
    $("footer").css("color","white");
    $("th").css("background-color","teal");
});

$( "footer" ).click(function() {
   $("footer").css("border", "3px double white");
   $("footer").css("font-size"," 1.2em");

    
  });
