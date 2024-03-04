<template>
  <div >
    <div id="header" :style="{ background: 'url(\'https://th.bing.com/th/id/R.f312f0b1bb5874c7d50043a0b7371413?rik=labYEBLCafZ15w&riu=http%3a%2f%2fimg.yipic.cn%2fthumb%2f43a0ef91%2fd6c99759%2ff8561e22%2fb04f8677%2fbig_43a0ef91d6c99759f8561e22b04f8677.png%3fx-oss-process%3dimage%2fformat%2cwebp%2fsharpen%2c100&ehk=6YfO9APiwS5GwuqomVqOukCQIjFLiUez%2bqDRjoVcpJk%3d&risl=&pid=ImgRaw&r=0\')', backgroundSize: 'cover' }">
      <navTop></navTop>
    </div>

    <div :style="{ background: 'url(\'src/assets/background.png\')', backgroundSize: 'cover'}">
  <div class="app-container" :style="{opacity: '0.85' }">
    <el-row>
      <!-- 第一个图片框 -->
      <el-col :span="12">
        <el-card class="image-card" header="广州历史洪水数据">
          <img src='/src/assets/GuangzhouHis.png' alt="历史洪水数据">
        </el-card>
      </el-col>

      <!-- 第二个图片框 -->
      <el-col :span="12">
        <el-card class="image-card" header="广州洪水敏感性图">
          <img src='/src/assets/GuangzhouSens.png' alt="洪水敏感性图">
        </el-card>
      </el-col>
    </el-row>

    <el-divider></el-divider>

    <!-- 文本框 -->
    <el-row>
      <el-col :span="24">
        <el-card class="info-card" header="分析与建议">
          <div v-if="floodInfo" class="indented-text">{{ floodInfo }}</div>
          <div v-else>Loading...</div>
        </el-card>
      </el-col>
    </el-row>
  </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ElMessage } from "element-plus";
import NavTop from "@/components/navTop.vue";

export default {
  components: {NavTop},
  data() {
    return {
      floodInfo: "",
      loading: true,
    };
  },
  mounted() {
    // 调用接口获取洪水易发信息
    this.fetchFloodInfo();
  },
  methods: {
    fetchFloodInfo() {
      axios
          .get("/api/suggest/all")
          .then((response) => {
            console.log(response.data.data[1].suggestions);
            this.floodInfo = response.data.data[1].suggestions;
          })
          .catch((error) => {});
    },
    get(url, successCallback, errorCallback) {
      this.axios
          .get(url)
          .then((response) => {
            if (successCallback) successCallback(response);
          })
          .catch((error) => {
            if (errorCallback) errorCallback(error);
          });
    },
  },
};
</script>

<style scoped>
.app-container {
  padding: 20px;
}

/* 新增样式规则 */
.indented-text::first-line {
  text-indent: 20em; /* 或者使用其他单位，如px、rem等 */
}

.image-card {
  margin-bottom: 20px;
  height: 690px; /* 调整为你想要的固定高度 */
}

.info-card {
  margin-top: 20px;
}
</style>
