$(document).ready(function() {
  $(".button-collapse").sideNav();
  $('.parallax').parallax();
  $('.collapsible').collapsible();
  $('select').material_select();

  $('.modal').modal();

  // for select "required" attribute
  $("select[required]").css({
    display: "inline",
    height: 0,
    padding: 0,
    width: 0
  });
  $('#textarea1').val('New Text');
  $('#textarea1').trigger('autoresize');

});
