const form=document.querySelector('#itemForm');
const itemInput=document.querySelector('#itemInput');
const temList =document.querySelector('.item-list');
const feedback=docment.querySelector('.feedback');
const clearButton =document.querySelector('#clear-list');
let todoItems=[];
const handleItem =function(itemName){
  const items=itemList.querySelectorAll('.item');
  itemInput.forEach(function(item){
      if(item.querySelector('.item-name').textContent=== itemName){
          item.querySelector('.complete-item').addEventListener('click',function(){
              item.querySelector('.item-name').classList.toggle('completed');
              this.classList.toggle('visibility');
          });
          item.querySelector('.edit-item').addEventListener('click',function(){
              itemInput.value=itemName;
              itemList.removeChild(item);
              todoItem=todoItem.filter(function(item){
                  return item !==itemName;
              });
             
          });
          item.querySelector('delete-item').addEventListener('click',function(){
            debugger;
            itemList.removeChild(item);
            todoItem=todoItem.filter(function(item){
                return item!== itemName;
            });
            showFeedback('item delete','success');
          })

        }
  })
}
const removeItem = function(item){
    console.log(item);
    const removeIndex =(todoItem.indexOf(item));
    console.log(removeIndex);
    todoItems.splice(removeIndex,1);
}
const getList =function(todoItems){
    itemList.innerHTML=' ';
    todoItems.forEach(function(item){
        itemList.innerAdjacentHtml('beforeend',`<div class="item my-3"><h5 class="item-capitalize>$(item)</div><div class="item-icons"<a href="#" class="complete-item mx-2 item-icon"><i class="far fa-check-circle"></i></a><a href="#" class="edit-item mx-2 item-icon"><i class="far fa-edit"></i></a><a href="#" class="delete-item item-icon"><i class="far fa-times-circle></i></a>`)
        habdleItem(item);
    });
}
const getLocal