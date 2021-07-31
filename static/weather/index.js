function get_weather() {
    $.ajax({
          type: "GET",
          url: "/weather",
        }).done(function (data) {
          console.log(data)
          var date = new Date()
          const options = { weekday: "long", month: "long", day: "numeric", hour: "numeric", minute: "numeric"}
          $('.today').html(date.toLocaleDateString('en', options))
          $('.weather-detail').html(data['weather'][0]['description'])
          $('.pressure').html(`${Math.round(data['main']['pressure']*0.75)} mm Hg`)
          $('.humid').html(`${data['main']['humidity']}% humidity`)
          var dir = {0:'E', 1:'NE', 2:'N', 3:'NW', 4:'W', 5:'SW', 6:'S', 7:'SE', 8:'E'}
          $('.wind-speed').html(`${data['wind']['speed']}m/s ${dir[Math.round(data['wind']['deg']/45)]}`)
          $('.max-temp').html(Math.round(data['main']['temp_max']-273.15))
          $('.temperature-feels').html(`+${Math.round(data['main']['feels_like']-273.15)} feels`)
        });
    return false;
  };
  