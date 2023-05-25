<template>
  <div class="universe mw-50" ref="app">
    <router-view></router-view>
    <!-- 촬영장소 modal -->
    <div class="modal fade" id="location" tabindex="-1" aria-labelledby="location-label" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="location-label"><strong>촬영 장소</strong></h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p v-for="location in movie.location_details" :key="location.id">{{location.place}}</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
          </div>
        </div>
      </div>
    </div>
    <!-- review modal -->
    <div class="modal fade" id="review-create-modal" tabindex="-1" aria-labelledby="create-label" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="create-label">리뷰 작성하기</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-start">
            <form>
              <p>별점</p>
              <div class="mb-3" id="review-create">
                <fieldset>
                  <input @click="selectScore" type="radio" name="rating" :value="5" id="create-rate1"><label for="rate1">⭐</label>
                  <input @click="selectScore" type="radio" name="rating" :value="4" id="create-rate2"><label for="rate2">⭐</label>
                  <input @click="selectScore" type="radio" name="rating" :value="3" id="create-rate3"><label for="rate3">⭐</label>
                  <input @click="selectScore" type="radio" name="rating" :value="2" id="create-rate4"><label for="rate4">⭐</label>
                  <input @click="selectScore" type="radio" name="rating" :value="1" id="create-rate5"><label for="rate5">⭐</label>
                </fieldset>
              </div>
              <div class="mb-3">
                <label for="message-text" class="col-form-label">내용</label>
                <textarea v-model="content" class="form-control" id="review-create-text"></textarea>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button @click="createReview" type="button" class="btn btn-primary">작성하기</button>
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
          </div>
        </div>
      </div>
    </div>
    <!-- review update -->
    <div class="modal fade" id="review-update-modal" tabindex="-1" aria-labelledby="update-label" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="update-label">리뷰 수정하기</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-start">
            <form>
              <p>별점</p>
              <div class="mb-3" id="review-update">
                <fieldset>
                  <input @click="selectScore" type="radio" name="rating" :value="5" id="update-rate1"><label for="rate1">⭐</label>
                  <input @click="selectScore" type="radio" name="rating" :value="4" id="update-rate2"><label for="rate2">⭐</label>
                  <input @click="selectScore" type="radio" name="rating" :value="3" id="update-rate3"><label for="rate3">⭐</label>
                  <input @click="selectScore" type="radio" name="rating" :value="2" id="update-rate4"><label for="rate4">⭐</label>
                  <input @click="selectScore" type="radio" name="rating" :value="1" id="update-rate5"><label for="rate5">⭐</label>
                </fieldset>
              </div>
              <div class="mb-3">
                <label for="message-text" class="col-form-label">내용</label>
                <textarea v-model="content" class="form-control" id="review-update-text"></textarea>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button @click="createReview" type="button" class="btn btn-primary">수정하기</button>
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data(){
    return {
      state: '',
      city: '',
      value: 0,
      content: '',
    }
  },
  methods: {
    logout(){
      this.$store.dispatch('logout')
    },
    selectScore(event){
      this.value = event.target.value
    },
    createReview(){
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${this.$store.state.movie_pk}/comments/`,
        data: {
          content: this.content,
          rate: this.value,
        },
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      }).then(res => {
        this.value = 0
        this.content = ''
        console.log(res)
      }).then(() => {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_pk}/commentlist/`
        }).then(res => {
          this.$store.commit('getMovieReviews', res.data)
          console.log(res.data)
        })
      }).catch(err => {
        console.log(err)
      })
    },
  },
  computed:{
    movie(){
      return this.$store.state.movie
    }
  },
}
</script>


<style>
.universe{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url(@/assets/uni.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  height: 100vh;
  width: 100vw;
  overflow: auto;
}
#review-create fieldset{
    display: inline-block; /* 하위 별점 이미지들이 있는 영역만 자리를 차지함.*/
    direction: rtl; /* 이모지 순서 반전 */
    border: 0; /* 필드셋 테두리 제거 */
}
#review-create fieldset legend{
    text-align: left;
}
#review-create input[type=radio]{
    display: none; /* 라디오박스 감춤 */
}
#review-create label{
    font-size: 1em; /* 이모지 크기 */
    color: transparent; /* 기존 이모지 컬러 제거 */
    text-shadow: 0 0 0 #f0f0f0; /* 새 이모지 색상 부여 */
}
#review-create label:hover{
    text-shadow: 0 0 0 rgb(232, 247, 31); /* 마우스 호버 */
}
#review-create label:hover ~ label{
    text-shadow: 0 0 0 rgb(232, 247, 31); /* 마우스 호버 뒤에오는 이모지들 */
}
#review-create input[type=radio]:checked ~ label{
    text-shadow: 0 0 0 rgb(232, 247, 31); /* 마우스 클릭 체크 */
}

#review-create-text{
  height: 200px;
}


#review-update-text{
  height: 200px;
}


#review-update fieldset{
    display: inline-block; /* 하위 별점 이미지들이 있는 영역만 자리를 차지함.*/
    direction: rtl; /* 이모지 순서 반전 */
    border: 0; /* 필드셋 테두리 제거 */
}
#review-update fieldset legend{
    text-align: left;
}
#review-update input[type=radio]{
    display: none; /* 라디오박스 감춤 */
}
#review-update label{
    font-size: 1em; /* 이모지 크기 */
    color: transparent; /* 기존 이모지 컬러 제거 */
    text-shadow: 0 0 0 #f0f0f0; /* 새 이모지 색상 부여 */
}
#review-update label:hover{
    text-shadow: 0 0 0 rgb(232, 247, 31); /* 마우스 호버 */
}
#review-update label:hover ~ label{
    text-shadow: 0 0 0 rgb(232, 247, 31); /* 마우스 호버 뒤에오는 이모지들 */
}
#review-update input[type=radio]:checked ~ label{
    text-shadow: 0 0 0 rgb(232, 247, 31); /* 마우스 클릭 체크 */
}
</style>
