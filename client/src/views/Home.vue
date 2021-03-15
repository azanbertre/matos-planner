<template>
  <div>
    <div class="home">
      <div class="shell-home">
        <div class="shell-left">
          <div class="text-left">
            <h1 class="title-left">
              UM NOVO JEITO DE ESTUDAR MATEMÁTICA
            </h1>
            <div class="divider"></div>
            <p class="secondary-text">
              No Smart Math os alunos aprendem e praticam a matemática de um
              jeito único com diversas dinâmicas e gameficação
            </p>
            <v-row class="mt-4 mb-5">
              <v-col cols="12" sm="9" md="6" xl="4" class="pa-3">
                <v-btn color="#0077FF" block dark class="ma-3 go-to-play-button" @click="goToPlay" x-large
                  >entrar no jogo</v-btn
                >
              </v-col>
              <v-col cols="12" sm="9" md="6" xl="4" class="pa-3">
                <v-btn
                  color="#FFF"
                  block
                  x-large
                  class="ma-3 create-game-button"
                  @click="$vuetify.goTo('#create-game-div', options)"
                >
                  criar um jogo
                </v-btn>
              </v-col>
            </v-row>
          </div>
        </div>
      </div>
    </div>
    <div class="container-topics" v-intersect="onIntersect" id="create-game-div">
      <v-row justify="center" class="my-10 pa-3">
        <v-col
          cols="6"
          sm="4"
          md="2"
          v-for="(section, index) in mathSections"
          :key="section.id"
        >
          <v-card
            :class="['card-section d-flex justify-center align-center', actualMathSection == index ? ' card-section-active': '']"
            dark
            :color="section.color"
            :style="'box-shadow: 0px 15px 30px' + section.color + 94"
            @click="actualMathSection = index"
          >
            <h1 class="section-title">{{ section.title }}</h1>
          </v-card>
        </v-col>
      </v-row>
      <div
        class="topics-shell"
        v-for="topic in mathSections[actualMathSection].topics"
        :key="topic.id"
      >
        <v-row class="topic-title">
          <h3>{{ topic.title }}</h3>
        </v-row>
        <topics-carousel :elements="topic.sub_topics" />
      </div>
    </div>
  </div>
</template>

<style>
  .home {
    overflow: hidden;
    height: 100vh;
    width: 100%;
  }
  .shell-home {
    width: 100%;
    height: 100%;
    background: url("../assets/back-home.png") center/cover;
  }
  .shell-left {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    width: 50vw;
    height: 100vh;
    flex-direction: column;
    padding-left: 8vw;
  }
  .title-left {
    font-size: 6vh;
    width: 90%;
    margin: 0px;
    text-transform: uppercase;
    margin-top: 60px;
    color: #2b4a6d;
  }
  .text-left {
    margin-bottom: 80px;
  }
  .divider {
    width: 6vw;
    height: 10px;
    border-radius: 100px;
    margin-top: 10px;
    margin-bottom: 30px;
    background: #0077ff;
  }
  .secondary-text {
    width: 60%;
    font-size: 14pt;
    text-align: justify;
  }

  .card-actions-body {
    background: #fff;
    height: 10vh;
    display: flex;
    align-items: flex-end !important;
    justify-content: flex-end;
  }
  .topics-shell {
    position: relative;
  }
  .container-topics {
    transition: 0.9s;
    padding-top: 30px;
    background: #ffffff;
    width: 100%;
  }
  .topic-title {
    margin-left: 43px;
    position: absolute;
    top: -28px;
  }
  .card-section {
    width: 100%;
    height: 100px;
    border-radius: 15px !important;
    transition: 0.5s !important;
    cursor: pointer;
    filter: grayscale(0.7);
  }
  .card-section-active{
    border-bottom: 12px solid rgba(0, 0, 0, 0.473) !important;
    transform: scale(0.95);
    filter: grayscale(0);
  }
  .card-section:hover {
    filter: grayscale(0.4);
  }
  .container-topics {
    overflow-x: hidden;
  }
  .go-to-play-button{
    box-shadow: 0px 10px 30px #1482ff7a !important;
  }
  .create-game-button{
    box-shadow: 0px 10px 30px #18499223 !important;
    color: #0077ff !important;
  }
  @media only screen and (max-width: 600px) {
    .shell-home {
      background: url("../assets/back-home-mobile.png") center/cover;
      background-position-y: -38px;
    }
    .shell-left {
      width: 75%;
    }
    .secondary-text {
      width: 90%;
    }
    .topics-shell {
      margin-bottom: 140px;
    }
    .section-title {
      font-size: 17pt;
    }
    .title-left {
      font-size: 3.5vh;
      width: 82%;
    }
  }
</style>

<script>
  import TopicsCarousel from "@/components/TopicsCarousel.vue";
  export default {
    name: "Home",
    components: { TopicsCarousel },
    data() {
      return {
        teacherName: "Test Nome Professor",
        classes: [],
        showCreateRoom: false,
        rooms: [],
        isIntersecting: false,
        showCode: false,
        actualMathSection: 0,
        mathSections: [
          {
            title: "Algebra",
            id: "32hahv",
            color: "#1edb7b",
            topics: [
              {
                id: 1,
                title: "Riffpath",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 2,
                title: "Podcat",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 3,
                title: "Gigazoom",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 4,
                title: "Rhybox",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 5,
                title: "Skibox",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 6,
                title: "Wikizz",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 7,
                title: "Jaloo",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 8,
                title: "Blogspan",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 9,
                title: "Skippad",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 10,
                title: "Browsecat",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
            ],
          },
          {
            title: "Geometria",
            id: "32dasv",
            color: "#9355e5",
            topics: [
              {
                id: 1,
                title: "Riffpath2",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 2,
                title: "Podcat",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 3,
                title: "Gigazoom",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 4,
                title: "Rhybox",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 5,
                title: "Skibox",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 6,
                title: "Wikizz",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 7,
                title: "Jaloo",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 8,
                title: "Blogspan",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 9,
                title: "Skippad",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
              {
                id: 10,
                title: "Browsecat",
                sub_topics: [
                  {
                    id: 1,
                    title: "Twitterworks",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 2,
                    title: "Avamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 3,
                    title: "Fanoodle",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 4,
                    title: "Blogpad",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 5,
                    title: "Ntag",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 6,
                    title: "Oyondu",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 7,
                    title: "Babbleopia",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 8,
                    title: "Avaveo",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 9,
                    title: "Yambee",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                  {
                    id: 10,
                    title: "Quamba",
                    text:
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolor",
                  },
                ],
              },
            ],
          }
        ],
      };
    },
    mounted() {
      if(this.$router.history.current.hash.includes('#create-game-div')){
        this.$vuetify.goTo('#create-game-div', this.options)
      }
    },
    computed:{
      options () {
        return {
          duration: 1000,
          offset: 0,
          easing: 'easeInOutCubic',
        }
      }
    },
    methods: {
      goToPlay(){
        this.$router.push("/jogar");
      },
      onIntersect(entries, observer) {
        this.isIntersecting = entries[0].isIntersecting;
      },
    },
  };
</script>
