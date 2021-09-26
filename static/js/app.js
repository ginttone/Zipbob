$(document).foundation();


// Enable Scroll Reveal
var $scrollReveal = $('.scroll-reveal');

window.sr = ScrollReveal({
  distance: 0,
  scale: 1,
  duration: 1000,
  easing: 'cubic-bezier(0.77, 0, 0.175, 1)',
  mobile: true
});

sr.reveal('.scroll-reveal');

$.each($scrollReveal, function() {
  sr.reveal(this, $(this).data());
});



// Enable Smooth Scrolling ...  by Chris Coyier of CSS-Tricks.com
	$('a[href*="#"]:not([href="#"]):not([href="#show"]):not([href="#hide"]):not([href^="#panel"])').click(function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
			if (target.length) {
				$('html,body').animate({
					scrollTop: target.offset().top
				}, 1000);
				return false;
			}
		}
	});


// Back to top
jQuery(document).ready(function($){
	// browser window scroll (in pixels) after which the "back to top" link is shown
	var offset = 300,
		//browser window scroll (in pixels) after which the "back to top" link opacity is reduced
		offset_opacity = 1200,
		//duration of the top scrolling animation (in ms)
		scroll_top_duration = 700,
		//grab the "back to top" link
		$back_to_top = $('.cd-top');

	//hide or show the "back to top" link
	$(window).scroll(function(){
		( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
		if( $(this).scrollTop() > offset_opacity ) { 
			$back_to_top.addClass('cd-fade-out');
		}
	});

	//smooth scroll to top
	$back_to_top.on('click', function(event){
		event.preventDefault();
		$('body,html').animate({
			scrollTop: 0 ,
		 	}, scroll_top_duration
		);
	});

});

// accodian jquery
// $('.next-week-list').accordion();
    $('.next-week-list-title').click(function(){
        $(this).next().slideToggle().siblings('.next-week-list-table').slideUp();
     });



/* javascript accodian
        //아코디언
        var btnCollapse = document.getElementById('btn-collapse'),
            heading = document.getElementsByClassName('panel-heading'),
            question= document.getElementsByClassName('panel-question'),
            answer = document.getElementsByClassName('panel-body');

        // 제목 클릭시 할일
        for(var i = 0; i < heading.length; i++){
          heading[i].addEventListener('click',function(tt){
            for(var j = 0; j<question.length; j++){
              question[j].classList.remove('active');
              tt.target.parentNode.classList.add('active');
              activateBody();
            } //question 마다 할일
          });
        }

        function activateBody(){
          // 1.페널의 바디 answer가 모두 안보이도록하기
          for(var x=0; x<answer; x++){
            answer[x].style.display = 'none';
          }
          // 2.클래스active 부모페널 자식중 panel-body가 보이도록
          var activePanel = document.querySelector('.panel-question.active .panel-body');
          activePanel.style.display="block";
        }
        activateBody();

        btnCollapse.addEventListener('click', function(){
          for(var i =0; i < answer.length; i++){
            answer[i].style.display='none';
        }});
*/

// highchart js
        var colors = Highcharts.getOptions().colors;

        Highcharts.chart('container-chart', {
            chart: {
                type: 'spline'
            },

            legend: {
                symbolWidth: 40
            },

            title: {
                text: '농수산물 물가 시세 추이'
            },

            subtitle: {
                text: 'Source: WebAIM. Click on points to visit official screen reader website'
            },

            yAxis: {
                title: {
                    text: '세로축'
                },
                accessibility: {
                    description: 'Percentage usage'
                }
            },

            xAxis: {
                title: {
                    text: '가로 축'
                },
                accessibility: {
                    description: '몇일부터 몇일 사이 '
                },
                categories: ['1주', '2주', '3주', '4주', '오늘', '내일']
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
                        description: '설명'
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

// highchart js2

const chart = Highcharts.chart('container-chart2', {
    title: {
        text: '제목'
    },
    subtitle: {
        text: '설명'
    },
    xAxis: {
        categories: ['가', '나', '다', '라', '마', '바', '사', '아', '자', '차', '카', '타']
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
            text: 'Plain'
        }
    });
});

document.getElementById('inverted').addEventListener('click', () => {
    chart.update({
        chart: {
            inverted: true,
            polar: false
        },
        subtitle: {
            text: 'Inverted'
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
            text: 'Polar'
        }
    });
});
