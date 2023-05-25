<template>
  <div class="container">
    <div class="row">
      <div class="MultiCarousel" data-items="3, 3, 3, 3" data-slide="2" id="MultiCarousel"  data-interval="1000">
        <div class="MultiCarousel-inner">
          <div v-for="review in reviews" :key="review.id" class="item single-review">
            <div class="pad15">
              <div>
                <b class="lead">{{review.user}}</b>
                <span>별점 : {{review.rate}}</span>
                <div v-if="review.user===username">
                  <div class="review-height">
                    <button type="button" class="btn btn-primary btn-small" data-bs-toggle="modal" data-bs-target="#review-update-modal">수정</button>
                    <button type="button" class="btn btn-danger btn-small">삭제</button>
                  </div>
                </div>
                <div v-else>
                  <div class="review-height"></div>
                </div>
              </div>
              <hr>
              <p>{{review.content}}</p>
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
.MultiCarousel { float: left; overflow: hidden; padding: 15px; width: 100%; position:relative; }
.MultiCarousel .MultiCarousel-inner { transition: 0.1s ease all; float: left; }
.MultiCarousel .MultiCarousel-inner .item { float: left;}
.MultiCarousel .MultiCarousel-inner .item > div { text-align: center; height: 300px; padding:3px; margin:3px; background:#f1f1f1; color:#666;}
.MultiCarousel .leftLst, .MultiCarousel .rightLst { position:absolute; border-radius:50%;top:calc(50% - 20px); }
.MultiCarousel .leftLst { left:0; }
.MultiCarousel .rightLst { right:0; }
.MultiCarousel .leftLst.over, .MultiCarousel .rightLst.over { pointer-events: none; background:#ccc; }
.review-height{
  height: 20px;
}
.single-review{
  width: 150px;
}
.btn-small{
  height: 20px;
  width: 50px;
  font-size: 50%;
  text-align: center;
}
</style>