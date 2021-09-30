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
        categories: ['1주', '2주', '3주', '이번주', '다음1주', '다음2주']
    },

    tooltip: {
        valueSuffix: '%'
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

    series: [
        {
            name: 'NVDA',
            data: [34.8, 43.0, 51.2, 41.4, 64.9, 72.4],
            color: colors[2],
            accessibility: {
                description: 'This is the most used screen reader in 2019'
            }
        }, {
            name: 'JAWS',
            data: [69.6, 63.7, 63.9, 43.7, 66.0, 61.7],
            dashStyle: 'ShortDashDot',
            color: colors[0]
        }, {
            name: 'VoiceOver',
            data: [20.2, 30.7, 36.8, 30.9, 39.6, 47.1],
            dashStyle: 'ShortDot',
            color: colors[1]
        }, {
            name: 'Narrator',
            data: [null, null, null, null, 21.4, 30.3],
            dashStyle: 'Dash',
            color: colors[9]
        }, {
            name: 'ZoomText/Fusion',
            data: [6.1, 6.8, 5.3, 27.5, 6.0, 5.5],
            dashStyle: 'ShortDot',
            color: colors[5]
        }, {
            name: 'Other',
            data: [42.6, 51.5, 54.2, 45.8, 20.2, 15.4],
            dashStyle: 'ShortDash',
            color: colors[3]
        }
    ],

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

/* 하이차트2 레시피 추천 */
const chart = Highcharts.chart('hi-container2', {
    title: {
        text: '추천레시피 단어'
    },
    subtitle: {
        text: '긍정 단어빈도수 조사'
    },
    xAxis: {
        categories: ['가', '나', '다','라', '마' ,'바' ,'사', '아', '자', '차', '카','타']
    },
    series: [{
        type: 'column',
        colorByPoint: true,
        data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
        showInLegend: false
    }]
});

document.getElementById('plain').addEventListener('click', () => {
    chart.update({
        chart: {
            inverted: false,
            polar: false
        },
        subtitle: {
            text: '기본'
        }
    });
});

document.getElementById('polar').addEventListener('click', () => {
    chart.update({
        chart: {
            inverted: false,
            polar: true
        },
        subtitle: {
            text: '파이차트'
        }
    });
});


/* 다음주 등락률 테이블 솔트 */
new Tablesort(document.getElementById('my-table'));
new Tablesort(document.getElementById('my-table2'));


