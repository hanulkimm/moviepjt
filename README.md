# 핫태하태 프로젝트

## 주제

영화 촬영 장소를 기반으로 영화를 추천해주는 서비스 구현

## 팀원 정보 및 업무 분담 내역



## 목표 서비스 구현 및 실제 구현 정도

- 영화마다 다양한 촬영장소를 가지고 있고 지역마다 다양한 영화를 촬영하였다
- 이러한 정보를 바탕으로 
  - 지역별 촬영이력이 존재하는 영화
  - 영화별 촬영장소
  - 를 알려주는 서비스
- 목표한 서비스는 전부 구현하였다

## 데이터베이스 모델링(ERD)

## 서비스 대표 기능에 대한 설명(영화 추천의 기술적 설명)
- 입장페이지
  - 로그인이력이 있을 경우 메인페이지로 이동
  - 없을 경우 로그인 페이지로 이동
  - 로그인, 회원가입 이후 자동으로 메인페이지로 이동
- 메인페이지
  - 대한민국의 지도를 클릭하여 세부 도시을 선택하는 페이지로 이동
  - 지도에 마우스를 올릴 시 올린 행정구역 하이라이팅, 검색 페이지에 자동 입력
- 도시 선택 페이지
  - 선택한 행정구역의 지도를 클릭하여 행정구역-도시 에서 촬영한 이력이 있는 영화 리스트업
  - 도시를 선택하지 않고 검색 시 해당 행정구역에서 촬영한 이력이 있는 모든 영화 리스트업
- 영화 세부 페이지
  - 세부 페이지 진입 시 티저영상 자동 재생
  - 포스터 및 기본정보 스크롤에 따라 자동 이동
- 프로필 페이지
  - 원하는 이미지를 등록하여 프로필 이미지 설정 가능
  - 리뷰에 나타나는 nickname, 비밀번호 재설정 가능

## 후기

윤태영
- front의 경우 참고하고자하는 대부분의 기능들이 jquery를 이용해 DOM을 조정하도록 되어있어 jquery에 대한 추가적이 학습이 불가피하였다.
  - 좀 더 디테일한 학습이 필요하다
- component와 router-view를 나누어서 구성을 할때 css의 경우 다른 component나 view에 존재하는 스타일이 적용되는 것을 확인할 수 있었다.
  - 이후에 진행하는 프로젝트에서는 class의 이름은 디테일하게 작성하여 체계적으로 관리할 필요가 있어 보인다.
- 태그에 삼항연산자를 이용해 조건을 부여하는 기능이 매우 효율적이었다.
  - 관련한 정확한 작동 방식을 학습할 필요가 있다.
- js는 타입에 대한 설정을 하지 않아 받은 데이터를 편집할 일이 있을 경우 error메시지를 많이 맞닥뜨렸다.
  - ts에 대한 학습이 필요하다