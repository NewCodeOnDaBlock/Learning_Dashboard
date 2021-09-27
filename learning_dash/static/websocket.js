const socket = io.connect('http://127.0.0.1:5000/')

socket.on('connect', () => {
    const userID = document.querySelector('.user').value
    console.log('connected!', userID)
    socket.emit('connected', {'user_id' : userID })
})


socket.on('request-sent',(data) => {

    // adding friend request to the html //
    console.log('request sent successfully')
    console.log(data.first_name)
})


socket.on('request-accept', (data) => {

    // adding friend request to the html //
    console.log('request accepted')
})


socket.on('request-deny', (data) => {

    // deny friend request to the html //
    console.log('request denied')
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

for(let requestForm of requestForms) {

    requestForm.querySelector('.accept').addEventListener('click', (e) => {

        e.preventDefault()
        const userID = requestForm.querySelector('input').value;
        socket.emit('accepting-request', {'sender_id': userID })
        requestForm.remove()
    
    })
    requestForm.querySelector('.deny').addEventListener('click', (e) => {

        e.preventDefault()
        const userID = requestForm.querySelector('input').value;
        socket.emit('denying-request', {'sender_id': userID })
        requestForm.remove()
    
    })
    
}



/*
const acceptBtns = document.querySelectorAll('.accept');

for(let accept_button of acceptBtns){

    accept_button.addEventListener('click', (e) => {
        e.preventDefault()

        const form = document.querySelector('.request-form');
        const userID = form.querySelector('input').value;
        socket.emit('accepting-request', {'sender_id': userID })
        form.remove()
    })
}

const denyBtns = document.querySelectorAll('.deny');

for(let deny_button of denyBtns ){

    deny_button.addEventListener('click', (e) => {
        e.preventDefault()

        /* const form = e.target.parentNode.parentNode.parentNode 
        const form = document.querySelector('.request-form');
        const userID = form.querySelector('input').value;
        socket.emit('denying-request', {'sender_id': userID })
        form.remove()
    })
}

*/
//------------------------------------------------//

