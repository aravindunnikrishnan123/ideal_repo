function startExam(){
    time_span     = document.getElementById('time-left');
    mydiv         = document.getElementById('mydiv');
    time_per_ques = document.getElementById('time').value;

    total_time = time_per_ques * 60;// convert minute into seconds.
    console.log(total_time);
    console.log('time per question: '+time_per_ques);
    //total_time = 6;
    t   = total_time;
    if (mydiv != null){
        setInterval(() => {
            if(t < 0){
                t = 6;
                document.getElementById('submit_btn').form.submit();
            }
            time_span.innerHTML = t;
            t -= 1;
        }, 1000);
    }
}
function submitAnswer(e){
    e.setAttribute('name','user_ans')
    document.getElementById('submit_btn').disabled = false;
    document.getElementById('time').value = total_time-time_span.innerHTML;
    
}
   
