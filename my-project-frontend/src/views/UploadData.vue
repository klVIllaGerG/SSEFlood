<template>
    <div id="header" :style="{ background: 'url(\'https://th.bing.com/th/id/R.f312f0b1bb5874c7d50043a0b7371413?rik=labYEBLCafZ15w&riu=http%3a%2f%2fimg.yipic.cn%2fthumb%2f43a0ef91%2fd6c99759%2ff8561e22%2fb04f8677%2fbig_43a0ef91d6c99759f8561e22b04f8677.png%3fx-oss-process%3dimage%2fformat%2cwebp%2fsharpen%2c100&ehk=6YfO9APiwS5GwuqomVqOukCQIjFLiUez%2bqDRjoVcpJk%3d&risl=&pid=ImgRaw&r=0\')', backgroundSize: 'cover' }">
      <navTop></navTop>
    </div>


  <el-card class="overlay-container"  :style="{ background: 'url(\'src/assets/background1.png\')', backgroundSize: 'cover',opacity: '0.85' }">
    <template #header>
      <div class="card-header">
        <span class="upload-text">图片数据上传</span>
        <el-button type="primary" @click="uploadAllImages" :loading="uploading">上传所有图片</el-button>
      </div>
    </template>

    <div class="styled-table-container">
      <table class="styled-table">
        <tr>
          <td style="width: 10px;">1</td>
          <td style="width: 100px;">dem数据</td>
          <td >  <el-upload
              ref="fileInputs"
              :auto-upload="false"
              :on-change="handleFileChange"
              :before-upload="beforeUpload"
              :file-list="fileList">

            <el-button slot="trigger" type="primary" style="font-size: 12px; margin-top: 15% ;">选取文件</el-button>
          </el-upload></td>
        </tr>
        <tr>
          <td style="width: 10px;">2</td>
          <td style="width: 100px;">dem_slope数据</td>
          <td style="margin-right: 80px;">  <el-upload
              ref="fileInputs"
              :auto-upload="false"
              :on-change="handleFileChange"
              :before-upload="beforeUpload"
              :file-list="fileList">

            <el-button slot="trigger" type="primary" style="font-size: 12px; margin-top: 15%">选取文件</el-button>
          </el-upload></td>
        </tr>
        <tr>
          <td style="width: 10px;">3</td>
          <td style="width: 100px;">EIBI数据</td>
          <td style="margin-right: 80px;">  <el-upload
              ref="fileInputs"
              :auto-upload="false"
              :on-change="handleFileChange"
              :before-upload="beforeUpload"
              :file-list="fileList">

            <el-button slot="trigger" type="primary" style="font-size: 12px; margin-top: 15%">选取文件</el-button>
          </el-upload></td>
        </tr>
        <tr>
          <td style="width: 10px;">4</td>
          <td style="width: 100px;">flood数据</td>
          <td style="margin-right: 80px;">  <el-upload
              ref="fileInputs"
              :auto-upload="false"
              :on-change="handleFileChange"
              :before-upload="beforeUpload"
              :file-list="fileList">

            <el-button slot="trigger" type="primary" style="font-size: 12px; margin-top: 15%">选取文件</el-button>
          </el-upload></td>
        </tr>
        <tr>
          <td style="width: 10px;">5</td>
          <td style="width: 100px;">water数据</td>
          <td style="margin-right: 80px;">  <el-upload
              ref="fileInputs"
              :auto-upload="false"
              :on-change="handleFileChange"
              :before-upload="beforeUpload"
              :file-list="fileList">

            <el-button slot="trigger" type="primary" style="font-size: 12px; margin-top: 15%">选取文件</el-button>
          </el-upload></td>
        </tr>
        <tr>
          <td style="width: 10px;">6</td>
          <td style="width: 100px;">rs数据</td>
          <td style="margin-right: 80px;">  <el-upload
              ref="fileInputs"
              :auto-upload="false"
              :on-change="handleFileChange"
              :before-upload="beforeUpload"
              :file-list="fileList">

            <el-button slot="trigger" type="primary" style="font-size: 12px; margin-top: 15%">选取文件</el-button>
          </el-upload></td>
        </tr>
        <tr>
          <td style="width: 10px;">7</td>
          <td style="width: 100px;">glcm数据</td>
          <td style="margin-right: 80px;">  <el-upload
              ref="fileInputs"
              :auto-upload="false"
              :on-change="handleFileChange"
              :before-upload="beforeUpload"
              :file-list="fileList">

            <el-button slot="trigger" type="primary" style="font-size: 12px; margin-top: 15%">选取文件</el-button>
          </el-upload></td>
        </tr>
        <tr>
          <td style="width: 10px;">8</td>
          <td style="width: 100px;">MNDWI数据</td>
          <td style="margin-right: 80px;">  <el-upload
              ref="fileInputs"
              :auto-upload="false"
              :on-change="handleFileChange"
              :before-upload="beforeUpload"
              :file-list="fileList">

            <el-button slot="trigger" type="primary" style="font-size: 12px; margin-top: 15%">选取文件</el-button>
          </el-upload></td>
        </tr>
        <tr>
          <td style="width: 10px;">9</td>
          <td style="width: 100px;">NDVI数据</td>
          <td style="margin-right: 80px;">  <el-upload
              ref="fileInputs"
              :auto-upload="false"
              :on-change="handleFileChange"
              :before-upload="beforeUpload"
              :file-list="fileList">

            <el-button slot="trigger" type="primary" style="font-size: 12px; margin-top: 15%">选取文件</el-button>
          </el-upload></td>
        </tr>
      </table>

    </div>
    </el-card>
    <div v-if="uploadError">
      <p>上传失败</p>
      <p>错误信息: {{ uploadError }}</p>
    </div>

    <div class="overlay-container-1" :style="{ background: 'url(\'src/assets/background1.png\')', backgroundSize: 'cover',opacity: '0.85' }">
      <el-card>
        <template #header>
          <div class="card-header">
            <span class="upload-text">测绘地图生成</span>
            <el-button @click="generateMapWithLoading" :loading="loadingMap" class="upload-button">点击生成</el-button>
            <el-button @click="generateMap" class="upload-button">查看地图</el-button>
            <el-button @click="exportImage" class="upload-button">导出图片</el-button>
          </div>
        </template>
        <div>
          <!-- 使用 v-if 判断是否有地图图片数据，有则显示图片 -->
          <img v-if="mapImageSrc" :src="mapImageSrc" alt="生成的地图">
          <p v-else>请先生成地图</p>
        </div>
      </el-card>
    </div>
</template>

<script>
import axios from 'axios';
import navTop from "@/components/navTop.vue"
import {ElMessage} from "element-plus";
import NavTop from "@/components/navTop.vue";
export default {
  components: {NavTop},
  data() {
    return {
      uploadError: null,
      selectedFiles: [],
      fileList: [],
      uploading: false,
      mapImageSrc: null,  // 添加一个用于存储地图图片的变量
      loadingMap: false, // 添加一个用于控制生成地图按钮加载状态的变量
    };
  },
  methods: {
    handleFileChange(file, fileList) {
      this.selectedFiles = this.selectedFiles.concat(fileList);
    },
    beforeUpload(file) {
      // 如果需要在上传前进行一些操作，可以在这里处理
      return true; // 返回 true 表示允许上传
    },
    uploadAllImages() {
      this.uploadError = null;
      this.uploading = true;

      Promise.all(this.selectedFiles.map((file, index) => this.uploadImage(file, index)))
        .then(() => {
          this.selectedFiles = []
          this.fileList = []
          ElMessage.success({
            message: '所有图片上传成功',
            duration: 3000, // 设置显示时间，单位为毫秒
          });
        })
        .catch(error => {
          console.error("至少有一个图片上传失败", error);

          // 输出详细的错误信息
          if (error.response) {
            this.uploadError = `服务器响应状态码: ${error.response.status}, 服务器响应数据: ${error.response.data}`;
          } else if (error.request) {
            this.uploadError = "没有收到服务器响应";
          } else {
            this.uploadError = `请求设置时发生错误: ${error.message}`;
          }
        })
        .finally(() => {
          this.uploading = false;
        });
    },
    uploadImage(file, index) {
      if (!file) {
        return Promise.resolve(); // 如果没有选择文件，则返回 resolved Promise
      }

      const formData = new FormData();
      formData.append("image", file.raw);

      // 使用 Promise 封装上传逻辑
      return new Promise((resolve, reject) => {
        axios.post('http://127.0.0.1:5000/upload', formData, {
          headers: {
            'Content-Disposition': `attachment; filename=${file.name}`,
          },
        })
          .then(response => {
            // 处理上传成功的响应
            console.log(`图片 ${index + 1} 上传成功`, response.data);
            resolve();
          })
          .catch(error => {
            // 处理上传失败的错误
            console.error(`图片 ${index + 1} 上传失败`, error);
            reject(error);
          });
      });
    },
    generateMapWithLoading() {
      this.loadingMap = true; // 开始加载状态

      axios.get('http://127.0.0.1:5000/create_image')
          .then(response => {
            this.loadingMap = false;
            ElMessage.success({
              message: '生成成功',
            });
          })
          .catch(error => {
          });


    },

    generateMap() {
      axios.get('http://127.0.0.1:5000/get_image', { responseType: 'arraybuffer' })
          .then(response => {
            // 将二进制数据转换为base64格式
            const base64Image = btoa(
                new Uint8Array(response.data)
                    .reduce((data, byte) => data + String.fromCharCode(byte), '')
            );

            // 设置到mapImageSrc变量中
            this.mapImageSrc = `data:image/png;base64,${base64Image}`;
          })
          .catch(error => {
            console.error('获取地图图片数据失败', error);
          });
    },
    exportImage() {
      if (this.mapImageSrc) {
        // 创建一个虚拟的下载链接
        const link = document.createElement('a');
        // 设置链接的属性
        link.href = this.mapImageSrc;
        link.download = 'exported_image.png'; // 下载的文件名

        // 将链接添加到文档中
        document.body.appendChild(link);

        // 模拟点击链接进行下载
        link.click();

        // 从文档中移除链接
        document.body.removeChild(link);
      } else {
        // 如果没有图片，提示用户生成地图
        ElMessage.warning('请先生成地图');
      }
    },

  },
};
</script>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 40px;
}

.upload-text {
  color: #000000;
  /* 按钮文字颜色 */
  font-size: 22px;
  /* 例如，设置为16像素 */
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
}

.upload-button {
  background-color: #3498db;
  /* 按钮背景颜色 */
  color: #fff;
  /* 按钮文字颜色 */
  font-size: 16px;
  /* 例如，设置为16像素 */
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  /* 添加淡入效果 */

  /* 鼠标悬停时改变背景颜色 */
  &:hover {
    background-color: #2980b9;
  }
}

.text {
  font-size: 14px;
}


.overlay-container {
  position: absolute;
  top: 180px;
  left: 25%;
  transform: translate(-50%, -10%);
  background-color: rgba(255, 255, 255, 0.85);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 15px;
  width: 80%;
  max-width: 700px;
  max-height: 100%;
  overflow: auto;
}

.overlay-container-1 {
  position: absolute;
  top: 81px;
  left: 50%;
  background-color: rgba(255, 255, 255, 0.85);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 20px;
  width: 80%;
  max-width: 700px;
  max-height: 80%;
  overflow: auto;
  margin-top: 20px;
}

.styled-table-container {
  max-width: 1100px;
  /* 调整最大宽度，根据需要修改 */

  margin: 0 auto;
  /* 水平居中 */
}

.styled-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;

  /* 调整表格与上方的距离，根据需要修改 */
}

.styled-table td,
.styled-table th {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
  width: 120px;

  /* 设置宽度为 150 像素，根据需要修改 */
}

.styled-table th {
  background-color: #f2f2f2;
  /* 表头背景色 */
}

.styled-table td button {
  background-color: #4d8acf;
  /* 按钮背景色 */
  color: white;
  border: none;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.styled-table td button:hover {
  background-color: #2178e3;
  /* 按钮鼠标悬停时的背景色 */
}

.styled-table progress {

}
</style>
