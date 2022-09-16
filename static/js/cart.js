function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


async function postfunction(){
var updateBtnss = document.querySelectorAll('.update-cart');
for  (var updateBtn of updateBtnss) {
    updateBtn.addEventListener('click', function(event) {
    event.preventDefault()
    var productId = this.dataset.product
    var title = this.dataset.title
    var description = this.dataset.description
    var image = this.dataset.image
    var cart=this.dataset.cart
    // console.log(document.getElementById('product-qty').value)
   var quan=1
    if (document.getElementById('product-qty')) {
        quan=document.getElementById('product-qty').value
    }
   
    let postData={
        'product': productId,
        'quantity': quan,
        'cart':cart
        } 

    $.ajax({
        headers: { 
                'Content-Type':'application/json',
				'X-CSRFToken':csrftoken},
        type : 'POST',
        contentType: "application/json",
        url :  "/api/cart/",
        data : JSON.stringify(postData),
        success : function(response){
            if (response[0]==undefined){
                // console.log(response['get_image'])
                document.querySelector('.basket').innerHTML +=
                `<li class="bask" value=${response.id} data-sub='343'>
                <div class="media-left">
                  <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${response.get_image}" alt="..."> </a> </div>
                </div>
                <div class="media-body">
                  <h6 class="media-heading">${response.get_title}</h6>
                  <span class="price">${response.get_price}</span> <span class="qty">QTY: ${response.quantity}</span> </div>
              </li>`
              document.querySelector('.subt').innerHTML =`<li>
              <h5 class="text-center">SUBTOTAL: ${response.sub_total} USD</h5>
              </li>`
            }
            else{
                document.querySelector('.basket').innerHTML =``
                document.querySelector('.subt').innerHTML =``
                for (let item of response) {
                    console.log(item.get_image)

                    document.querySelector('.basket').innerHTML +=
                    `<li class="bask" value=${item.id} data-sub='343'>
                    <div class="media-left">
                      <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${item.get_image}" alt="..."> </a> </div>
                    </div>
                    <div class="media-body">
                      <h6 class="media-heading">${item.get_title}</h6>
                      <span class="price">${item.get_price}</span> <span class="qty">QTY: ${item.quantity}</span> </div>
                  </li>`
                  document.querySelector('.subt').innerHTML =`<li>
                  <h5 class="text-center">SUBTOTAL: ${item.sub_total} USD</h5>
                  </li>`
                }
            }
          
        },
        error : function(response){
            console.log('orda')
            console.log(response)
        }
    });
    
})}  
  
testfunction();
};


async function testfunction() {
let response = await fetch('http://localhost:8000/api/cart/');
let items = await response.json();
// var subtotal=0;
for await (let item of items){
    
    if(item['cart']['status']==false){
        if (document.querySelector('.order-detail')) {
            document.querySelector('.order-detail').innerHTML += `
            <p>${item['product']['title']} <span>${item.total_price}  $ </span></p>`
            document.querySelector('.all-total').innerHTML=`
            TOTAL COST  <span> ${item.sub_total} $</span>`
                        
        }
        document.querySelector('.basket').innerHTML +=
        `<li class="bask" value=${item.id} data-sub=${item.total_price}>
        <div class="media-left">
          <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${item['product']['main_image']}" alt="..."> </a> </div>
        </div>
        <div class="media-body">
          <h6 class="media-heading">${item['product']['title']}</h6>
          <span class="price">${item['product']['price']}</span> <span class="qty">QTY: ${item.quantity}</span> </div>
      </li>`
        document.querySelector('.subt').innerHTML =`<li>
        <h5 class="text-center">SUBTOTAL: ${item.sub_total} USD</h5>
        </li>`
        if (document.querySelector('.cart-item')) {
        document.querySelector('.cart-item').innerHTML += 
        `<ul class="row cart-details">
        <li class="col-sm-6">
            <div class="media"> 
            <!-- Media Image -->
            <div class="media-left media-middle"> <a href="#." class="item-img"> <img class="media-object" src="${item['product']['main_image']}" alt=""> </a> </div>
            
            <!-- Item Name -->
            <div class="media-body">
                <div class="position-center-center">
                <h5>${item['product']['title']}</h5>
                <p>${item['product']['description']}</p>
                </div>
            </div>
            </div>
        </li>
        
        <!-- PRICE -->
        <li class="col-sm-2">
            <div class="position-center-center"> <span class="price"><small>$</small>${item['product']['price']}</span> </div>
        </li>
        
        <!-- QTY -->
        <li class="col-sm-1">
        <div class="position-center-center">
            <div class="quinty"> 
            <!-- QTY -->
            <input  type="number" class="item-qty form-control form-control-lg text-center" data-product=${item['product']['id']} data-id=${item.id} value="${item.quantity}">
            </div>
        </div>
        </li>
    
        <!-- TOTAL PRICE -->
        <li class="col-sm-2">
            <div class="position-center-center"> <span class="price"><small>$</small>${item.total_price}</span> </div>
        </li>
        
        <!-- REMOVE -->
        <li class="col-sm-1 closebtn" >
            <div class="position-center-center"> <a href="#."><i class="icon-close" data-sub=${item.sub_total} data-total=${item.total_price} data-close=${item.id} ></i></a> </div>
        </li>
        </ul>`
        var qtyBtnss=document.querySelectorAll('.item-qty')
        for  (var qtyBtn of qtyBtnss) {
                qtyBtn.addEventListener('input', function(event) {
                event.preventDefault()
                var itemid = this.dataset.id
                var productId = this.dataset.product
                var qty = this.value
                // console.log(itemid,productId,qty)
                let postData={
                    'product': productId,
                    'quantity': qty,
                    }
                    $.ajax({
                        headers: { 
                            'Content-Type':'application/json',
                            'X-CSRFToken':csrftoken, 
                                  },
                    type : 'PATCH',
                    contentType: "application/json",
                    url :  `/api/cart/${itemid}/`,
                    data : JSON.stringify(postData),
                    success : function(response){
                        setTimeout(function(){
                        location.reload();
                    },100);
                    },
                    error : function(response){
                        console.log(response)
                    }
                            });
                }); 
        }
    
        var closeBtnss = document.querySelectorAll('.icon-close');
        for  (var closeBtn of closeBtnss) {
            var sub_tot = closeBtn.dataset.sub
            console.log(sub_tot)
            closeBtn.addEventListener('click', function(event) {
            event.preventDefault()
            var Cartid = this.dataset.close
            var tot = this.dataset.total
            var sub = this.dataset.sub
            // var sub_tot=sub
            
            event.currentTarget.parentNode.parentNode.parentNode.parentNode.remove();
            document.querySelectorAll('.bask').forEach(i => 
                {
                 if (i.value==Cartid){
                     i.remove();
                                     
                 }
             });
            sub_tot-=tot
            console.log(sub_tot)
            document.querySelector('.subt').innerHTML =`<li>
                <h5 class="text-center">SUBTOTAL: ${sub_tot} USD</h5>
                </li>`
    
            $.ajax({
                headers: { 
                    'Content-Type':'application/json',
                    'X-CSRFToken':csrftoken,
                
            },
            type : 'DELETE',
            contentType: "application/json",
            url :  `/api/cart/${Cartid}`,
            data : Cartid,
            success : function(response){
                console.log('SUCCESS')
            },
            error : function(response){
                console.log(response)
            }
                    });
            }); 
            }
    
    
    }
    }

}};

postfunction();

