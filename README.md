`<Final project>`
#  Zipbob ![leaf](https://user-images.githubusercontent.com/83646543/136412844-10c6f8f2-0bcd-4034-aac7-139ebdf523e5.png)

## 농수산물 가격예측을 통한 레시피 추천 서비스


### :chart_with_upwards_trend: Project BASE 

```
코로나 19로 외식문화에서 집 밥 문화로 전향되고 있음을 인식하고, 
농수산물 유통 정보를 알려주어 개인들에게 현명한  소비를 독려하고자 하였다. 
바쁜 사회인들에게 농수산물 유통 정보와 함께 추천 레시피를 알려줌으로써 
따로 ‘어떤 요리를 할지’에 대한 불필요한 고민을 덜어준다.
```

### :computer: Work-processing

![processe](https://user-images.githubusercontent.com/83646543/136413012-2f56ce86-8ff4-40dc-8394-a17ac3bb42c8.jpg)

### :+1: Work

1. 데이터 수집

   ```
   aT KAMIS Api  : 농산물 물가 예측을 위한 데이터 수집
   Youtube Api : 추천레시피 및 댓글 분석을 위한 데이터 수집
   만개의 레시피 scraping :추천레시피 및 댓글 분석을 위한 데이터 수집
   Google image Scraping : 농수산물 이미지 수집
   ```

2. 데이터 분석

   ```
   농수산물 가격 데이터 EDA 전처리
   Time Series(시계열) : 다음주 농수산물 가격 예측
   Text mining(텍스트마이닝) : 레시피 추천(댓글 감성 분석)
   ```

   

3. ERD 구현

   ```
   KAMIS : 농수산물 품목/분류/상세, 가격(1995년~현재), 다음주가격
   Youtube : 유투브 채널 , 타이틀, 재료, 조리법, 댓글
   만개의 레시피 : 타이틀, 재료, 조리법, 댓글
   User : 사용자 정보 
   Image : 농수산물 품목별 이미지 
   ```

   

4. Web 구현

   ```
   Frame 설계 : html 뼈대 만들기
   Ui Design 정의 : Color, Font , Size 등 정의 및 구현
   Bootstrap 사용 없이 구현 
   ```

   

5. Chatbot 구현 

   ```
   사용자가 입력한 단어를 실시간으로 자연어 처리 하여 , 집밥 사용목적에 부합하는 시나리오와 매칭. 
   플랫폼에서 제공하는 정보와 추가로 사용자가 원하는 기타 정보를 챗봇응답기가 실시간으로 사용자에게 대답하는 형태로 구현.
   ```
   

6. 추진일정

   ```
   8/20  Final project 조 구성
   8/31  Brainstorming (주제 선정, 팀 이름 선정, 역할분장 , 협업 툴 공유)
   9/6  기획안 발표
   9/7~9/15 Crawling , Web front
   9/13~  Machine Learning
   9/16~  Web backend
   10/1 프로젝트 1차 마무리
   10/4~ 프로젝트 수정 및 보완
   10/6  PPT 및 포트폴리오 제작
   10/8 최종 프로젝트 발표/종강
   ```

[![SC2 Video](https://img.youtube.com/vi/ia2V0xFWCGY/0.jpg)](https://www.youtube.com/watch?v=ia2V0xFWCGY)

### :mortar_board: Educated

*  [Multicampus](https://www.multicampus.com) 빅데이터 기반 지능형 서비스 개발 수료(10/8 종강)

-----------------
###  :running: Member 

**About [JuHee Kim](alicelikesbab@gmail.com)** [PM & Frontend]

**Used skills in The final project.**

* Python , SQLite3

* Frontend :   Html5 ,  CSS ,  Javascript ,  Jquery  ,  Ajax , Django 

*  :link:  [Github](https://github.com/ginttone) , Google Doc

-------

**About [ Jihyun_Kim](hyunii605@google.com)** [Frontend]

**Used skills in The final project.**

* Python , SQLite3
* Frontend :   Html5 , CSS ,  Javascript ,  Jquery , Ajax , Django 
*  :link:  [Github]( https://github.com/fonslucens) , Google Doc

---------

**About [Jaehyeon_Song](wogus0523@gmail.com)** [Machine Learning]

**Used skills in The final project.**

* Python , SQLite3
* Machine Learning :  Pandas 1.1.5 ,  Konlpy 0.5.2 , Numpy 1.19.5 , nltk 3.6.4 ,  Okt , seaborn 0.11.1 ,  sklearn ,  Tensorflow 2.6 ,   Matplotlib 3.3.4 , Worldcloud
*  :link:  [Github](https://github.com/Songgplant ) , Google Doc

---------

**About [ Daseul_Jeong](jds88guy@gmail.com)** [Backend & Crawling]

**Used skills in The final project.**

* Python , SQLite3
* Backend :   Django 3.2.7 , Ajax 
* Crawling : selenium 3.141.0 , BeautifulSoup 3.4.3 , time , schedule , pandas 1.1.5
*  :link:  [Github]( https://github.com/Ethan-Jeong) , Google Doc

---------

**About [Hyunsoo_Choi]( hakdjhakdj@gmail.com)** [Machine Learning]

**Used skills in The final project.**

* Python , SQLite3
* Machine Learning :  Pandas 1.1.5 ,  Konlpy 0.5.2 , Numpy 1.19.5 , nltk 3.6.4 ,  Okt , seaborn 0.11.1 ,  sklearn ,  Tensorflow 2.6 , Matplotlib 3.3.4 , Worldcloud
*  :link:  [Github]( https://github.com/hakdj) , Google Doc

-----------------
