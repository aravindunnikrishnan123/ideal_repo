function displayForm(){
        document.getElementsByClassName('content')[0].style.display = 'block';
}

function showMessage(){
        element = document.getElementById('msg');
        if (element.innerHTML.length > 0){
                element.hidden = false;
                setTimeout(function(){
                     element.hidden = true;   
                },3000);
        }
}