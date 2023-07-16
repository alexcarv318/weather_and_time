$(document).ready(function() {
    
    const weather = document.getElementById('weather')
    const video = document.getElementById('video')
    const image = document.getElementsByClassName('weather-image')
    const card = document.getElementsByClassName('card')
    const weatherForecast = document.getElementsByClassName('weather-text')

    if (weather.innerHTML === 'Clouds') {
        video.setAttribute('src', '/static/main/video/clouds1080.mp4')
    } else if (weather.innerHTML === 'Rain') {
        video.setAttribute('src', '/static/main/video/rain1080.mp4')
    } else if (weather.innerHTML === 'Sun') {
        video.setAttribute('src', '/static/main/video/sun21080.mp4')
    }

    for (let i = 0; i < weatherForecast.length; i++) {
        if (weatherForecast[i].innerHTML === 'Clouds') {
            image[i].setAttribute('src', '/static/main/img/partly_cloudy.png')
            card[i].style.backgroundColor = 'rgba(235, 236, 242, 70%)'
        } else if (weatherForecast[i].innerHTML === 'Rain') {
            image[i].setAttribute('src', '/static/main/img/rainy.png')
            card[i].style.backgroundColor = 'rgba(235, 236, 242, 30%)'
        } else if (weatherForecast[i].innerHTML === 'Sun') {
            image[i].setAttribute('src', '/static/main/img/sunny.png')
            card[i].style.backgroundColor = 'rgba(235, 236, 242, 70%)'
        } else if (weatherForecast[i].innerHTML === 'Clear') {
            image[i].setAttribute('src', '/static/main/img/sunny.png')
            card[i].style.backgroundColor = 'rgba(235, 236, 242, 70%)'
        }
    }
    console.log(card)
})
