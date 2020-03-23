function validate(e){
 
    if (e){
        document.getElementsByClassName('drop-down')[0].hidden = true; 
        document.getElementsByTagName('option')[0].value = e.id;
        document.getElementsByTagName('option')[0].innerHTML = e.innerHTML;
    }

        textbox    = document.getElementById('inputbox');
        select_box = document.getElementById('selection-box');
        button_obj = document.getElementById('button');
        
        if (textbox.value != '' & select_box.value != 0){
            button_obj.disabled = false;
            button_obj.style.cursor = 'pointer';
        }
        else{
            button_obj.disabled = true;
            button_obj.style.cursor = 'not-allowed';
    
        }    
}

function setDropDown(e){
    if (e.id == 'selection-box'){
        document.getElementsByClassName('drop-down')[0].removeAttribute('hidden');
    }

    else{
        document.getElementsByClassName('drop-down')[0].hidden = true;
    }
  
}