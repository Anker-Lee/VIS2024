import * as echarts from 'echarts';
import axios from 'axios';

export default {
    components: { // 依赖组件

    },
    data() { // 本页面数据
        return {
            inputMsg: "",
        };
    },
    watch: {

    },
    mounted() {

    },
    methods: { // 这里写本页面自定义方法 
        testBackend: function () {
            const url = "/test"; // 确保这个URL匹配你的代理配置
            const dataToSend = {
                message: this.inputMsg
            };

            axios.post(url, dataToSend)
                .then(response => {
                    console.log("后端响应:", response.data);
                    const data = response.data.message
                    const chatResponse = document.getElementById('chatResponse');
                    chatResponse.innerHTML = `GPT: ${data}`;
                })
                .catch(error => {
                    console.error("请求错误:", error);
                });
        },

    },
    created() { // 生命周期中，组件被创建后调用

    },
};