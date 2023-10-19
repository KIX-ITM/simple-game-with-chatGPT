window.addEventListener('DOMContentLoaded', function(){

	// チェックボックスのHTML要素を取得
	const words = document.querySelectorAll("input[name=word]");
	let selectedNum = 0;

    // 選択出来るワードを2つまでに制限する
	for(let word of words) {
	    word.addEventListener('change',function(){
		    let count = document.querySelectorAll('input[name=word]:checked').length;
		    selectedNum = count;
		    if (count == 3) {
		        this.checked = false;
		    };
	    });
	}

    // 確認ボタンをチェック時に正解不正解を判定
    const answerCheckbox = document.getElementById('confirm-answer-checkbox');
    const popupMsgTitle = document.getElementById('popup-msg-title');
    const popupMsgContent = document.getElementById('popup-msg-content');

    answerCheckbox.addEventListener('change',setCorrectOrNot);
    function setCorrectOrNot() {
        let checkedWords = document.querySelectorAll('input[name=word]:checked');
        let count = checkedWords.length;
        let correct = true;
        if (this.checked && count < 2) {
            popupMsgTitle.innerText = '【不正解】';
            popupMsgContent.innerText = '共通点に当てはまる言葉を「2つ」選択してください。';
        };
        if (this.checked && count == 2) {
            let incorrectWord = this.value;
            console.log(incorrectWord);
            for(word of checkedWords) {
                if (word.value == incorrectWord) correct = false;
            };
            if (correct) {
                popupMsgTitle.innerText = '【正解】';
                popupMsgContent.innerText = 'おめでとうございます！！\nあなたはロボットではありません。';
            } else {
                popupMsgTitle.innerText = '【不正解】';
                popupMsgContent.innerText = '残念…。\nあなたはロボットです。';
            };
        };
    }
});

function setAnswerVisibility() {
  if (document.getElementById('switch-checkbox').checked){
    // hidden-answerを非表示,answerを表示
    document.getElementById('show-answer').style.display = 'none'
    document.getElementById('hidden-answer').style.display = 'inline'
  }else{
    // hidden-answerを表示,answerを表示
    document.getElementById('show-answer').style.display = 'inline'
    document.getElementById('hidden-answer').style.display = 'none'
  }
}