<template>
  <div   :style="{ opacity: '0.4' }">
    <div class="common-layout">
      <el-container>
        <el-header class="header-layout">
          <el-container >
            <el-aside width="40%">
              <el-menu :default-active="activeIndex" class="el-menu-demo"  mode="horizontal" @select="handleSelect">
                <el-menu-item index="home" class="hollow" @click="toHome()">首页</el-menu-item>
                <el-menu-item index="news" class="hollow" @click="toNews()">新闻中心</el-menu-item>
                <el-sub-menu index="flood">
                  <template #title>
                    <span class="hollow" >洪水测绘图</span>
                  </template>
                  <el-menu-item index="flood-shanghai" class="hollow2" style="margin-left: 10%;" @click="toExam()">广州洪水风险图</el-menu-item>
                  <el-menu-item index="flood-custom" class="hollow2"  @click="uploadTif()">自定义洪水风险图</el-menu-item>

                </el-sub-menu>
              </el-menu>
            </el-aside>
            <el-button @click="logout()" type="danger" style="margin-top: 15px;margin-left: 50%;font-size: 20px;  font-weight: bold;"  plain> 退出登录</el-button>
          </el-container>
        </el-header>
      </el-container>
    </div>
  </div>
</template>

<script setup>
import {get} from "@/net";
import {ElMessage} from "element-plus";
import router from "@/router";
import {reactive, ref} from "vue";
import {useStore} from "@/stores";

const store = useStore()

const toHome = () => {
  router.push('/index')
}
const toNews = () => {
  router.push('/news')
}

const uploadTif = () => {
  router.push('/upload')
}

const toExam = () => {
  router.push('/examPage')
}

const logout = () => {
  get('/api/auth/logout', (message) => {
    ElMessage.success(message)
    console.log(store.auth.user)
    store.auth.user = null
    router.push('/')
  })
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

.hollow2{
  font-size: 18px;
  position: relative;
  color: #333;
  text-shadow: 2px 2px 0 #fff, -2px -2px 0 #fff, 2px -2px 0 #fff, -2px 2px 0 #fff;
  
}




.hollow{

  font-size: 27px;
  color: rgba(0,0,0,2);
  font-weight: bold;
}
</style>