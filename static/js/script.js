document.addEventListener('DOMContentLoaded', function() {
    const musicToggleButton = document.getElementById('music-toggle');
    const backgroundMusic = document.getElementById('background-music');
    let isMusicPlaying = false;

    // 음악 재생/멈춤 버튼 이벤트 리스너
    musicToggleButton.addEventListener('click', function() {
        if (isMusicPlaying) {
            backgroundMusic.pause();
        } else {
            backgroundMusic.play();
        }
        isMusicPlaying = !isMusicPlaying;
    });

    // 정답과 오답을 체크하는 로직이 여기에 들어갑니다.
    // 예를 들어, 정답을 맞췄을 때와 틀렸을 때를 처리하는 함수를 구현할 수 있습니다.
});

// 정답을 맞췄을 때의 함수
function playCorrectSound() {
    const correctSound = document.getElementById('correct-sound');
    correctSound.play();
}

// 오답을 선택했을 때의 함수
function playWrongSound() {
    const wrongSound = document.getElementById('wrong-sound');
    wrongSound.play();
}
