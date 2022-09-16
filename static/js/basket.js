let updateBtns = document.getElementById('update-cart')

updateBtns.addEventListener('click', async function(event){
    event.preventDefault()
    let productId = this.dataset.product
    let action = this.dataset.action
    let quantity = document.getElementById('quantity').value

    if (user === 'Anonymous user'){
        window.alert('Not logged in')
    }
    else{
        createBasketItem(productId, action, quantity);
    }
})


function createBasketItem(productID, action, quantity){
    let url = '/api/basket_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body:JSON.stringify({'productID': productID, 'action': action, 'quantity': quantity}),
    })

    .then((response)=>{
        return response.json();
    })
}