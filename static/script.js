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

setTimeout(messagePop, 3000)


function notificationPop(){

    popUp.classList.add("after");

}

setTimeout(notificationPop, 7000)


var clickedChat = true;
let chatUs= document.querySelector("#chatwithus");

document.querySelector('.chat').addEventListener('click', (e) => {

    chatUs.classList.add("active");
    
})

document.querySelector('#main-container').addEventListener('click', (e) => {

    chatUs.classList.add("after");

})

let customerThanks = document.querySelector('#chatwithus');

function thankYouMessage(){

    customerThanks.innerHTML = "<div><p>Thanks! We\'ll message you shortly! <br> You may click anywhere outside the box to exit.</p></div>"

}

