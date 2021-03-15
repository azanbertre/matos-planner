<template>
  <div class="shell-hooper" @mouseover="activeArrows = true" @mouseleave="activeArrows = false">
    <hooper :settings="hooperSettings">
      <slide
        v-for="(el, index) in elements"
        :class="[
          'carousel-element d-flex justify-center',
          { 'hooper-slide-active': active_slide == index },
        ]"
        :key="el.id"
      >
        <div
          @click="openCard(index)"
          :class="[
            'shell-slide',
            { 'shell-slide-active': active_slide == index },
          ]"
          :style="'background-image: ' + createGradient(el.title)"
        >
          <div
            :class="[
              'subtopic-title',
              { 'subtopic-title-active': active_slide == index },
            ]"
          >
            {{ el.title }}
          </div>
        </div>
        <div
          :class="[
            'subtopic-text',
            { 'subtopic-text-active': active_slide == index },
          ]"
          @click="openCard(index)"
        >
          {{ el.text }}
        </div>
        <div
          :class="[
            'action-buttons-slide',
            { 'action-buttons-slide-active': active_slide == index },
          ]"
        >
          <v-row>
            <v-col cols="12" class="pa-0 my-1 mb-2 d-flex justify-center">
              <v-btn color="#FFF" small :disabled="active_slide !== index" @click="goToCreateGame(el.title)"
                >criar um jogo</v-btn
              >
            </v-col>
          </v-row>
        </div>
      </slide>
      <template v-if="activeArrows">
        <hooper-navigation slot="hooper-addons"></hooper-navigation>  
      </template>
    </hooper>
  </div>
</template>

<script>
  import gradient from 'random-gradient'
  import { Hooper, Slide, Navigation as HooperNavigation } from "hooper";
  import "hooper/dist/hooper.css";
  import axios from "axios";
  export default {
    props: ["elements"],
    name: "TopicsCarousel",
    components: {
      Hooper,
      Slide,
      HooperNavigation,
    },
    data() {
      return {
        unsplashData: null,
        active_slide: null,
        activeArrows: false,
        hooperSettings: {
          itemsToShow: 2,
          wheelControl: false,
          touchDrag: true,
          mouseDrag: false,
          breakpoints: {
            "540": {
              centerMode: true,
              infiniteScroll: true,
            },
            "1000": {
              itemsToShow: 6,
              pagination: "fraction",
            },
          },
        },
      };
    },
    mounted() {
      console.log(gradient('bruh'))
    },
    methods: {
      getUnsplashPhotos() {
        let local = localStorage.getItem("lastname");
        if (!local) {
          axios
            .get(
              "https://api.unsplash.com/photos/?client_id=2x9AU1ODDN887n4kTvDwIoNY-xlFsBB6yuEBuFU_8EQ?page=1&query=math"
            )
            .then((result) => {
              localStorage.setItem("lastname", JSON.stringify(result.data));
              this.unsplashData = result.data;
            });
        } else {
          this.unsplashData = JSON.parse(local);
        }
      },
      createGradient(title){
        return gradient(title)
      },
      openCard(slide) {
        if (slide == this.active_slide) return (this.active_slide = null);
        this.active_slide = slide;
      },
      goToCreateGame(gameName) {
        this.$router.push("/create/" + gameName.toLowerCase());
      },
    },
  };
</script>

<style>
  .shell-hooper {
    position: relative;
  }
  .hooper-prev,
  .hooper-next {
    outline: none;
    background: rgba(0, 0, 0, 0.377);
  }
  .hooper-slide {
    background-image: linear-gradient(
      0deg,
      rgba(32, 38, 57, 1) 11.4%,
      rgb(44, 53, 83) 70.2%
    );
    display: -webkit-flex;
    display: flex;
    color: #fff;
    margin: 3px;
    font-size: 30px;
    border-radius: 15px;
    width: 180px !important;
    height: 300px;
    border-radius: 10px;
    position: relative;
    transition: transform 0.5s;
    will-change: transform;
  }
  .hooper-list {
    overflow: visible;
  }
  .hooper {
    height: 305px;
    overflow: visible;
    margin-bottom: 50px;
    outline: none;
  }
  .hooper-slide-active {
    transform: scale(1.3);
    box-shadow: 0px 5px 20px -3px #2e75df65;
    z-index: 9999;
  }
  .subtopic-text {
    position: absolute;
    z-index: -99;
    color: rgba(255, 255, 255, 0.616);
    font-weight: 400;
    font-size: 8pt;
    padding: 0px 15px;
    position: absolute;
    top: 150px;
    transition: transform 0.6s;
    transform: translate(0, -60px);
    height: fit-content;
  }
  .subtopic-text-active {
    opacity: 1;
    position: relative;
    z-index: 0;
    transform: translate(0, 0px);
  }
  .subtopic-title {
    background: rgba(0, 0, 0, 0.308);
    padding: 12px 15px;
    border-radius: 10px;
    color: #fff;
    font-size: 16pt;
    font-weight: bold;
    text-shadow: 0px 3px 5px rgba(0, 0, 0, 0.486);
    transition: transform 0.5s;
    will-change: transform;
  }
  .subtopic-title-active {
    transform: translate(0, 75px);
    background: rgba(0, 0, 0, 0);
    font-size: 18pt;
  }
  .shell-slide {
    display: flex;
    -webkit-justify-content: center;
    justify-content: center;
    align-items: center;
    color: #fff;
    font-size: 30px;
    border-radius: 15px;
    width: 180px !important;
    max-height: 300px;
    height: 300px;
    color: rgb(35, 48, 66);
    border-radius: 10px;
    position: relative;
    transition: all 0.2s;
    will-change: max-height;
  }
  .shell-slide-active {
    border-radius: 10px;
    position: absolute;
    top: 0;
    z-index: 99999;
    max-height: 100px;
    will-change: transform;
    transform: translate(0%, 0%);
    transition: max-height 0.2s;
  }
  .action-buttons-slide {
    position: absolute;
    bottom: 20px;
    width: 100%;
    opacity: 0;
    transition: transform 0.6s;
    position: absolute;
    z-index: -99;
    transform: translate(0, 60px);
    will-change: transform;
  }
  .action-buttons-slide-active {
    opacity: 1;
    z-index: 99;
    transform: translate(0, 0px);
  }
  @media only screen and (max-width: 540px) {
    .subtopic-title {
      padding: 12px 17px;
      font-size: 12pt;
    }
    .hooper-prev,
    .hooper-next {
      display: none;
    }
  }
</style>
