function startExam(){
    time_span     = document.getElementById('time-left');
    mydiv         = document.getElementById('mydiv');
    if (mydiv != null){
        time_per_ques = document.getElementById('time').value;
        total_time = time_per_ques * 60;// convert minute into seconds.
        t   = total_time;
        setInterval(() => {
            if(t == 0){
                t = total_time;
                document.getElementById('time').value = t;
                document.getElementById('submit_btn').form.submit();
            }
            t -= 1;
            time_span.innerHTML = t;
            
        }, 1000);
    }
}
function submitAnswer(e){
    e.setAttribute('name','user_ans')
    document.getElementById('submit_btn').disabled = false;
    document.getElementById('time').value = total_time-time_span.innerHTML;
    
}
   
