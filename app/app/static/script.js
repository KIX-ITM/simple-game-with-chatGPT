window.addEventListener('DOMContentLoaded', function(){

	// チェックボックスのHTML要素を取得
	let words = document.querySelectorAll("input[name=word]");

    //選択出来るワードを2つまでに制限する
	for(let word of words) {
	    word.addEventListener('change',function(){
		    let count = document.querySelectorAll('input[type="checkbox"]:checked').length;
		    if (count == 3) {
		        this.checked = false;
		    };
	    });
	}
});