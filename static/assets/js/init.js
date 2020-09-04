$(document).ready(function() {

  let app = {

    // Initialize the game
    init: function() {
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

      // reset search text when focus out of the input field in navbar
      $('#nav-mobile #search_text').focusout(function() {
        $(this).val("");
      });

      // reset search text when focus out of the input field in sidenav
      $('#mobile-sidenav #search_text').focusout(function() {
        $(this).val("");
      });
    }};

  app.init();
});
