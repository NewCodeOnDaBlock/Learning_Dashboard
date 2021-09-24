const socket = io.connect('http://127.0.0.1:5000/')

socket.on('connect', () => {
    console.log('hi')
    socket.emit('connected', {'user_id' : userID })
})


const friendRequestLinks = document.querySelectorAll('.sendFriendRequest');

for(let link of friendRequestLinks){

    link.addEventListener('click', (e) => {
        e.preventDefault()
        e.target.innerText = "Awaiting Request Response";
        socket.emit('sending-request', {'receiver_id': e.target.getAttribute('data-userid') })
        
    })
}

const requestForms = document.querySelectorAll('.request-form');

requestForm.addEventListener('submit', (e) => {

    e.preventDefault()

})


const acceptBtns = document.querySelectorAll('.accept');

for(let accept_button of acceptBtns){

    accept_button.addEventListener('click', (e) => {
        e.preventDefault()

        const form = e.target.parentNode.parentNode.parentNode
        const userID = form.querySelector('input').value;
        socket.emit('accepting-request', {'sender_id': userID })
        form.remove()
    })
}

const denyBtns = document.querySelectorAll('.deny');

for(let deny_button of denyBtns ){

    deny_button.addEventListener('click', (e) => {
        e.preventDefault()

        const form = e.target.parentNode.parentNode.parentNode
        const userID = form.querySelector('input').value;
        socket.emit('denying-request', {'sender_id': userID })
        form.remove()
    })
}


socket.on('request-sent', (data) => {

    // adding friend request to the html //
    console.log('request sent successfully')
})


socket.on('request-accept', (data) => {

    // adding friend request to the html //
    console.log('request accepted')
})


socket.on('request-deny', (data) => {

    // adding friend request to the html //
    console.log('request denied')
})




