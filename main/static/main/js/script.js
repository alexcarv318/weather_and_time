$(document).ready(function() {

    // time of the clock
    window.setInterval(function() {
        let timeText = document.getElementById('time')
        let now = new Date()

        timeText.innerHTML = now.toLocaleTimeString()
    })

    // choose the video
    const weather = document.getElementById('weather')
    const video = document.getElementById('video')

    if (weather.innerHTML === 'Clouds') {
        video.setAttribute('src', '/static/main/video/clouds1080.mp4')
    } else if (weather.innerHTML === 'Rain') {
        video.setAttribute('src', '/static/main/video/rain1080.mp4')
    } else if (weather.innerHTML === 'Sun') {
        video.setAttribute('src', '/static/main/video/sun21080.mp4')
    }
})






