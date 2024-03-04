<template>
  <div>
  <div id="header" :style="{ background: 'url(\'https://th.bing.com/th/id/R.f312f0b1bb5874c7d50043a0b7371413?rik=labYEBLCafZ15w&riu=http%3a%2f%2fimg.yipic.cn%2fthumb%2f43a0ef91%2fd6c99759%2ff8561e22%2fb04f8677%2fbig_43a0ef91d6c99759f8561e22b04f8677.png%3fx-oss-process%3dimage%2fformat%2cwebp%2fsharpen%2c100&ehk=6YfO9APiwS5GwuqomVqOukCQIjFLiUez%2bqDRjoVcpJk%3d&risl=&pid=ImgRaw&r=0\')', backgroundSize: 'cover' }">
    <navTop></navTop>
  </div>
  <div class="news-page" :style="{ background: 'url(\'src/assets/background.png\')', backgroundSize: 'cover',opacity: '0.85' }">
    <el-row :gutter="20">
      <el-col :span="24">
        <el-card class="news-container" :style="{opacity: '0.85' }">
          <el-row :gutter="20">
            <el-col v-for="news in newsList" :key="news.id" :span="24">
              <el-card @click="goToDetail(news.id)" class="news-card">
                <div class="news-header">
                  <img :src="news.image" class="news-image" alt="News Image" />
                  <div class="news-info">
                    <h3>{{ news.title }}</h3>
                    <p>{{ news.summary }}</p>
                  </div>
                </div>
              </el-card>
            </el-col>
            <el-button type="primary" class="more-button" @click="openExternalSite"  >查看更多</el-button>
          </el-row>

        </el-card>
      </el-col>
    </el-row>


    <el-dialog v-model="dialogVisible" width="80%" >
  <!-- 自定义对话框的内容 -->
  <div>
    <h2 class="Title">{{ title }}</h2>
    <p  class="multiline" > {{ content }}</p>
  </div>

  <!-- 自定义对话框的底部 -->
  <div slot="footer" class="custom-dialog-footer">
    <el-button style="margin-right: 10px;"   @click="dialogVisible = false" >关闭</el-button>
  </div>

  <!-- 在这里插入内部对话框 -->
  <el-dialog v-model="innerVisible" width="30%" title="Inner Dialog" append-to-body>
    <!-- 自定义内部对话框的内容 -->
    <div>
      <h3>Custom Content for Inner Dialog</h3>
      <p>This is your custom content for the inner dialog.</p>
    </div>

    <!-- 内部对话框的底部 -->
    <div slot="footer" class="custom-dialog-footer">
      <el-button @click="innerVisible = false">Close Inner Dialog</el-button>
    </div>
  </el-dialog>
</el-dialog>

    <!-- 弹窗部分 -->
  </div>
  </div>
  
</template>

<script>
import navTop from "@/components/navTop.vue"
import axios from 'axios';
import NavTop from "@/components/navTop.vue";
export default {
  components: {NavTop},
  data() {
    return {
      newsList: [
        {
          id: "news1",
          title: '全力以赴打赢防汛抢险硬仗——华北、黄淮等地抗击汛情一线直击',
          summary: '受台风“杜苏芮”北上影响，7月29日至8月1日，华北、黄淮等地出现极端降雨过程，海河发生流域性较大洪水，子牙河、大清河、永定河先后发生编号洪水，河北多地、北京西南部地区洪涝地质灾害严重，造成重大人员伤亡和财产损失。',
          image: 'https://www.gov.cn/yaowen/liebiao/202308/W020230802280047464233_ORIGIN.JPG',
        },
        {
          id: "news2",
          title: '确保人民群众安居乐业、温暖过冬——京津冀和东北等地洪涝灾后重建观察',
          summary: '经历了洪水考验的地区灾后重建进展如何？受灾群众能否安全温暖过冬？当地应对极端灾害能力又有哪些新变化？新年前夕，新华社记者兵分多路实地探访。跟着记者的步伐，一起关注受灾群众温暖过冬。',
          image: 'src/assets/news2.png',
        },
        {
          id: "news3",
          title: '世界周刊丨“极端天气”背后',
          summary: '山火、高温、暴雨、飓风、洪水，你是否觉得今年全球的极端天气格外多？英国天空电视台注意到，仅过去一个星期，极端天气就袭击了美国、澳大利亚、印度和阿根廷。此前，美国气象学家贝拉尔代利发出警告，2023年或将是全球极端天气的惊人之年。',
          image: 'src/assets/news3.png',
        },
        // 其他新闻...
      ],
      dialogVisible: false, // 新增属性，用于控制弹窗的显示与隐藏
      title:"",
      content: "",
      image:"",
      };
  },
  methods: {
    goToDetail(newsId) {
      // 打开弹窗
      this.dialogVisible = true;
      // 点击小框框跳转到新闻详情页，你可以在这里加入路由跳转逻辑
      axios.get(`http://127.0.0.1:5000/download_news?news_key=${newsId}`)
          .then(response => {
            const res = response.data
            console.log(res)
            this.title = res.title
            this.content =res.content
            ;
            this.loadingMap = false
          })
          .catch(error => {
            console.log("get失败")
          });
      console.log(`进入新闻详情页,新闻ID:${newsId}`);
    },
    openExternalSite() {
      // 点击查看更多按钮在新标签页中打开站外网站
      window.open('https://so.ifeng.com/?q=%E6%B4%AA%E6%B0%B4&c=1', '_blank');
    },
  },
};
</script>

<style>
.news-page {
  padding: 20px;
}

.news-container {
  padding: 20px;

  .news-card {
    cursor: pointer;
    transition: transform 0.3s ease;

    &:hover {
      transform: scale(1.05);
    }

    .news-header {
      display: flex;
      align-items: center;
      margin-bottom: 15px;

      .news-image {
        width: 400px;
        height: 220px;
        border-radius: 4px;
        object-fit: cover;
        margin-right: 15px;
      }

      .news-info {
        flex: 1;

        h3 {
          font-size: 18px;
          margin: 0;
        }

        p {
          font-size: 16px;
          margin: 0;
        }
      }
    }
  }

  .more-button {
    position: absolute;
    top: 10px;
    right: 10px;
  }
}

.Title{
  text-align: center;
  font-size: 28px;

}

.multiline{
  white-space: pre-line;
}
</style>
