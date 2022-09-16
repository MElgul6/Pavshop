// let form = document.querySelector('#login-form');

// form.addEventListener('submit', async function(event){
//     // event.preventDefault();
//     // console.log(form.email.value);

//     let postData = {
//         email: form.username.value,
//         password: form.password.value

//     }

//     let response = await fetch('http://localhost:8000/api/token/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(postData),

//     });
//     // console.log(JSON.stringify(await response.json()))
//     if (response.ok){
//         let data = await response.json();
//         localStorage.setItem('user-detail', JSON.stringify(data));
//         window.location = '/list'
//     }
    
    

// })