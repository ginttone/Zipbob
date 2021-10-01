//  챗봇 js시작
var coll = document.getElementsByClassName('collapsible_j');

// 챗봇 클릭하면 떠오르게.
for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}

// 챗봇 시작할 때 시간 받아서 출력.
function getTime() {
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();

    if (hours < 10) {
        hours = "0" + hours //e.g. 7시의 경우 07시로 표시
    }

    if (minutes < 10) {
        minutes = "0" + minutes
    }

    let time = hours + ":" + minutes;
    return time;
}

// 시작 메시지
function firstBotMessage(){
    let firstMessage = "안녕하세요! Zipbob입니다."
    document.getElementById("botStarterMessage").innerHTML = "<p class='botText'><span>" + firstMessage + '</span></p>';

    let time = getTime();

    $('#chat-timestamp').append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

function getHardResponse(userText) {
    let botResponse = getBotResponse(userText);
    let botHTML = '<p class="botText"><span>' + botResponse + '</span></p>';
    $ ("#chatbox").append(botHTML);

    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

//응답 얻기
function getResponse() {
    let userText = $("#textInput").val();

    if(userText == "") {
        userText = "오늘도 코딩 열심히!";
    }

    let userHTML = '<p class="userText"><span>' + userText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHTML);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    setTimeout (() => {
        getHardResponse(userText);
    }, 1000)
}

function buttonSendText(sampleText) {
    let userHTML = '<p class="botText"><span>' + sampleText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHTML);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

//비행기 아이콘 누르면 메시지 전달
function sendButton() {
    getResponse();
}

//하트 버튼 누르기
function heartButton() {
    buttonSendText("Heart clicked!")
}

//enter 키 눌러 메시지 보내기
$("#textInput").keypress(function(e) {
    if (e.which == 13) {
        getResponse();
    }
})


function getBotResponse(input) {
    //간단한 응답
    if (input == "안녕") {
        console.log("만나서 반가워요");
        return "만나서 반가워요!";
    } else if (input == "잘 있어") {
        console.log("즐거웠어요. 다음에 만나요!");
        return "즐거웠어요. 다음에 만나요!";
    } else if (input == "모각코") {
        console.log("오늘도 즐겁게 공부해봐요. 파이팅!");
        return "오늘도 즐겁게 공부해봐요. 파이팅!";
    } else if (input == "날씨") {
        console.log("요즘 너무 덥죠?");
        return "요즘 너무 덥죠?";
    } else {
        console.log("잘 이해하지 못했어요. 다른 이야기를 해볼까요?");
        return "잘 이해하지 못했어요. 다른 이야기를 해볼까요?";
    }
}

/* 추천레시피 슬라이드 */
var slideIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > x.length) {slideIndex = 1}
  x[slideIndex-1].style.display = "block";
  setTimeout(carousel, 5000);
}

/* 추천레시피 아코디언 검색*/
  $('.question').click(function(){
            $(this).next().slideToggle();
            $(this).next().siblings('.answer').slideUp();
         });

/* 로그인 form */
    function signupToggle(){
        var containerf = document.querySelector('.containerf');
        containerf.classList.toggle('active');
        var popup = document.querySelector('.signup-form');
        popup.classList.toggle('active');
    }

    function loginToggle(){
        var containerf = document.querySelector('.containerf');
        containerf.classList.toggle('active');
        var popup = document.querySelector('.login-form');
        popup.classList.toggle('active');
    }




/* 다음주 등락률 테이블 솔트 */
new Tablesort(document.getElementById('my-table'));
new Tablesort(document.getElementById('my-table2'));


/* JDS */

$(document).ready(function(){

    $.ajax({
                 url:'next_week_pred',
                 datatype:'JSON',
                 success:function(data){
                        next_week_pred_graph(data)
                 }
    });

});


function emailcheck(){

		var submit_email = document.getElementById('reg_email_75').value;
		var label_email = document.getElementById("email_label");

		let email_str = document.getElementById('reg_email_75').value;

		if (submit_email != '' && email_str.includes("@") & email_str.includes(".com") && submit_email.length >  5 ){

			$.ajax({
					 url:'emailchk',
					 data:{ email:submit_email},
					 datatype:'JSON',
					 success:function(data,color){
						$("p[id='email_label']").text(data.data);
						label_email.style.color = data.color;
					 }
			});
		}else{
			alert("정확한 메일주소를 입력하세요.");
			$("p[id='email_label']").text("");
		}
}


function namecheck(){
    var name = $("#reg_name").val();
    var email = $("#reg_email_75").val();

    if ( email != ""  && ( name.length < 2 || name.length > 10 )){

        if($("#reg_pwd").is(":disabled")){

        }else{
            $("#reg_pwd").attr("disabled");
            $("p[id='name_label']").text("2자리 ~ 10자리 이내로 입력해주세요.");
        }

    }else{
        $("p[id='name_label']").text("");
        if($("#reg_pwd").is(":disabled")){
            $("#reg_pwd").removeAttr("disabled");
        }
    }
}

function pwdcheck(){
    var pw = $("#reg_pwd").val();
    var num = pw.search(/[0-9]/g);
    var eng = pw.search(/[a-z]/ig);
    var spe = pw.search(/[`~!@@#$%^&*|₩₩₩'₩";:₩/?]/gi);

    if ( pw.length > 0 ){
        if(pw.length == 0 || pw.length > 20){
            $("p[id='pwd_label']").text("8자리 ~ 20자리 이내로 입력해주세요.");
            $("#reg_pwd_chk").attr("disabled");

            return false;
         }else if(pw.search(/\s/) != -1){
            $("p[id='pwd_label']").text("비밀번호는 공백 없이 입력해주세요.");
            $("#reg_pwd_chk").attr("disabled");

          return false;
         }else if(num < 0 || eng < 0 || spe < 0 ){
            $("p[id='pwd_label']").text("영문,숫자, 특수문자를 혼합하여 입력해주세요.");
            $("#reg_pwd_chk").attr("disabled");

            return false;
         }else {
            // disabled 여부
            $("p[id='pwd_label']").text("");
            if($("#reg_pwd_chk").is(":disabled")){
                $("#reg_pwd_chk").removeAttr("disabled");
            }
            console.log("통과");
            return true;
         }
    }
}

function dupcheck(){
    var pw = $("#reg_pwd").val();
    var pw_chk = $("#reg_pwd_chk").val();
    var pwd_label = document.getElementById("pwd_chk_label")

    if ( pw_chk.length > 0 ){
        if( pw != pw_chk ){
            $("p[id='pwd_chk_label']").text("일치하지 않습니다. 다시 입력해주세요.");
            pwd_label.style.color = "Red";
            $("#reg_submit").attr("disabled");
        }else{
            $("p[id='pwd_chk_label']").text("일치합니다.");
            pwd_label.style.color = "Green";
            if($("#reg_submit").is(":disabled")){
                $("#reg_submit").removeAttr("disabled");
            }
        }
    }

}

function regi_submit(){

    var submit_email = document.getElementById('reg_email_75').value;
    var submit_name = document.getElementById('reg_name').value;
    var submit_pwd = document.getElementById('reg_pwd').value;
    var submit_pwd_chk = document.getElementById('reg_pwd_chk').value;

    var label_email = document.getElementById("email_label").value;

    if ( label_email == ""){
        alert('메일 중복확인을 해주세요.');
    }else if( submit_name == "" ){
        alert('이름을 입력해주세요.');
    }else if( submit_pwd == "" ){
        alert('비밀번호를 입력해주세요.');
    }else if( submit_pwd == submit_pwd_chk ){
        $.ajax({
             url:'regi_view',
             data:{ email:submit_email , name:submit_name , pwd:submit_pwd },
             datatype:'JSON',
             success:function(data){
                alert(data);
                window.open("{% url 'index' %}","_self");

             }
        });
    }else{
        alert('비밀번호가 일치하지 않습니다.');
    }

}

function login(){
    var login_email = document.getElementById('login_email').value;
    var login_password = document.getElementById("login_password").value;

    if ( login_email != '' && login_password != '' ) {

        $.ajax({
                 url:'login',
                 data:{ email:login_email , pwd:login_password},
                 datatype:'JSON',
                 success:function(data){
                    alert(data.data);
                    window.open("{% url 'index' %}","_self");
                 }
        });
    }else if( login_email == '' ){
        alert('메일을 입력하세요');
    }else if( login_password == '' ){
        alert('비밀번호를 입력하세요');
    }
}

function next_week_pred_graph(data){
    /* 하이차트 다음주가격예측 */
    var colors = Highcharts.getOptions().colors;

    Highcharts.chart('hi_container1', {
        chart: {
            type: 'spline'
        },

        legend: {
            symbolWidth: 40
        },

        title: {
            text: '다음주 예측 그래프'
        },

        subtitle: {
            text: '농수산물의 주단위 가격변동 추이'
        },

        yAxis: {
            title: {
                text: '세로축 금액입니다.'
            },
            accessibility: {
                description: '세로축 금액입니다.내용'
            }
        },

        xAxis: {
            title: {
                text: '가로축 기간입니다.'
            },
            accessibility: {
                description: '가로축 기간입니다.내용'
            },
            categories: data.date
        },

        tooltip: {
            valueSuffix: '원'
        },

        plotOptions: {
            series: {
                point: {
                    events: {
                        click: function () {
                            window.location.href = this.series.options.website;
                        }
                    }
                },
                cursor: 'pointer'
            }
        },

        series: data.data,

        responsive: {
            rules: [{
                condition: {
                    maxWidth: 550
                },
                chartOptions: {
                    chart: {
                        spacingLeft: 3,
                        spacingRight: 3
                    },
                    legend: {
                        itemWidth: 150
                    },
                    xAxis: {
                        categories: ['Dec. 2010', 'May 2012', 'Jan. 2014', 'July 2015', 'Oct. 2017', 'Sep. 2019'],
                        title: ''
                    },
                    yAxis: {
                        visible: false
                    }
                }
            }]
        }
    });
}