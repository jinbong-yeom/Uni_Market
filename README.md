# __유니마켓__
### 서비스 설명
*** 
* 해당 서비스, 중고거래 앱 통합 서비스는 사용 자의 이용용의성을 도모하기 위해 다양한 중고거래 앱을 통합하여 편의기능과 함께 제공하는 안드로이드 기반 앱이다.<br>
<ol>
<li>사용자에게 입력받은 키워드를 이용하여 통합된 중고 매물의 리스트를 제공한다. 이때 일부 중고거래 앱은 사용자의 동네 인증을 필요로 하므로 지역 이름을 키워드와 함께 입력으로 받는다. 지정한 동네와 키워드를 조건으로 하여 데이터베이스에서 알맞은 매물들을 추출하고 매물의 이름, 사진, 가격, 지역, 상세 페이지 정보 등의 매물 정보를 제공한다.</li>
<li>사용자는 필터링 1번의 입력과 제목에서 제외하고 싶은 단어를 필터링 키워드로 하고 가격 범위를 설정하여 알람기능을 제공받을 수 있다. 조건에 맞는 새로운 매물이 등록되면 모니터링에 의해서 알람을 받을 수 있다.</li>
</ol>
 
<br />

## __설치방법__

## __의존성__

### For Server
*** 
* python 3.6.9<br>  
Flask<br>
firebase-admin 6.0.1<br>
pymongo 4.2.0<br>
bs4 0.0.1<br>

* 설치방법
     ```
      pip install -r requirements.txt
    ```

### For App
***
* retrofit2 2.9.0<br>
firebase-messaging 23.1.0<br>
firebase-analytics 21.2.0<br>
android.material 1.6.1<br>
androidx.appcompat 1.5.1<br>
androidx.test.ext 1.1.3<br>
androidx.test.espresso-core 3.4.0<br>
junit 4.13.<br>
com.github.bumptech.glide 4.11.0<br>
JDK version 11.0.13<br>

<br/>

## __실행방법(development)__
### server
***
* crawler<br>
cd crawling<br>
```
python3 crawler.py -t 1 //당근 매물 크롤링
python3 crawler.py -t 2 //번개 매물 크롤링 
python3 crawler.py -t 3 //중고 매물 크롤링 
```
* server<br>
cd server<br>
python3 server.py<br>

## __실행방법(어플)__
***
#### 검색 & 필터링 & 정렬
![1검색](https://user-images.githubusercontent.com/100690081/206858931-a69e25ab-77ec-425b-94e3-7144d233606d.gif)
![2정렬](https://user-images.githubusercontent.com/100690081/206858942-28238fc8-fbfd-4753-a4e9-5d7d2fe753c0.gif)
![3필터링](https://user-images.githubusercontent.com/100690081/206858945-f811f2c6-d5c4-4ad6-beb4-8d151b149d1a.gif)

#### 상세페이지 & 원래 플랫폼으로 이동
![4 상세페이지](https://user-images.githubusercontent.com/100690081/206858947-7669e532-83e1-45c5-a257-be7fa2c2ef51.gif)

#### 알림설정 & 해제
![5알림](https://user-images.githubusercontent.com/100690081/206858969-5cd465d8-1109-415e-8c3c-159bd9a7a41a.gif)


#### 지역설정 & 개발자문의 & 버전확인
![Screenshot_20221210-222043 (1)](https://user-images.githubusercontent.com/100690081/206859142-3cbcd1f6-d0ff-40d5-b1ec-aaceac859d92.jpg)




<br/>

## __라이선스__
```
The MIT License (MIT)

Copyright (c) 2022 uni-market

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
<br />

## __Contributors__

  |염진봉|[jinbong-yeom](https://github.com/jinbong-yeom)| wlftj13@naver.com | 충북대학교 컴퓨터공학과
|:-|:-|:-|:-|
 |**강인우**|**[kiw331](https://github.com/kiw331)**|**mingureion@gmail.com**|**충북대학교 컴퓨터공학과**|
 |**이석범**|**[stoneTiger0912](https://github.com/stoneTiger0912)**|**seokbeom0912@gmail.com**|**충북대학교 컴퓨터공학과**|
