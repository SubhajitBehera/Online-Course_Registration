 function student_registration()
            {
                var cn = document.getElementById("one").value;
                var param = 'cname='+cn;
                var request = new XMLHttpRequest();
                request.onreadystatechange = checkCname;
                request.open("POST","http://127.0.0.1:8000/checkOne/",true);
                request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                request.send(param);

                function checkCname()
                {
                    if(request.readyState == 4)
                    {
                        var val=request.responseText;
                        var json_data=JSON.parse(val); //converting string to json type
                        var sp=document.getElementById("one1");

                        if (json_data.error == "Name is Taken")
                        {
                            sp.style.color="red";
                            sp.innerText = json_data.error;
                            document.getElementById("b1").disabled = true;

                        }
                        else
                        {
                            sp.style.color="blue";
                            sp.innerText = json_data.message;
                            document.getElementById("b1").disabled = false;

                        }
                    }
                }
            }
 function contact()
            {
                var cno = document.getElementById("two").value;
                var param = "cno="+cno;
                var request=new XMLHttpRequest();
                request.onreadystatechange = checkCno;
                request.open("POST","http://127.0.0.1:8000/checkCno/",true);
                request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                request.send(param);
                function checkCno()
                {
                    if (request.readyState ==4)
                    {
                        var val=request.responseText;
                        var json_data=JSON.parse(val);
                        var sp=document.getElementById("two2");

                        if (json_data.error == "Contact No is Taken")
                        {
                            sp.style.color="red";
                            sp.innerText = json_data.error;
                            document.getElementById("b1").disabled = true;

                        }
                        else
                            {
                                sp.style.color="green";
                                sp.innerText = json_data.message;
                                document.getElementById("b1").disabled = false;

                            }


                    }

                }


            }