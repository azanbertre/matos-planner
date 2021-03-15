<template>
  <div>
    <VueSlickCarousel v-bind="settings" @beforeChange="testEvent">
      <div
        class="circle-element d-flex justify-center align-center"
        v-for="el in elements"
        :key="el"
      >
        {{ el }}
      </div>
    </VueSlickCarousel>
  </div>
</template>

<script>
  import VueSlickCarousel from "vue-slick-carousel";
  import "vue-slick-carousel/dist/vue-slick-carousel.css";
  // optional style for arrows & dots
  import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

  export default {
    name: "CircleCarousel",
    props: ["elements"],
    components: { VueSlickCarousel },
    data() {
      return {
        settings: {
          centerMode: true,
          centerPadding: "20px",
          focusOnSelect: true,
          infinite: true,
          swipeToSlide: true,
          slidesToShow: 5,
          waitForAnimate: true,
          speed: 700,
        },
      };
    },
    methods:{
      testEvent(e){
        console.log(e)
      }
    }
  };
</script>

<style>
  .circle-element {
    width: 200px !important;
    height: 200px;
    background: rgb(255, 255, 255);
    font-size: 50pt;
    border-radius: 150px;
    box-shadow: 0px 5px 30px -6px #2e75df4b;
    margin: 30px auto;
    outline: none;
    font-weight: bold;
    color: rgb(35, 48, 66);
    border: 5px solid rgb(255, 255, 255);
  }
  /* .slick-current{
    transform: scale(1.5);
    margin: 50px auto;
    display: flex;
    justify-content: center;
  }
  .slick-center{
    display: flex !important;
    align-items: center;
  } */
</style>
