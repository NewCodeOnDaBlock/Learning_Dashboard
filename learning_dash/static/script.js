var clickedBookMark = true;

function bookMark (element){

    if(clickedBookMark){

        element.src="/static/images/bookmark _filled.png";
        clickedBookMark = false;
    }
    else {

        element.src="/static/images/bookmark.png";
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
    document.querySelector("#overlay").style.display = "block";
    
})

document.querySelector('#overlay').addEventListener('click', (e) => {

    chatUs.classList.add("after");
    document.querySelector("#overlay").style.display = "none";

})

let customerThanks = document.querySelector('#chatwithus');

function thankYouMessage(){

    customerThanks.innerHTML = "<div><p>Thanks! We\'ll message you shortly! <br> You may click anywhere outside the box to exit.</p></div>"

}

let profilePic = document.querySelector('#logout-popup');
let signOutLink = document.querySelector('.signOutLink')
let hoveredProfilePic = true;

function signOutPop(){

    profilePic.classList.add("active");

}

function hideSignOutPop(){

    profilePic.classList.add("after");

}

document.querySelector('.signOutLink').addEventListener('mouseout', (e) =>{

    profilePic.classList.add('after')

})


//----------------------------------------------------------------------------//



