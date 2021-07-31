$('.emergency').click(function (event) {
    event.preventDefault();
    if (firebase.auth().currentUser) {
        var user = firebase.auth().currentUser.uid;
    } else {
        alert('Please login');
        return false;
    };
    $.ajax({
          data: {
            user: user,
          },
          type: "POST",
          url: "/emergency",
        }).done(function (data) {
            alert('Sent the emergency notification. Please wait for someone to come check up on you');
        });
    return true;
});