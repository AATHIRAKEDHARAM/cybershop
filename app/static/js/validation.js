function validate(){
    let txt_email=document.getElementById('exampleInputEmail1')
    let txt_pass=document.getElementById('exampleInputPassword1')
    let email_pattern=/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    let status =1
    
    if (txt_email.value==''){
        document.getElementById('email_err').innerHTML="*Please enter your email"
        document.getElementById('email_err').style.color="red"
        document.getElementById('exampleInputEmail1').style.borderColor="red"
        status =1
    }
    else if(txt_email.value.match(email_pattern)==null){
        document.getElementById('email_err').innerHTML="*Enter a valid email"
        document.getElementById('email_err').style.color="red"
        document.getElementById('exampleInputEmail1').style.borderColor="red"
        status = 1
    }
    else{
        document.getElementById('email_err').innerHTML=""
        document.getElementById('exampleInputEmail1').style.borderColor=""
        status = 0
    }
    if(txt_pass.value==""){
        document.getElementById('pass_err').innerHTML="*please enter your password"
        document.getElementById('pass_err').style.color="red"
        document.getElementById('exampleInputPassword1').style.borderColor="red" 
        status =1
    }
    else{
        document.getElementById('pass_err').innerHTML=""
        document.getElementById('exampleInputPassword1').style.borderColor=""
        status =0
    }
    if(status==1){
        return false
    }
   

}