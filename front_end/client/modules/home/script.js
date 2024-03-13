import story from "../story/story.vue";
import storyboard from "../storyboard/storyboard.vue";
import axios from 'axios';

export default {
    components: { // 依赖组件
        story,
        storyboard
    },
    data() { // 本页面数据
        return {
            // showMain: true,
            showMain: false,
            input_story: "",
            isButtonDisabled: true,
        };
    },
    watch: {
        input_story: function (val) {
            // console.log(val);
            if (val !== "") {
                    this.isButtonDisabled = false;
                    // console.log("button enabled");
            } else {
                    this.isButtonDisabled = true;
            }
        }
    },
    mounted() {

    },
    methods: { // 这里写本页面自定义方法 
        showMainPage() {
            this.generateStoryInfo();
            this.showMain = true;
        },
        generateStoryInfo: function () {
            const url = "/generate_story_info"; // 确保这个URL匹配你的代理配置
            const dataToSend = {
                message: this.input_story
            };

            axios.post(url, dataToSend)
                .then(response => {
                    console.log("后端响应:", response.data);
                    const data = response.data.message
                    console.log(data);
                    this.$bus.$emit('pass_story_info', data); // 传递数据给子组件   
                })
                .catch(error => {
                    console.error("请求错误:", error);
                });
        }

    },
    created() { // 生命周期中，组件被创建后调用

    },
};