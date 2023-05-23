<template>
  <div>
    <div>
      review list
    </div>
    <div>
      <form id="myform" @submit.prevent="createReview">
        <input v-model="content" type="text">
        <fieldset>
          <input @click="selectScore" type="radio" name="rating" :value="5" id="rate1"><label for="rate1">⭐</label>
          <input @click="selectScore" type="radio" name="rating" :value="4" id="rate2"><label for="rate2">⭐</label>
          <input @click="selectScore" type="radio" name="rating" :value="3" id="rate3"><label for="rate3">⭐</label>
          <input @click="selectScore" type="radio" name="rating" :value="2" id="rate4"><label for="rate4">⭐</label>
          <input @click="selectScore" type="radio" name="rating" :value="1" id="rate5"><label for="rate5">⭐</label>
        </fieldset>
        <button type="submit">작성</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'reviewList',
  data(){
    return {
      value: 0,
      content: ''
    }
  },
  props:{
    movie_pk: String
  },
  created(){
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_pk}/commentlist/`
    }).then(res => {
      console.log(res)
    })
  },
  methods:{
    createReview(){
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_pk}/comments/`,
        data: {
          content: this.content,
          rate: this.value,
        },
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      }).then(res => {
        console.log(res)
      }).catch(err => {
        console.log(err)
      })
    },
    selectScore(event){
      this.value = event.target.value
    }
  }

}
</script>

<style>
#myform fieldset{
    display: inline-block; /* 하위 별점 이미지들이 있는 영역만 자리를 차지함.*/
    direction: rtl; /* 이모지 순서 반전 */
    border: 0; /* 필드셋 테두리 제거 */
}
#myform fieldset legend{
    text-align: left;
}
#myform input[type=radio]{
    display: none; /* 라디오박스 감춤 */
}
#myform label{
    font-size: 1em; /* 이모지 크기 */
    color: transparent; /* 기존 이모지 컬러 제거 */
    text-shadow: 0 0 0 #f0f0f0; /* 새 이모지 색상 부여 */
}
#myform label:hover{
    text-shadow: 0 0 0 rgb(232, 247, 31); /* 마우스 호버 */
}
#myform label:hover ~ label{
    text-shadow: 0 0 0 rgb(232, 247, 31); /* 마우스 호버 뒤에오는 이모지들 */
}
#myform input[type=radio]:checked ~ label{
    text-shadow: 0 0 0 rgb(232, 247, 31); /* 마우스 클릭 체크 */
}
</style>