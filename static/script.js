var clickedBookMark = true;

function bookMark (element){

    if(clickedBookMark){

        element.src="static/images/bookmark _filled.png";
        clickedBookMark = false;
    }
    else {

        element.src="static/images/bookmark.png";
        clickedBookMark = true;
    }
}

let popUp = document.querySelector("#message-slider");

function messagePop(){

    popUp.classList.add("active");

}


document.querySelector("#message-slider").addEventListener('click', (e) =>{

    popUp.classList.add("after");

});

