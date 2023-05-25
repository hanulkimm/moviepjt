<template>
  <div class="container">
    <div class="row">
      <div class="MultiCarousel" data-items="3, 3, 3, 3" data-slide="2" id="MultiCarousel"  data-interval="1000">
        <div class="MultiCarousel-inner">
          <div v-for="review in reviews" :key="review.id" class="item single-review">
            <div class="pad15">
              <input class="checkbox-ticket" type="radio" name="ticket" id="ticket-1">
              <label for="ticket-1 ticket">
                <span class="top-dots">
                  <span class="section dots">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                  </span>
                </span>
                <div>
                  <span class="duration">
                    {{review.user.nickname}}
                  </span>
                  <span class="duration">
                    별점 : {{review.rate}}
                  </span>
                  <hr class="mt-1 mb-0 black">
                </div>
                <span class="mt-2 pb-4 mb-3 content black">
                  {{review.content}}
                </span>
                <span class="section dots">
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                </span>
                <span class="section pt-2">
                  <i class='uil uil-clock-two mt-3'></i>
                </span>
                <div>
                  <button @click="updateReview" :data-rate="review.rate" :data-review="review.content" type="button" class="btn btn-primary btn-small me-3" data-bs-toggle="modal" data-bs-target="#review-update-modal">수정</button>
                  <button type="button" class="btn btn-danger btn-small">삭제</button>
                </div>
                <span class="bottom-dots">
                  <span class="section dots">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                  </span>
                </span>
              </label>
            </div>
          </div>
        </div>
        <button class="btn btn-primary leftLst">◀</button>
        <button class="btn btn-primary rightLst">▶</button>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'reviewList',
  props:{
    reviews: Array
  },
  computed: {
    username(){
      return localStorage.getItem('username')
    }
  },
  methods:{
    updateReview(event){
      this.$store.commit('selectReview', {review: event.target.dataset.review, rate: event.target.dataset.rate})
    }

  },
  updated(){
    $(document).ready(function () {
      let itemsMainDiv = ('.MultiCarousel');
      let itemsDiv = ('.MultiCarousel-inner');
      let itemWidth = "";
      $('.leftLst, .rightLst').click(function () {
        let condition = $(this).hasClass("leftLst");
        if (condition)
          click(0, this);
        else
          click(1, this)
      });
    
        ResCarouselSize();
    
        $(window).resize(function () {
          ResCarouselSize();
        });
    
        //this function define the size of the items
        function ResCarouselSize() {
          let incno = 0;
          let dataItems = ("data-items");
          let itemClass = ('.item');
          let id = 0;
          let btnParentSb = '';
          let itemsSplit = '';
          let sampwidth = $(itemsMainDiv).width();
          let bodyWidth = $('body').width();
          $(itemsDiv).each(function () {
            id = id + 1;
            let itemNumbers = $(this).find(itemClass).length;
            btnParentSb = $(this).parent().attr(dataItems);
            itemsSplit = btnParentSb.split(',');
            $(this).parent().attr("id", "MultiCarousel" + id);
    
    
            if (bodyWidth >= 1200) {
                incno = itemsSplit[3];
                itemWidth = sampwidth / incno;
            }
            else if (bodyWidth >= 992) {
                incno = itemsSplit[2];
                itemWidth = sampwidth / incno;
            }
            else if (bodyWidth >= 768) {
                incno = itemsSplit[1];
                itemWidth = sampwidth / incno;
            }
            else {
                incno = itemsSplit[0];
                itemWidth = sampwidth / incno;
            }
            $(this).css({ 'transform': 'translateX(0px)', 'width': itemWidth * itemNumbers });
            $(this).find(itemClass).each(function () {
                $(this).outerWidth(itemWidth);
            });
    
            $(".leftLst").addClass("over");
            $(".rightLst").removeClass("over");
    
          });
        }
        //this function used to move the items
        function ResCarousel(e, el, s) {
            let leftBtn = ('.leftLst');
            let rightBtn = ('.rightLst');
            let translateXval = '';
            let divStyle = $(el + ' ' + itemsDiv).css('transform');
            // eslint-disable-next-line
            let values = divStyle.match(/-?[\d\.]+/g);
            let xds = Math.abs(values[4]);
            if (e == 0) {
                translateXval = parseInt(xds) - parseInt(itemWidth * s);
                $(el + ' ' + rightBtn).removeClass("over");
    
                if (translateXval <= itemWidth / 2) {
                    translateXval = 0;
                    $(el + ' ' + leftBtn).addClass("over");
                }
            }
            else if (e == 1) {
                let itemsCondition = $(el).find(itemsDiv).width() - $(el).width();
                translateXval = parseInt(xds) + parseInt(itemWidth * s);
                $(el + ' ' + leftBtn).removeClass("over");
    
                if (translateXval >= itemsCondition - itemWidth / 2) {
                    translateXval = itemsCondition;
                    $(el + ' ' + rightBtn).addClass("over");
                }
            }
            $(el + ' ' + itemsDiv).css('transform', 'translateX(' + -translateXval + 'px)');
        }
    
        //It is used to get some elements from btn
        function click(ell, ee) {
            let Parent = "#" + $(ee).parent().attr("id");
            let slide = $(Parent).attr("data-slide");
            ResCarousel(ell, Parent, slide);
        }
    });
  }
}
</script>

<style>
.MultiCarousel { float: left; overflow: hidden; padding: 0px; width: 100%; position:relative; }
.MultiCarousel .MultiCarousel-inner { transition: 0.1s ease all; float: left; }
.MultiCarousel .MultiCarousel-inner .item { float: left;}
.MultiCarousel .leftLst, .MultiCarousel .rightLst { position:absolute; border-radius:50%;top:calc(50% - 20px); }
.MultiCarousel .leftLst { left:0; }
.MultiCarousel .rightLst { right:0; }
.MultiCarousel .leftLst.over, .MultiCarousel .rightLst.over { pointer-events: none; background:#ccc; }
.review-height{
  height: 20px;
}
.single-review{
  width: 200px;
}
.btn-small{
  height: 30px;
  width: 60px;
  font-size: 50%;
  text-align: center;
}



@import url('https://fonts.googleapis.com/css2?family=Lato:wght@700;900&display=swap');

:root {
	font-size: 20px;
	--dark-blue: black;
	--white-gr: #c4c3ca;
	--yellow: #6ccdeb;
	--yellow-2: #478bc2;
}
.section{
	position: relative;
	width: 100%;
	display: block;
	z-index: 2;
}
[type="radio"]:checked,
[type="radio"]:not(:checked){
	position: absolute;
	left: -9999px;
	width: 0;
	height: 0;
	visibility: hidden;
}
.checkbox-ticket:checked + label,
.checkbox-ticket:not(:checked) + label{
	position: relative;
	width: 184px;
	display: inline-block;
	cursor: pointer;
	padding: 10px 0;
	text-align: center;
	margin: 5px;
	border-radius: 0;
	background-color: transparent;
	overflow: hidden;
	transition: all 250ms linear;
}
.checkbox-ticket:checked + label:before,
.checkbox-ticket:not(:checked) + label:before{
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: -1;
	display: block;
	background-image: linear-gradient(335deg, var(--yellow), var(--yellow-2));
}

.checkbox-ticket + label .duration{
	font-family: 'Lato', sans-serif;
	font-weight: 700;
	font-size: 18px;
	line-height: 1;
	text-transform: uppercase;
	color: var(--dark-blue);
	display: block;
}
.checkbox-ticket + label .price{
	font-family: 'Lato', sans-serif;
	font-weight: 900;
	font-size: 40px;
  height: 300px;
	line-height: 1;
	text-transform: uppercase;
	color: var(--dark-blue);
	display: block;
	transition: all 250ms linear;
	text-shadow: 1px 2px 4px var(--yellow), 0 0 0 #000, 1px 2px 4px var(--yellow);
}
.checkbox-ticket + label .price sup{
	font-size: 26px;
	line-height: 1;
	letter-spacing: 4px;
}

.checkbox-ticket + label .time {
	font-family: 'Lato', sans-serif;
	font-weight: 700;
	font-size: 15px;
	text-transform: uppercase;
	color: var(--dark-blue);
	display: block;
}
.top-dots,
.bottom-dots {
	position: absolute;
	width: 100%;
	display: block;
	top: 0;
	transform: translateY(-50%);
	z-index: 10;
}
.bottom-dots {
	top: 100%;
}

.dots span {
	position: absolute;
	width: 6px;
	height: 6px;
	display: block;
	border-radius: 50%;
	top: 0;
	transform: translateY(-50%);
	background-color: var(--dark-blue);
}
.dots span:nth-child(1){
	width: 30px;
	height: 30px;
	left: -15px;
}
.dots span:nth-child(2){
	width: 30px;
	height: 30px;
	right: -15px;
}
.dots span:nth-child(3){
	left: 19px;
}
.dots span:nth-child(4){
	left: 29px;
}
.dots span:nth-child(5){
	left: 39px;
}
.dots span:nth-child(6){
	left: 49px;
}
.dots span:nth-child(7){
	left: 59px;
}
.dots span:nth-child(8){
	left: 69px;
}
.dots span:nth-child(9){
	left: 79px;
}
.dots span:nth-child(10){
	left: 89px;
}
.dots span:nth-child(11){
	left: 99px;
}
.dots span:nth-child(12){
	left: 109px;
}
.dots span:nth-child(13){
	left: 119px;
}
.dots span:nth-child(14){
	left: 129px;
}
.dots span:nth-child(15){
	left: 139px;
}
.dots span:nth-child(16){
	left: 149px;
}
.dots span:nth-child(17){
	left: 159px;
}
.dots span:nth-child(18){
	left: 169px;
}
.dots span:nth-child(19){
	left: 179px;
}
.ticket{
  padding-top: 0;
  padding-bottom: 0;
}
.black{
  color: black;
}
.content{
  display: inline-block;
  height: 150px;
  font-size: 0.8rem;
}
</style>