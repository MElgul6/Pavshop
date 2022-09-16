const bir= document.getElementById("cox pis");
// console.log(typeof(parseInt(bir.dataset.rate)))
const iki= document.getElementById("pis");
const uc= document.getElementById("pis deyil");
const dord= document.getElementById("yaxsi");
const bes= document.getElementById("ela");
const rating= document.getElementsByName("rating");

const arr=[bir,iki,uc,dord,bes]

const handleSelect=(selection)=>{
    switch(selection){
        case 'cox pis':{
            bir.classList.add('checked');
            iki.classList.remove('checked');
            uc.classList.remove('checked');
            dord.classList.remove('checked');
            bes.classList.remove('checked');
            return
        };
        case 'pis':{
            bir.classList.add('checked');
            iki.classList.add('checked');
            uc.classList.remove('checked');
            dord.classList.remove('checked');
            bes.classList.remove('checked');
            return
        };
        case 'pis deyil':{
            bir.classList.add('checked');
            iki.classList.add('checked');
            uc.classList.add('checked');
            dord.classList.remove('checked');
            bes.classList.remove('checked');
            return
        };
        case 'yaxsi':{
            bir.classList.add('checked');
            iki.classList.add('checked');
            uc.classList.add('checked');
            dord.classList.add('checked');
            bes.classList.remove('checked');
            return
        };
        case 'ela':{
            bir.classList.add('checked');
            iki.classList.add('checked');
            uc.classList.add('checked');
            dord.classList.add('checked');  
            bes.classList.add('checked');
            return
        };
    }
}


arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
    handleSelect(event.target.id)
}))

arr.forEach(item=> item.addEventListener('click', (event)=>{
    rating.forEach(r=> {
        r.value=parseInt(item.dataset.rate);
        console.log(r.value)
    });
}))