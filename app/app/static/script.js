window.addEventListener('DOMContentLoaded', function(){

	// チェックボックスのHTML要素を取得
	const words = document.querySelectorAll("input[name=word]");
//	const submit_answer = document.querySelector("input[name=submit-answer-checkbox");

	let selected_num = 0;

    //選択出来るワードを2つまでに制限する
	for(let word of words) {
	    word.addEventListener('change',function(){
		    let count = document.querySelectorAll('input[type="checkbox"]:checked').length;
		    selected_num = count;
		    if (count == 3) {
		        this.checked = false;
		    };
	    });
	}

//	submit_answer.addEventListener('change',function(){
//        if (selected_num != 2) this.checked = false;
//	});
});