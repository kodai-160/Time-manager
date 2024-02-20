const hour = document.getElementById('hour');
const min = document.getElementById('min');
const sec = document.getElementById('sec');

function countdown() {
    const now = new Date();
    const tommorow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
    const diff = tommorow.getTime() - now.getTime();

    //ミリ秒から単位を計算
    const calcHour = Math.floor(diff / (1000 * 60 * 60));
    const calcMin = Math.floor(diff / (1000 * 60)) % 60;  
    const calcSec = Math.floor(diff / 1000) % 60;

    //取得した時間を表示
    hour.innerHTML = calcHour < 10 ? '0' + calcHour : calcHour;
    min.innerHTML = calcMin < 10 ? '0' + calcMin : calcMin;
    sec.innerHTML = calcSec < 10 ? '0' + calcSec : calcSec;
}
countdown();
setInterval(countdown, 1000);