from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = '1234qwer!@#$'  # 세션을 위한 시크릿 키 설정

@app.route('/')
def index():
    session['number'] = random.randint(1, 20)  # 1에서 20 사이의 숫자를 랜덤으로 선택
    session['attempts'] = 1  # 시도 횟수 초기화
    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'GET':
        # GET 요청 시 처리 방식. 예를 들어, 메인 페이지로 리다이렉트
        return redirect(url_for('index'))
    
    try:
        user_guess = int(request.form['guess'])
    except ValueError:
        # 사용자 입력이 숫자가 아니거나 비어 있을 때
        message = '숫자를 입력해주세요!'
        sound = 'error.mp3'
        return render_template('guess.html', message=message, sound=sound, attempts=session['attempts'])

    session['attempts'] += 1
    if user_guess < session['number']:
        message = '더 높은 숫자입니다!'
        sound = 'wrong.mp3'
    elif user_guess > session['number']:
        message = '더 낮은 숫자입니다!'
        sound = 'wrong.mp3'
    else:
        message = '정답입니다!'
        sound = 'correct.mp3'

    if session['attempts'] >= 20 or user_guess == session['number']:
        session.pop('number', None)  # 게임 종료 시 숫자 세션 삭제
        session.pop('attempts', None)  # 게임 종료 시 시도 횟수 세션 삭제
        return render_template('end.html', message=message, sound=sound)  # 게임 종료 페이지 렌더링

    return render_template('guess.html', message=message, sound=sound, attempts=session['attempts'])

if __name__ == '__main__':
    app.run(debug=True)
