# skincare_recommend - 사용자 맞춤 스킨케어 추천 서비스


## ** 프로젝트 개요**
사용중인 제품의 전성분표를 찍어 업로드하면 OCR(사진으로부터 텍스트 인식)을 이용하여 전성분을 분석,
각 성분을 사용자의 피부타입과 피부고민 및 선호도를 기준으로 적합/부적합을 판단하는 웹 서비스.
피부타입과 성분이 맞지 않을 경우 추가로 새로운 제품을 추천하는 기능

진행 기간 : 2023년 3월 7일 → 2023년 4월 22일

팀원 구성 (총 4인) : 주제 선정 및 기획 1명, 데이터 수집 및 전처리 2명, AI 모델 개발 4명, 서버 구축 3명, 앱 개발 2명, 발표 자료 준비 및 발표 1명


## ** 사용 기술 및 도구 ** 
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&logo=GoogleColab&logoColor=white"/> 


## ** 구현 상세 **

<img width="500" alt="image" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/38598215-6f9a-47cd-a5c5-82354d358343">
<img width="500" alt="image" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/68e07c3f-4230-4355-aac3-acb1e8e65e08">
<img width="500" alt="image" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/d552a600-a799-4758-a89c-ea60508f0bcf">
<img width="500" alt="image" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/112bc7f8-74d7-4cdb-8af0-fd727f78e0cc">

전성분 단어나 글씨 크기, 또 화장품 패키징에 적혀있다는 특성 상 필연적으로 오탈자가 발생하게 되었고, 이를 해결하기 위해 편집거리 유사도 알고리즘 적용
전성분 데이터를 이용해 어떤 단어와 가장 유사한 지를 판단해 변경하는 식으로 오탈자 해결

<img width="500" alt="image" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/1ac96d15-2c71-4a42-9cb1-07992509d967">
<img width="500" alt="image" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/ecacaa0b-d0c3-420b-ad20-2ff85b7008de">
추천 제품 데이터는 올리브영 홈페이지의 스킨/케어 카테고리를 웹 크롤링하여 구축
제품의 적절/부적절 판단과 추천제품 선정은 사용자의 피부타입과 피부고민에 맞는/맞지않는 성분을 찾아 제품의 전성분과 코사인 유사도를 계산하여 사용

<br/><br/>

## ** 구현 화면 **
<br/>
<img width="500" alt="1" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/a2419035-fec0-44ce-b7e5-ff0af11ccd98">
<img width="500" alt="2" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/104f37af-1473-42e6-ad77-5b1664ceab21">
<img width="500" alt="3" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/06209559-3411-4161-9dee-8fdca9ccafb7">
<img width="500" alt="4" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/14c79b69-7944-4155-a40f-33e0aee74040">
<img width="500" alt="5" src="https://github.com/yuyoni/SkincareRecommend/assets/127701092/56560d4b-ce9a-454f-82c4-4cdc81e3a774">

