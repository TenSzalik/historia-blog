var $temp = $("<input>");
var $url = $(location).attr('href');

$('.clipboard').on('click', function() {
  $("body").append($temp);
  $temp.val($url).select();
  document.execCommand("copy");
  $temp.remove();
  alert("skopiowano link!");
})

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

$(document).on("click", ".heart" , function(){
  document.cookie = 'Serce=True';
  doSomething();
  $('.ALLheart').load('/serce');
  $('.ALLheart').hide().load(document.URL +  ' .ALLheart').fadeIn('500');
  $('.ALLheart').hide().load(document.URL +  ' .ALLheart').fadeIn('500');
});

function getCookie(name) {
  var dc = document.cookie;
  var prefix = name + "=";
  var begin = dc.indexOf("; " + prefix);
  if (begin == -1) {
      begin = dc.indexOf(prefix);
      if (begin != 0) return null;
  }
  else
  {
      begin += 2;
      var end = document.cookie.indexOf(";", begin);
      if (end == -1) {
      end = dc.length;
      }
  }
  // because unescape has been deprecated, replaced with decodeURI
  //return unescape(dc.substring(begin + prefix.length, end));
  return decodeURI(dc.substring(begin + prefix.length, end));
} 

function doSomething() {
  var myCookie = getCookie("Serce");

  if (myCookie == null) {
      console.log("nie ma ciastka");
  }
  else {
      $(".heart").addClass('selected');
      console.log("jest ciastko ;)");
  }
}

doSomething();

$(window).on("load", function(){
  $(".loader-wrapper").fadeOut("slow");
})

