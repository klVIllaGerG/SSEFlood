<template>
  <div id="header" :style="{ background: 'url(\'https://th.bing.com/th/id/R.f312f0b1bb5874c7d50043a0b7371413?rik=labYEBLCafZ15w&riu=http%3a%2f%2fimg.yipic.cn%2fthumb%2f43a0ef91%2fd6c99759%2ff8561e22%2fb04f8677%2fbig_43a0ef91d6c99759f8561e22b04f8677.png%3fx-oss-process%3dimage%2fformat%2cwebp%2fsharpen%2c100&ehk=6YfO9APiwS5GwuqomVqOukCQIjFLiUez%2bqDRjoVcpJk%3d&risl=&pid=ImgRaw&r=0\')', backgroundSize: 'cover' }">
    <navTop></navTop>
  </div>

  <div>
    <div class="common-layout">
      <el-container>
        <el-header class="header-layout">
          <el-container>
            
            
          </el-container>
        </el-header>

        <el-main>
          <div class="block text-center" m="t-4">
            <span class="demonstration"></span>
            <el-carousel :interval="4000" type="card" height="500px">
              <el-carousel-item v-for="item in imageSourcesTop" :key="item.name" :name="item.name">
                <img :src="item.src" alt="carousel-item" style="width: 100%; height: 100%;">
                <!-- <h3 class="small justify-center" text="2xl">{{ item }}</h3> -->
              </el-carousel-item>
            </el-carousel>
          </div>
        </el-main>

        <el-footer class="footer-layout">
          <div class="footer-module" style="border: 20px solid #ddd; padding: 100px;">
            <h3 class="module-title text-center" style="font-size: 25px;">——— 洪 水 简 介 ———</h3>
            <p class="module-content" style="font-size: 20px; color:rgb(255, 127, 127) ;">
              &emsp;&emsp;洪水灾害是一种突发性强、发生频率高、危害严重的自然灾害。我国每年因洪水灾害而造成的损失十分巨大。据初步统计，我国约有50％的人口和70％的财产分布在洪水威胁区域。<br>
              &emsp;&emsp;本网站主要功能为洪水敏感性测绘，通过分析某地历史上的洪水、降雨、地质等信息，测绘出该地洪水灾害风险、洪水敏感性评价和管理的基础性工作，是制定各项防洪减灾措施，尤其是非工程防洪减灾措施的重要依据。为洪水风险管理和防洪减灾规划提供借鉴，能有效降低洪灾隐患，提高抗洪救灾能力，减轻洪灾损失。
            </p>
          </div>

          <div class="footer-module" style="border: 1px solid #ddd; padding: 10px;">
            <h3 class="module-title text-center" style="font-size: 25px;">——— 洪 水 知 识 ———</h3>
            <el-row class="image-container">
              <el-col v-for="item in imageSourcesFoot" :key="item.name" :span="8">
                <img :src="item.src" alt="洪水知识" style="width: 100%; height: 100%;">
              </el-col>
            </el-row>
          </div>
        </el-footer>
      </el-container>
    </div>
  </div>
</template>

<script setup>
import navTop from "@/components/navTop.vue"
import {get} from "@/net";
import {ElMessage} from "element-plus";
import router from "@/router";
import {reactive, ref} from "vue";
import {useStore} from "@/stores";

const store = useStore()

const imageSourcesTop =  [
  { name: 'image1', src: 'src/assets/hengfu1.png'},
  { name: 'image2', src: 'src/assets/hengfu2.png' },
  { name: 'image3', src: 'src/assets/hengfu3.png' },
  // Add more images as needed
];
const imageSourcesFoot =  [
  { name: 'poster1', src: 'src/assets/hongshuizhishi1.png' },
  { name: 'poster2', src: 'src/assets/hongshuizhishi2.png' },
  { name: 'poster3', src: 'src/assets/hongshuizhishi3.png' },
  // Add more images as needed
];


const uploadTif = () => {
  router.push('/upload')
}
</script>

<style scoped>

.text-center {
  text-align: center;
}

.module-title {
  margin-bottom: 20px;
  color: var(--el-text-color-secondary);
  font-size: 18px;
  text-align: center;
}

a {
  text-decoration: none;
}

.image-container {
  display: flex;
  justify-content: space-around;
  text-align: center;
}

.demonstration {
  color: var(--el-text-color-secondary);
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>