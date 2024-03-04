<template>
  <div style="width: 100vw;height: 100vh;overflow: hidden;display: flex">
    <div style="flex: 1">
      <el-image style="width: 100%;height: 100%" fit="cover"
                src="https://cdn.pixabay.com/photo/2015/08/05/14/52/high-water-876580_1280.jpg"/>
    </div>
    <div class="welcome-title">
      <h1>FloodSenseMap</h1>
    </div>
    <div style="width: 400px;background-color: white;z-index: 1">
      <router-view v-slot="{ Component }">
        <transition name="el-fade-in-linear" mode="out-in">
          <component :is="Component" style="height: 100%"/>
        </transition>
      </router-view>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Cairo');
.welcome-title {
  position: absolute;
  bottom: 30px;
  right: 380px;
  color: white;
  text-shadow: 0 0 10px rgb(118, 169, 189);
}


body {
  background-color: #010;
}

.title {
  font-family: "Cairo";
  text-align: center;
  color: #FFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  letter-spacing: 1px;
  line-height: 2;
}

h1 {
  background-image: url(https://cdn.pixabay.com/animation/2023/01/24/23/10/23-10-47-824_512.gif);
  background-size: cover;
  color: transparent;
  -webkit-background-clip: text;
  font-size: 100px;
  margin: 10px 0;
}

/* styling my button */


</style>

