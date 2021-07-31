$("#submit_button").click(function (event) {
  event.preventDefault();
  if (firebase.auth().currentUser) {
    var user = firebase.auth().currentUser.uid;
  } else {
      alert('Please login');
      return false;
    };
  var temperature = $("#temperature").val();
  var temp = $('.validate-input input[name="temperature"]');
  if ($(temp).val().trim() != "") {
  $.ajax({
        data: {
          user: user,
          temperature: temperature,
        },
        type: "POST",
        url: "/temperature",
      }).done(function (data) {
        $("#form1").hide();
        $("#result").html(
          '<span class="contact100-form-title">Thank You!</span>'
        );
      });
    };
  return true;
});
