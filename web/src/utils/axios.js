import axios from "axios";
import qs from "qs";
const service = axios.create({
  baseURL: "/api", 
  timeout: 5000,
  withCredentials: true,
   headers: {
     "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
   }
});

service.interceptors.request.use(
  (config) => {
    if (config.method === "post") {
      let curPost = config.url.split("/")[config.url.split("/").length - 1];
      if (curPost === "uploadpicture" || curPost === "fileUpload") {
        return config; // 这里对上传文件/图片的 api 不做传参序列化处理
      } else {
        config.data = qs.stringify(config.data);
        return config;
      }
    }
    return config;
  },
  (error) => {
    console.log(error);
    return Promise.reject();
  }
);
service.interceptors.response.use(response => {
  //接收到响应数据并成功后的一些共有的处理，关闭loading等
   if (response.status === 200) {
      return response.data;
    } else {
      console.log(response);
      Promise.reject();
    }
}, error => {
   /***** 接收到异常响应的处理开始 *****/
  if (error && error.response) {
    // 1.公共错误处理
    // 2.根据响应码具体处理
    
  } else {
    // 超时处理
    
  }
  //Message.error(error.message)
  /***** 处理结束 *****/
  //如果不需要错误处理，以上的处理过程都可省略
  return Promise.resolve(error.response)
})

export default service;
